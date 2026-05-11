---
title: "9. Bibliothèque standard"
type: docs
weight: 10
---

# Chapitre 9 : bibliothèque standard

## Slides

{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/09_Bibliotheque_standard.html">}}
  
[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/09_Bibliotheque_standard.html?print-pdf)

## Exemples

### Fichiers (I/O)

{{<details "1242.2_09.01_FileTextBasics" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.01_FileTextBasics_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <fstream>
#include <print>
#include <string>

int main()
{
    // 1. Create and write
    std::ofstream fOut("myFile.txt");
    fOut << "PI= " << 3.14159 << "." << '\n';
    fOut.close();

    // 2. Reopen and read — formatted extraction splits on whitespace
    std::ifstream fIn("myFile.txt");
    std::string s;
    double d{};
    char c{};
    fIn >> s >> d >> c;
    fIn.close();

    std::println("{}|{}|{}", s, d, c);
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.02_BinaryFileWrite" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.02_BinaryFileWrite_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Unformatted write into a binary file (RAW, byte by byte).

#include <fstream>
#include <print>

int main()
{
    int a = 1;
    int t1[] = {100, 101, 102, 103, 104, 105};
    double b = 9.87;
    char c = 'W';

    std::ofstream f("toto.xyz", std::ios::out | std::ios::binary);
    if (!f.is_open())
    {
        std::println("Cannot open file for writing!");
        return -1;
    }

    // write() expects a char* — integers and doubles must be reinterpret_cast'd
    f.write(reinterpret_cast<char*>(&a), sizeof(int));
    f.write(reinterpret_cast<char*>(&b), sizeof(double));
    f.write(reinterpret_cast<char*>(&c), sizeof(char));

    for (unsigned int i = 0; i < sizeof(t1) / sizeof(int); i++)
    {
        f.write(reinterpret_cast<char*>(&t1[i]), sizeof(int));
    }

    f.seekp(0, std::ios::end);
    auto size = f.tellp();
    std::println("File size: {} bytes", static_cast<long long>(size));

    f.close();
    std::println("Done");
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.03_BinaryFileRead" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.03_BinaryFileRead_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Unformatted read from a binary file (RAW, byte by byte).
// The reader must know the exact order and type of the stored values.
// Real-world binary formats usually start with a header describing a version
// and layout — swapping two read() calls below would scramble every value.

#include <fstream>
#include <print>

int main()
{
    int a{};
    int t1[6]{};
    double b{};
    char c{};

    std::ifstream f("toto.xyz", std::ios::in | std::ios::binary);
    if (!f.is_open())
    {
        std::println("Cannot open file for reading!");
        return -1;
    }

    // Order matters — must match the writer
    f.read(reinterpret_cast<char*>(&a), sizeof(int));
    f.read(reinterpret_cast<char*>(&b), sizeof(double));
    f.read(reinterpret_cast<char*>(&c), sizeof(char));
    for (int i = 0; i < 6; i++)
    {
        f.read(reinterpret_cast<char*>(&t1[i]), sizeof(int));
    }

    f.seekg(0, std::ios::end);
    auto size = f.tellg();
    std::println("File size: {}", static_cast<long long>(size));

    f.close();

    std::println("a={}", a);
    std::println("b={}", b);
    std::println("c={}", c);
    for (int i = 0; i < 6; i++)
    {
        std::println("{}", t1[i]);
    }
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.04_FormattedFileWrite" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.04_FormattedFileWrite_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Formatted write into a file using operator<<.
//
// Note on text vs binary mode under Windows:
// in text mode, ofstream silently inserts a '\r' before every '\n' it writes
// (and ifstream strips them on read). The resulting file on disk can be
// larger than the bytes you actually wrote. Pass std::ios::binary to disable
// this translation and get exactly what you write.

#include <fstream>
#include <print>

int main()
{
    int a = 78;
    int t1[6];
    double b = 9.87;
    char c = 'W';

    for (int i = 0; i < 6; i++)
    {
        t1[i] = 10000 + i;
    }

    std::ofstream f("toto2.xyz", std::ios::out | std::ios::binary);
    if (!f.is_open())
    {
        std::println("Cannot open file for writing!");
        return -1;
    }

    f << a << '\n';
    f << b << '\n';
    f << c << '\n';
    for (int i = 0; i < 6; i++)
    {
        f << t1[i] << '\n';
    }

    f.seekp(0, std::ios::end);
    auto size = f.tellp();
    std::println("File size: {}", static_cast<long long>(size));

    f.close();
    std::println("Done");
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.05_FormattedFileRead" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.05_FormattedFileRead_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Formatted read from a file using operator>>.

#include <fstream>
#include <print>

int main()
{
    int a{};
    int t1[6]{};
    double b{};
    char c{};

    std::ifstream f("toto2.xyz", std::ios::in | std::ios::binary);
    if (!f.is_open())
    {
        std::println("Cannot open file for reading!");
        return -1;
    }

    f >> a;
    f >> b;
    f >> c;
    for (int i = 0; i < 6; i++)
    {
        f >> t1[i];
    }

    f.seekg(0, std::ios::end);
    auto size = f.tellg();
    std::println("File size: {}", static_cast<long long>(size));

    f.close();

    std::println("a={}", a);
    std::println("b={}", b);
    std::println("c={}", c);
    for (int i = 0; i < 6; i++)
    {
        std::println("{}", t1[i]);
    }
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.06_FileCopy" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.06_FileCopy_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Copy a file byte by byte using read()/write() and a dynamically allocated
// buffer sized from the source file.

#include <fstream>
#include <print>

int main()
{
    std::ifstream infile("test.dat", std::ios::binary);
    if (!infile)
    {
        std::println("File not found!");
        return 1;
    }

    std::ofstream outfile("copy.dat", std::ios::binary);
    if (!outfile)
    {
        std::println("Cannot open output file!");
        return 1;
    }

    // Get size of input file
    infile.seekg(0, std::ios::end);
    auto size = infile.tellg();
    infile.seekg(0, std::ios::beg);

    // Allocate a buffer that matches the source size
    char* buffer = new char[static_cast<size_t>(size)];

    infile.read(buffer, size);
    outfile.write(buffer, size);

    delete[] buffer;
    buffer = nullptr;

    outfile.close();
    infile.close();

    std::println("Copied file size: {}", static_cast<long long>(size));
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### std::string

{{<details "1242.2_09.07_StringOperations" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.07_StringOperations_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// std::string basics: concatenation, size, indexed access, find/rfind,
// substr and its out_of_range exception on negative indices.

#include <iostream>
#include <limits>
#include <print>
#include <stdexcept>
#include <string>

int main()
{
    std::string s1, s2, s3;

    std::print("Enter a first string (no spaces): ");
    std::cin >> s1;
    std::print("Enter a second string (no spaces): ");
    std::cin >> s2;

    s3 = s1 + s2;
    std::println("Concatenation of the two strings:");
    std::println("{}", s3);

    auto size = s3.size();
    std::println("The string has {} characters.", size);

    for (size_t i = 0; i < size; i++)
    {
        std::println("character {} = {}", i, s3[i]);
    }
    std::println("capacities: {} {} {}", s1.capacity(), s2.capacity(), s3.capacity());

    // Flush the buffer before switching to getline()
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::print("\nEnter a first string with spaces: ");
    std::getline(std::cin, s1);
    std::print("Enter a second string with spaces: ");
    std::getline(std::cin, s2);
    s3 = s1 + s2;
    std::println("Concatenation of the two strings:");
    std::println("{}", s3);

    std::print("\nWhich substring to search for? ");
    std::string needle;
    std::cin >> needle;

    auto position = s3.find(needle, 0);
    if (position == std::string::npos)
    {
        std::println("The substring '{}' was not found!", needle);
    }
    else
    {
        std::println("The substring '{}' is at position (from left): {}", needle, position);
    }

    position = s3.rfind(needle, std::string::npos);
    if (position == std::string::npos)
    {
        std::println("The substring '{}' was not found!", needle);
    }
    else
    {
        std::println("The substring '{}' is at position (from right): {}", needle, position);
    }

    s1 = "XXX";
    try
    {
        // If the starting index is out of range, substr throws out_of_range.
        // If the requested length extends past the end, substr silently clamps.
        s1 = s3.substr(s3.size() - 3, 3);
    }
    catch (const std::out_of_range&)
    {
        std::println("out_of_range exception");
    }
    std::println("The last three characters of the string are: {}", s1);

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.08_StringStreamConversion" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.08_StringStreamConversion_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Using std::ostringstream / std::istringstream to convert between
// numbers and strings.

#include <print>
#include <sstream>
#include <string>

int main()
{
    double number1 = 10.25;

    // number -> string
    std::println("Conversion number -> string");
    std::ostringstream oss;
    oss << number1;

    std::string result = oss.str();
    std::println("Number as string: {}", result);
    std::println("String length: {}", result.length());

    // string -> number
    std::println("\nConversion string -> number");
    std::string numberAsString = "12.34";
    std::istringstream iss(numberAsString);

    double number2{};
    iss >> number2;
    std::println("Second number: {}", number2);

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Conteneurs séquentiels

{{<details "1242.2_09.09_ListIterator" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.09_ListIterator_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// std::list is a doubly-linked list: traverse it from begin() or from end(),
// or use reverse_iterator via rbegin()/rend().

#include <list>
#include <print>

int main()
{
    std::list<int> numbers;
    for (int i = 0; i < 10; i++)
    {
        numbers.push_back(10 * i);
    }

    std::print("List from the beginning:");
    for (auto it = numbers.begin(); it != numbers.end(); it++)
    {
        std::print(" {}", *it);
    }
    std::println("");

    // Traverse backwards using a forward iterator.
    // end() points one past the last element, so we decrement BEFORE dereferencing.
    std::print("\nList from the end:");
    for (auto it = numbers.end(); it != numbers.begin();)
    {
        it--;
        std::print(" {}", *it);
    }
    std::println("");

    // Same traversal with reverse_iterator — cleaner.
    std::print("\nList from the end (reverse_iterator):");
    for (auto rit = numbers.rbegin(); rit != numbers.rend(); ++rit)
    {
        std::print(" {}", *rit);
    }
    std::println("");

    // Insert 111 between the first (0) and second (10) elements
    auto it = numbers.begin();
    it++;
    numbers.insert(it, 111);

    std::print("\nList from the beginning (with one extra element):");
    for (auto iter = numbers.begin(); iter != numbers.end(); iter++)
    {
        std::print(" {}", *iter);
    }
    std::println("");

    // std::list does NOT support direct index access (no operator[] or at()).
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.10_ListPushInsertPop" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.10_ListPushInsertPop_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// std::list: push_back / push_front / insert / pop_front.
// Shows the two common traversal styles: range-based for vs explicit iterator.

#include <list>
#include <print>

void printList(const std::list<int>& list)
{
    std::print("range-based for: ");
    for (const int& value : list)
    {
        std::print("{} ", value);
    }
    std::println("");
}

void printListIterator(const std::list<int>& list)
{
    std::print("explicit iterator: ");
    for (auto iter = list.begin(); iter != list.end(); iter++)
    {
        std::print("{} ", *iter);
    }
    std::println("");
}

int main()
{
    std::list<int> lst;
    printList(lst);

    lst.push_back(1);
    printList(lst);

    lst.push_front(0);
    printList(lst);

    lst.insert(lst.begin(), 2);
    printList(lst);

    lst.insert(--lst.end(), 3);
    printList(lst);

    lst.pop_front();
    printList(lst);

    printListIterator(lst);
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.11_VectorOperations" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.11_VectorOperations_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Tour of the std::vector API: push_back, front/back, pop_back, empty,
// resize, reserve, capacity, sort, fill, accumulate, at() bounds checking,
// reverse iteration, assignment, equality.

#include <algorithm>
#include <numeric>
#include <print>
#include <stdexcept>
#include <vector>

int main()
{
    std::println("---> std::vector<int> v; // empty integer vector");
    std::vector<int> v;

    std::println("---> v.push_back(1000); // append 1000");
    v.push_back(1000);

    std::println("v.front() = {}", v.front());
    std::println("v.back()  = {}", v.back());

    std::println("---> v.pop_back();");
    v.pop_back();

    if (v.empty())
    {
        std::println("v.empty(): vector is empty");
    }

    std::println("\n---> v.resize(10); // new ints default-initialized to 0");
    v.resize(10);
    std::println("v.size() = {}", v.size());

    // size is 10 — direct indexing up to index 9 is valid
    v[9] = 5000;
    std::println("v[9] = {}", v[9]);

    std::fill(v.begin(), v.end(), 100);

    v.clear();

    // reserve() allocates capacity up front so push_back() avoids reallocations
    v.reserve(50);
    std::println("\nAfter reserve(50):");
    std::println("v.size()     = {}", v.size());
    std::println("v.capacity() = {}", v.capacity());

    for (int i = 0; i < 50; ++i)
    {
        v.push_back(i);
    }
    std::println("After 50 push_back: v.size() = {}", v.size());
    std::println("max_element = {}", *std::max_element(v.begin(), v.end()));

    v.resize(5);
    std::sort(v.begin(), v.end());

    std::print("Sorted vector via v[i]:");
    for (size_t i = 0, size = v.size(); i < size; ++i)
    {
        std::print(" {}", v[i]);
    }
    std::println("");

    // operator[] does NOT check bounds — out-of-range access is undefined behavior.
    // at() throws std::out_of_range instead.
    try
    {
        v.at(static_cast<size_t>(-1)) = 10;
    }
    catch (const std::out_of_range&)
    {
        std::println("at() threw std::out_of_range");
    }

    std::print("Reverse iteration:");
    for (auto it = v.rbegin(); it != v.rend(); ++it)
    {
        std::print(" {}", *it);
    }
    std::println("");

    std::vector<int> v2(10);
    v2.at(9) = 5;
    std::vector<int> v3(10, 20); // 10 elements initialized to 20

    std::println("\nsum of v3 = {}", std::accumulate(v3.begin(), v3.end(), 0));

    v = v3;
    if (std::equal(v.begin(), v.end(), v3.begin()))
    {
        std::println("equal: v is a copy of v3");
    }
    else
    {
        std::println("equal: v and v3 differ!");
    }
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.12_ListOfPointersCleanup" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.12_ListOfPointersCleanup_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// A std::list<int*> owns raw pointers — clear() only destroys the list nodes,
// it does NOT delete what they point to. The owner must free each pointer
// FIRST, then clear the list (or let it go out of scope).

#include <algorithm>
#include <list>
#include <print>

int main()
{
    std::list<int*> l;
    l.push_back(new int(5));
    l.push_back(new int(0));
    l.push_back(new int(1));
    l.push_back(new int(6));

    std::println("\nList content (address : value):");
    for (auto it = l.begin(); it != l.end(); it++)
    {
        std::println(" {} : {}", static_cast<void*>(*it), **it);
    }

    // Solution 1: explicit loop
    for (auto it = l.begin(); it != l.end(); it++)
    {
        delete *it;
        *it = nullptr;
    }

    // Solution 2 (equivalent): std::for_each with a lambda
    // std::for_each(l.begin(), l.end(), [](int*& p) { delete p; p = nullptr; });

    // The nodes still exist — only the pointed-to ints were freed.
    std::println("\nAfter delete (addresses now dangling / nullptr):");
    for (auto it = l.begin(); it != l.end(); it++)
    {
        std::println(" {}", static_cast<void*>(*it));
    }

    l.clear();
    std::println("\nAfter l.clear(): size = {}", l.size());
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Conteneurs associatifs

{{<details "1242.2_09.13_Map" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.13_Map_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// std::map basics: insert via operator[], iterate, find(),
// and the operator[] trap: accessing a missing key SILENTLY INSERTS an
// empty entry, growing the map.

#include <map>
#include <print>
#include <string>

int main()
{
    std::map<std::string, double> grades;

    grades["Computer Science"] = 5.5;
    grades["Physics"] = 4.5;
    grades["History of Math"] = 2.5;
    grades["Analysis"] = 4.0;
    grades["Algebra"] = 5.5;
    grades["C++"] = 6;

    for (auto it = grades.begin(); it != grades.end(); ++it)
    {
        std::println("In {}, my grade is {}.", it->first, it->second);
    }

    std::println("\ngrades[\"Physics\"] = 5.5;");
    grades["Physics"] = 5.5;

    std::println("\nAfter updating an existing key:");
    for (auto it = grades.begin(); it != grades.end(); ++it)
    {
        std::println("In {}, my grade is {}.", it->first, it->second);
    }

    std::println("\nfind(\"Computer Science\")->second = {}",
                 grades.find("Computer Science")->second);

    auto it = grades.find("Communication");
    if (it == grades.end())
    {
        std::println("find(\"Communication\"): key not found");
    }
    else
    {
        std::println("grade in Communication: {}", it->second);
    }

    // operator[] on a missing key creates a new default-initialized entry
    // and increases the map's size.
    std::println("\noperator[] on existing key 'Computer Science': {}",
                 grades["Computer Science"]);
    std::println("operator[] on missing  key 'ComputerXScience' : {} (silently inserted!)",
                 grades["ComputerXScience"]);

    std::println("\nFinal map:");
    for (auto it2 = grades.begin(); it2 != grades.end(); ++it2)
    {
        std::println("In {}, my grade is {}.", it2->first, it2->second);
    }
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.14_Multimap" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.14_Multimap_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// std::multimap allows duplicate keys — so operator[] does NOT exist
// (which value would it return?). Entries are inserted via insert(),
// and all values for a given key are retrieved via lower_bound/upper_bound
// or equal_range.

#include <map>
#include <print>
#include <string>

int main()
{
    std::multimap<std::string, double> grades;

    grades.insert({"Computer Science", 5.5});
    grades.insert({"Physics", 4.5});
    grades.insert({"History of Math", 2.5});
    grades.insert({"Analysis", 4.0});
    grades.insert({"Algebra", 5.5});
    grades.insert({"XXX", 4});

    for (auto it = grades.begin(); it != grades.end(); ++it)
    {
        std::println("In {}, grade {}", it->first, it->second);
    }

    // Adding several entries with the same key — none overwrite each other
    grades.insert({"Physics", 5.5});
    grades.insert({"Computer Science", 5.5});
    grades.insert({"Physics", 3.5});

    std::println("\nAfter adding duplicate keys:");
    for (auto it = grades.begin(); it != grades.end(); ++it)
    {
        std::println("In {}, grade {}", it->first, it->second);
    }

    // find() returns ONE of the matching entries — not necessarily the one you want
    std::println("\nfind(\"Physics\")->second = {}", grades.find("Physics")->second);

    // lower_bound / upper_bound: iterate over every value sharing a key
    std::string key = "Computer Science";
    auto itLow = grades.lower_bound(key);
    auto itUp = grades.upper_bound(key);
    std::print("\nlower_bound/upper_bound for '{}':", key);
    for (auto it = itLow; it != itUp; it++)
    {
        std::print(" {}", it->second);
    }
    std::println("");

    // equal_range: same result, packaged as a pair
    auto range = grades.equal_range(key);
    std::print("equal_range for '{}'        :", key);
    for (auto it = range.first; it != range.second; ++it)
    {
        std::print(" {}", it->second);
    }
    std::println("");
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Smart pointers

{{<details "1242.2_09.15_SharedPointer" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.15_SharedPointer_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// std::shared_ptr: shared ownership via reference counting. An object is
// destroyed the moment the last shared_ptr pointing to it is reassigned
// or goes out of scope.

#include <memory>
#include <print>

class Triangle
{
public:
    Triangle(double base, double height)
        : m_base(base), m_height(height) {}

    ~Triangle()
    {
        std::println("destroying Triangle({}, {})", m_base, m_height);
    }

    double getBase() const { return m_base; }
    double getHeight() const { return m_height; }

private:
    double m_base{0};
    double m_height{0};
};

int main()
{
    auto sp0 = std::make_shared<Triangle>(12, 3.44567);

    std::shared_ptr<Triangle> sp1, sp2;
    // sp1 = new Triangle(2, 1.5); // NOT allowed: no implicit raw->shared
    sp1.reset(new Triangle(2, 1.5));
    sp2 = sp1;
    std::println("sp0={} sp1={} sp2={}",
                 static_cast<void*>(sp0.get()),
                 static_cast<void*>(sp1.get()),
                 static_cast<void*>(sp2.get()));

    sp2 = sp0;
    std::println("sp0={} sp1={} sp2={}",
                 static_cast<void*>(sp0.get()),
                 static_cast<void*>(sp1.get()),
                 static_cast<void*>(sp2.get()));

    // The second Triangle (2, 1.5) now has zero owners and is destroyed
    sp1 = sp0;
    std::println("sp0={} sp1={} sp2={}",
                 static_cast<void*>(sp0.get()),
                 static_cast<void*>(sp1.get()),
                 static_cast<void*>(sp2.get()));
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_09.16_UniquePointer" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.16_UniquePointer_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// std::unique_ptr: exclusive ownership. A unique_ptr CANNOT be copied,
// only moved — so it must be passed by reference to functions that don't
// take ownership. Mixing raw pointers and smart pointers is dangerous:
// if two smart pointers end up owning the same raw pointer, both will
// try to delete it (double-free → crash).

#include <memory>
#include <print>

class X
{
public:
    explicit X(int x = 10) : m_x(x) {}

    ~X()
    {
        std::println("Destroying X(m_x={})", m_x);
    }

    int getValue() const { return m_x; }

private:
    int m_x{10};
};

// unique_ptr must be passed by reference — no copy is allowed
void show(const std::unique_ptr<X>& obj)
{
    std::println("show: {}", obj->getValue());
}

int main()
{
    {
        std::unique_ptr<X> uniq(new X(1));
        std::println("main: {}", uniq->getValue());
        show(uniq);

        // std::unique_ptr<X> uniq2(uniq);  // ERROR: copy constructor is deleted
        // std::unique_ptr<X> uniq3 = uniq; // ERROR: copy assignment is deleted

        uniq.reset(new X(2)); // destroys the X(1) currently owned
    } // destroys the X(2) owned by uniq

    // WARNING: mixing raw pointers with unique_ptr is unsafe.
    // Two unique_ptr owning the same raw pointer → double delete at scope exit.
    {
        X* ptx = new X(3);
        std::unique_ptr<X> uniq(ptx);
        std::println("{}", uniq->getValue());
        std::unique_ptr<X> uniq2(ptx); // compiles, but will crash at scope exit
        std::println(" I'm here!");
    }
    std::println("I will never get here with a broken program...");
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Threads

{{<details "1242.2_09.17_ThreadBasics" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_09.17_ThreadBasics_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Basic std::thread usage. Two threads each print a character repeatedly.
// Because both threads share stdout without synchronization, the output
// typically shows interleaved runs like "AAAABBBBBAAAAABBBB", each thread
// getting a slice of CPU time.
//
// Note: std::cout is used here (not std::println) to keep each character
// write minimal and maximize visible interleaving.

#include <iostream>
#include <thread>

constexpr int SIZE = 500;

void taskA()
{
    for (int i = 0; i < SIZE; i++)
    {
        std::cout << "A";
    }
}

void taskB()
{
    for (int i = 0; i < SIZE; i++)
    {
        std::cout << "B";
    }
}

int main()
{
    std::cout << "Two threads (A and B) will start\n";

    std::thread first(taskA);
    std::thread second(taskB);

    first.join();
    std::cout << "\nFIRST THREAD DONE\n";
    second.join();
    std::cout << "SECOND THREAD DONE\n";
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 9.1

### Exercice 1 : écriture binaire
Écrire un programme qui enregistre (sous forme binaire, et non pas formatée), dans un fichier dont le nom est fourni par l'utilisateur, une suite de nombres entiers fournis sur l’entrée standard.
On conviendra que l’utilisateur fournira la valeur 0 (qui ne sera pas enregistrée dans le fichier) pour préciser qu’il a terminé.

Dans un deuxième temps, on fera les tests suivants :
- si le fichier existe déjà, on fera une demande de confirmation
- dans la lecture des entiers, on veillera à surveiller que l’utilisateur n’entre que des entiers.

### Exercice 2 : lecture binaire
Écrire un programme permettant de lister (sur la sortie standard) les entiers contenus dans le fichier tel que celui créé par l’exercice précédent.

### Exercice 3 : rang
Écrire un programme permettant à un utilisateur de retrouver, dans un fichier tel que celui créé dans l'exercice 1, les entiers dont il fournit le « _rang_ » (sa position).
On conviendra qu’un rang égal à 0 signifie que l'utilisateur souhaite mettre fin au programme.

### Exercice 4 : lecture formatée
Écrire un programme qui ouvre un fichier texte dont le nom est donné par l’utilisateur et qui affiche le contenu sur la console en numérotant les lignes.

{{<a_noter>}}
La méthode **`ignore`** vide le contenu pouvant être dans le flux du nombre de caractères **`n`** spécifié, soit jusqu'à ce que le caractère spécifié **`delim`** soit rencontré.

**`istream &ignore(int n=1, int delim=eof() );`**

**Exemple**

**`cin.ignore( numeric_limits<streamsize>::max(), '\n' );`**
  
Pour les autres méthodes utiles pour la lecture / écriture avec un fichier en C++, se référer à la documentation de [**`std::istream`**](https://en.cppreference.com/w/cpp/io/basic_istream) et [**`std::ostream`**](https://en.cppreference.com/w/cpp/io/basic_ostream).
{{</a_noter>}}

## Série 9.2

### Exercice 1 : **`std::vector`**
Pour utiliser le type **`std::vector`**, il faut inclure la bibliothèque qui définit ce type avec la directive suivante :

**`#include <vector>`**

Soient les déclarations suivantes:

**`using MyArray = std::vector<int>;`**

**`MyArray tab1, tab2;`**

En vous aidant d'un  programme, répondez aux questions suivantes.

#### A. Quelles valeurs contiendra **`tab1`**, après l'exécution de la boucle suivante ?
```cpp
for (auto i = 0; i < 10; ++i)
  tab1.push_back(tab1.size());
```

#### B. Que fait la fonction suivante ?
```cpp
void foo(MyArray& tab1, MyArray& tab2)
{
    for (std::size_t i = 0; i < tab1.size(); i++)
    {
        tab2.push_back(tab1.front());
    }
}
```

#### C. Que se passe-t-il lorsqu'on ajoute "trop" d'éléments à un vecteur ?

Faire un programme pour mettre en évidence le mécanisme utilisé par **`std::vector`** pour résoudre le problème.

#### D. Que se passe-t-il si on écrit **`tab1[i] = 3;`** avec **`i`** ≥ **`tab1.size()`** ?

#### E. Que se passe-t-il si on écrit **`tab1.at(i) = 3;`** avec **`i`** ≥ **`tab1.size()`** ?

#### F. Initialiser de manière simple un vecteur avec les 8 premiers termes de la suite de Fibonacci (1 1 2 3 5 8 13 21).
Voir [Initialize Vector in C++](https://www.geeksforgeeks.org/initialize-a-vector-in-cpp-different-ways/)

### Exercice 2 : comportement dynamique de `vector`
Quel est l'affichage du programme suivant ? Expliquer le résultat.

```cpp
// comparing size, capacity and max_size
#include <print>
#include <vector>

int main()
{
  std::vector<int> myvector;

  // set some content in the vector:
  for (auto i = 0; i < 100; ++i) 
     myvector.push_back(i);

  std::println("size: {}", myvector.size());
  std::println("capacity: {}", myvector.capacity());
  std::println("max_size: {}", myvector.max_size());

  return 0;
}
```

- Recopier le code
- Ajouter le maximum d’éléments. Est-ce le comportement attendu ?
- Compléter le programme avec deux façons d’afficher le contenu du vecteur
  - Avec un itérateur
  - Avec un ***range based for loop***

## Série 9.3

### Exercice 1 : performance des opérations avec `std::vector` et `std::list`
En utilisant les déclarations suivantes :

```cpp
using myArray = std::vector<int>;
using myList = std::list<int>;
```

On demande d'écrire un programme capable de tester l'efficacité des tâches ci-dessous :

1. Insertion de 100'000'000 éléments à la fin d'un `std::vector`
2. Insertion de 100'000'000 éléments à la fin d'un `std::vector` (en utilisant `reserve`)
3. Insertion de     500'000 éléments au début d'un `std::vector` (en utilisant `insert`)
4. Insertion de     500'000 éléments au début d'un `std::vector` (en utilisant `reserve`)
5. Insertion de     500'000 éléments à la fin d'une `std::list`
6. Insertion de     500'000 éléments au début d'une `std::list`
7. Insertion de     500'000 éléments au début d'une `std::forward_list`
8. Insertion de      50'000 éléments à la FIN d'une `std::forward_list` (traverser la liste pour ajouter à la fin)

{{<a_noter>}}
Les tailles utilisées sont différentes car certaines opérations peuvent prendre beaucoup plus de temps que d'autres.
{{</a_noter>}}

Pour mesurer le temps, vous pouvez utiliser les fonctions de <chrono> :

```cpp
#include <chrono>
...
auto start = std::chrono::high_resolution_clock::now();

// Function to profile here

auto stop = std::chrono::high_resolution_clock::now();
auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
std::println("Time taken: {} milliseconds", duration.count());
```

#### Quelles sont vos conclusions par rapport aux écarts de performances ? Pourquoi ?

## Série 9.4

### Exercice 1 : conteneurs associatifs et template
Écrire un programme qui utilise un tableau associatif permettant de manipuler des paires (pays / ville).

```console
Suisse  Berne
USA     New York
USA     Washington
USA     Boston

USA===>  | New York | Washington | Boston
```

La clé est le pays et la valeur est la ville.
On voit donc, ici qu'il y a trois entrées avec la clé USA.

On écrira deux modèles de fonctions (templates) pour afficher les résultats.
Si la variable représentant le tableau associatif se nomme *stateMap*, on pourra appeler les fonctions de ce code :

```cpp
showMultimap(stateMap);	        // Display all container content.
std::string s = "USA";
showMultimapRange(stateMap, s);	// Display all values which has a s key.
```
Les deux fonctions doivent être des modèles de fonctions, c'est-à-dire qu'elles doivent fonctionner avec des types de clé et de valeur quelconques.
On demande d'utiliser le [structured binding](https://en.cppreference.com/w/cpp/language/structured_binding) dans l'implémentation de ces fonctions.

<div style="page-break-after: always;"></div>

### Exercice 2 : conteneurs associatifs et algorithmes

Écrire un programme qui lit un fichier de texte donné en paramètre (qui contient des citations de Steve Jobs), complètement, mot par mot. 
Le programme créera une table associative (dictionnaire clé-valeur) avec comme clés les mots, et comme valeur le nombre d’occurrences. 
À la fin de l’exécution, le programme affichera le nombre total de mots contenu dans le texte, le nombre de mots différents, ainsi que le nombre d’occurrences de chaque mot triés du plus grand nombre d'occurences au plus petit, puis par ordre alphabétique en second tri.

**Indication** : l'implémentation du tri multiple nécessite de passer d'un container associatif à un autre type. Utiliser la méthode **`sort()`** accompagnée d'une méthode de comparaison personnalisée.

<table>
<thead>
    <tr>
    <th style="text-align:left;"> Exemple:  </th>
    <th style="text-align:right;"> jobs.txt </th>
    </tr>
</thead>
<tbody>
    <tr>
    <td style="text-align:left;background-color: rgb(50, 50, 50);width:40%;color:white;"> 
    <span style="color:blue">program </span> <span style="color:yellow">jobs.txt</span>
    <br>The file contains 51 words
    <br>Occurence count: 42       
    <br>4x "the"
    <br>3x "you"
    <br>2x "Stay"
    <bt>2x "things"
    <br>2x "to"
    <br>2x "your"
    <br>1x "Dont"
    <br>...
    <td style="text-align:right;background-color: rgb(200, 200, 100);width:60%;color:black;">
    Don’t let the noise of others’ opinions drown out your own inner voice.
    Have the courage to follow your heart and intuition. 
    They somehow already know what you truly want to become...
    </td>
    </tr>
</tbody>
</table>

On demande d'utiliser le [structured binding](https://en.cppreference.com/w/cpp/language/structured_binding) dès que possible.

Cours de C++, 1ère année, HE-Arc
## Série 9.5 : smart pointers

### Exercice 1 : "de natif à smart !"

Reprendre le code source de l'exercice 3 de la série 2.1 qui propose de manipuler des points : 

{{<plantuml id="ex9.5.1" >}}
@startuml

skin rose
skinparam classAttributeIconSize 0
hide circle

class Point
{
  - x : double
  - y : double
  + label : char
  + show() : void
  + translate (double dx, double dy) : void
  + Point (char name, double x, double y)
}
@enduml
{{</plantuml>}}

Réaliser les étapes suivantes : 

- Ajouter un destructeur dans la classe *Point* et tracker les appels au moyen de std::println.
- Modifier le fichier *main.cpp* en utilisant les notions suivantes : 
  - Smart pointers
  - std::make_
  - Containeurs 
  - 'auto' 
  - Free function
  - 'Using' pour la déclaration des types custom
  - ...
