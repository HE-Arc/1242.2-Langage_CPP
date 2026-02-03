from pathlib import Path
import re
import tomllib
from xml.parsers.expat import errors
import argparse


INCLUDE_RE = re.compile(r'^\s*<!--\s*SNIPPET:INCLUDE\s+source_file=([^\s]+)\s+id=([A-Za-z0-9_.-]+)\s*-->\s*$')

SNIPPET_BEGIN_RE = re.compile(r'^\s*//@\s*SNIPPET:BEGIN\s+([A-Za-z0-9_.-]+)\s*$')
SNIPPET_END_RE   = re.compile(r'^\s*//@\s*SNIPPET:END\s+([A-Za-z0-9_.-]+)\s*$')

SNIPPET_BLOCK_BEGIN_RE = re.compile(r'^\s*<!--\s*SNIPPET:BEGIN\s+source_file=([^\s]+)\s+id=([A-Za-z0-9_.-]+)\s*-->\s*$')

SNIPPET_BLOCK_END_RE = re.compile(r'^\s*<!--\s*SNIPPET:END\s*-->\s*$')

def scan_markdown_for_includes(content_root: Path):
    includes = []

    for md_file in content_root.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8", errors="replace")
        lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

        for lineno, line in enumerate(lines, start=1):
            m = INCLUDE_RE.match(line)
            if not m:
                continue

            source_file = m.group(1)
            snippet_id = m.group(2)

            includes.append({
                "md_file": md_file,
                "line": lineno,
                "source_file": source_file,
                "id": snippet_id,
            })

    return includes

def load_snippet_paths(config_path: Path, repo_root: Path) -> list[Path]:
    data = tomllib.loads(config_path.read_text(encoding="utf-8"))

    if "snippets" not in data or "paths" not in data["snippets"]:
        raise RuntimeError("Invalid config: missing [snippets].paths")

    paths = []
    for p in data["snippets"]["paths"]:
        path = (repo_root / p).resolve()
        if not path.exists():
            raise RuntimeError(f"Snippet path does not exist: {path}")
        paths.append(path)

    return paths


def scan_files_for_snippets(paths):
    snippets = {}

    for root in paths:
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in (".c", ".h", ".cpp"):
                continue

            text = path.read_text(encoding="utf-8", errors="replace")
            lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

            current_id = None
            buffer = []

            for lineno, line in enumerate(lines, start=1):
                m_begin = SNIPPET_BEGIN_RE.match(line)
                if m_begin:
                    if current_id is not None:
                        raise RuntimeError(
                            f"{path}:{lineno}: nested SNIPPET:BEGIN"
                        )
                    current_id = m_begin.group(1)
                    buffer = []
                    continue

                m_end = SNIPPET_END_RE.match(line)
                if m_end:
                    if current_id is None:
                        raise RuntimeError(
                            f"{path}:{lineno}: SNIPPET:END without BEGIN"
                        )
                    if m_end.group(1) != current_id:
                        raise RuntimeError(
                            f"{path}:{lineno}: SNIPPET:END id mismatch"
                        )

                    snippets.setdefault(path.name, {})[current_id] = "\n".join(buffer).rstrip()
                    current_id = None
                    buffer = []
                    continue

                if current_id is not None:
                    buffer.append(line)

            if current_id is not None:
                raise RuntimeError(
                    f"{path}: EOF: missing SNIPPET:END for '{current_id}'"
                )

    return snippets

def check_includes_against_snippets(includes, snippets):
    errors = 0

    for inc in includes:
        src = inc["source_file"]
        sid = inc["id"]
        md_file = inc["md_file"]
        line = inc["line"]

        if src not in snippets:
            print(
                f"{md_file}:{line}: error: undefined snippet file '{src}'"
            )
            errors += 1
            continue

        if sid not in snippets[src]:
            print(
                f"{md_file}:{line}: error: undefined snippet '{sid}' in file '{src}'"
            )
            errors += 1

    return errors

def replace_includes_in_markdown(md_path, snippets):
    original = md_path.read_text(encoding="utf-8", errors="replace")
    lines = original.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    # Step 1: normalize
    lines = normalize_generated_blocks_to_includes(lines)

    out = []
    modified = False

    for line in lines:
        m = INCLUDE_RE.match(line)
        if not m:
            out.append(line)
            continue

        source_file = m.group(1)
        snippet_id = m.group(2)

        content = snippets[source_file][snippet_id]

        block = [
            f"<!-- SNIPPET:BEGIN source_file={source_file} id={snippet_id} -->",
            "<!--",
            "  GENERATED FILE — DO NOT EDIT.",
            "  This block is automatically regenerated.",
            "-->",
            "```c",
            content,
            "```",
            "<!-- SNIPPET:END -->",
        ]

        out.extend(block)
        modified = True

    new_text = "\n".join(out)

    # Force LF output, only write if changed
    normalized_original = original.replace("\r\n", "\n").replace("\r", "\n")
    if new_text != normalized_original:
        md_path.write_text(new_text, encoding="utf-8", newline="\n")
        return True

    return False

def remove_generated_snippet_blocks(lines):
    out = []
    inside = False

    for line in lines:
        if SNIPPET_BLOCK_BEGIN_RE.match(line):
            inside = True
            continue

        if inside:
            if SNIPPET_BLOCK_END_RE.match(line):
                inside = False
            continue

        out.append(line)

    if inside:
        raise RuntimeError("Unclosed SNIPPET:BEGIN block in markdown")

    return out

def normalize_generated_blocks_to_includes(lines):
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m = SNIPPET_BLOCK_BEGIN_RE.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        source_file = m.group(1)
        snippet_id = m.group(2)

        # Skip until END
        j = i + 1
        while j < len(lines) and not SNIPPET_BLOCK_END_RE.match(lines[j]):
            j += 1
        if j >= len(lines):
            raise RuntimeError("Unclosed SNIPPET:BEGIN block in markdown (missing SNIPPET:END)")

        out.append(f"<!-- SNIPPET:INCLUDE source_file={source_file} id={snippet_id} -->")
        i = j + 1

    return out


def main():
    import argparse

    repo_root = Path(__file__).resolve().parent.parent
    content_root = repo_root / "content"

    parser = argparse.ArgumentParser(prog="hugo_preprocessor.py")
    parser.add_argument(
        "command",
        nargs="?",
        choices=["scan", "clean", "replace"],
        help="scan | clean | replace (default: clean + scan + replace)",
    )
    args = parser.parse_args()

    if not content_root.exists():
        raise RuntimeError(f"content/ directory not found at {content_root}")

    def do_clean():
        modified = 0
        for md_file in content_root.rglob("*.md"):
            original = md_file.read_text(encoding="utf-8", errors="replace")
            norm = original.replace("\r\n", "\n").replace("\r", "\n")
            lines = norm.split("\n")

            new_lines = normalize_generated_blocks_to_includes(lines)
            new_text = "\n".join(new_lines)

            if new_text != norm:
                md_file.write_text(new_text, encoding="utf-8", newline="\n")
                modified += 1

        print(f"\nMarkdown files cleaned: {modified}")

    def do_scan_and_load():
        includes = scan_markdown_for_includes(content_root)

        config_path = repo_root / "tools" / "hugo_preprocessor.toml"
        snippet_paths = load_snippet_paths(config_path, repo_root)
        snippet_paths = [p.resolve() for p in snippet_paths if p.exists()]
        c_snippets = scan_files_for_snippets(snippet_paths)

        errors = check_includes_against_snippets(includes, c_snippets)
        if errors > 0:
            print(f"\n{errors} error(s) generated.")
            raise SystemExit(1)

        return includes, c_snippets

    def do_replace(includes, c_snippets):
        modified = 0
        seen = set()
        for inc in includes:
            md = inc["md_file"]
            if md in seen:
                continue
            seen.add(md)
            if replace_includes_in_markdown(md, c_snippets):
                modified += 1

        print(f"\nMarkdown files updated: {modified}")

    # ---------- dispatch ----------
    if args.command is None:
        # Default: clean -> scan -> replace
        do_clean()
        includes, c_snippets = do_scan_and_load()
        do_replace(includes, c_snippets)
        return

    if args.command == "clean":
        do_clean()
        return

    if args.command == "scan":
        includes, c_snippets = do_scan_and_load()
        print(f"\nIncludes found: {len(includes)}")
        print(f"Snippet files indexed: {len(c_snippets)}")
        return

    if args.command == "replace":
        includes, c_snippets = do_scan_and_load()
        do_replace(includes, c_snippets)
        return


if __name__ == "__main__":
    main()
