---
title: "Roadmap"
author: "Benoit Le Callennec"
date: 2026-03-03
tags : ["C++", "Roadmap"]
draft: true
---

{{< details 1242.2-Langage_CPP-roadmap >}}
**`main.cpp`**

```cpp
class BankAccount
{
public:
  BankAccount() = default;
  BankAccount(const BankAccount &other) = default;
  virtual ~BankAccount() = default;

  void deposit(double amount);
  void withdraw(double amount);
  void show() const;

private:
  double m_balance{0.0};
};
```
{{</details>}}

{{< plantuml id="roadmap">}}
@startmindmap

<style>
mindmapDiagram {
  .debutant {
    BackgroundColor #c8e6c9
    FontColor #1b5e20
  }
  .intermediaire {
    BackgroundColor #fff9c4
    FontColor #f57f17
  }
  .avance {
    BackgroundColor #ffccbc
    FontColor #bf360c
  }
  .tres_avance {
    BackgroundColor #e1bee7
    FontColor #4a148c
  }
  node {
    FontName Arial
    FontSize 13
    RoundCorner 12
    Padding 8
  }
  :depth(1) {
    FontSize 14
    FontStyle bold
    BackgroundColor #eceff1
    FontColor #37474f
  }
  :depth(0) {
    FontSize 20
    FontStyle bold
    BackgroundColor #0d1b2a
    FontColor white
    RoundCorner 20
  }
}
</style>

* C++

+ Syntaxe de base
++ Types primitifs, variables, constantes <<debutant>>
++ Opérateurs arithmétiques & logiques <<debutant>>
++ Structures de contrôle (if, for, while, switch) <<debutant>>
++ Fonctions : paramètres, retour, surcharge <<debutant>>
++ Tableaux, pointeurs, références <<debutant>>

+ Classes & objets
++ Classes & objets, accesseurs <<debutant>>
++ Constructeurs / destructeurs <<debutant>>
++ Encapsulation, héritage simple <<debutant>>

+ Mémoire de base
++ Stack vs Heap, new / delete <<debutant>>
++ Fuites mémoire, valgrind basique <<debutant>>

+ STL de base
++ Conteneurs séquentiels : vector, list, deque <<debutant>>
++ Conteneurs associatifs : map, set, unordered_map <<debutant>>
++ Itérateurs & algorithmes de base <<debutant>>

+ Outils de base
++ Compilation : g++, clang++, flags -Wall -O2 <<debutant>>
++ Débogage : gdb / lldb basique <<debutant>>
++ CMake (bases) <<debutant>>

+ Langage approfondi
++ Portée, durée de vie, namespaces <<intermediaire>>
++ Passage par valeur / référence / pointeur <<intermediaire>>
++ Fonctions inline, default args <<intermediaire>>
++ auto & decltype <<intermediaire>>

+ POO & polymorphisme
++ Polymorphisme, fonctions virtuelles <<intermediaire>>
++ Héritage multiple & virtual base <<intermediaire>>
++ Opérateurs de copie / déplacement (Rule of 5) <<intermediaire>>
++ Classes abstraites & interfaces <<intermediaire>>
++ RTTI, dynamic_cast <<intermediaire>>

+ Gestion mémoire
++ Smart pointers : unique_ptr, shared_ptr, weak_ptr <<intermediaire>>
++ RAII (Resource Acquisition Is Initialization) <<intermediaire>>
++ Move semantics & rvalue references <<intermediaire>>

+ Templates (bases)
++ Fonctions & classes templates <<intermediaire>>
++ Spécialisation partielle / totale <<intermediaire>>
++ Variadic templates (bases) <<intermediaire>>

+ STL & algorithmes
++ Algorithmes STL (sort, find_if, transform...) <<intermediaire>>
++ Adaptateurs : stack, queue, priority_queue <<intermediaire>>
++ std::string, string_view (C++17) <<intermediaire>>

+ Concurrence (bases)
++ std::thread, std::mutex, std::lock_guard <<intermediaire>>
++ std::async, std::future, std::promise <<intermediaire>>

+ Qualité & outils
++ Sanitizers (ASan, UBSan, TSan) <<intermediaire>>
++ Profiling : perf, gprof, Valgrind <<intermediaire>>
++ Tests unitaires : Catch2, Google Test <<intermediaire>>

+ POO avancée
++ CRTP (Curiously Recurring Template Pattern) <<avance>>
++ Mixin & policy-based design <<avance>>
++ Object slicing, vtables en détail <<avance>>

+ Mémoire & performance
++ Allocateurs personnalisés <<avance>>
++ Memory pools & arenas <<avance>>
++ Placement new, alignement mémoire <<avance>>

+ Templates avancés
++ SFINAE & enable_if <<avance>>
++ Concepts (C++20) <<avance>>
++ Template template parameters <<avance>>
++ Fold expressions <<avance>>

+ Métaprogrammation
++ Type traits (std::is_integral, etc.) <<avance>>
++ constexpr & consteval (C++20) <<avance>>
++ if constexpr <<avance>>
++ std::conditional, std::enable_if <<avance>>

+ STL moderne
++ Ranges & vues (C++20) <<avance>>
++ std::span, std::variant, std::optional <<avance>>
++ Personnalisation des comparateurs & hashers <<avance>>

+ Concurrence avancée
++ Modèle mémoire C++11 (happens-before) <<avance>>
++ std::atomic & opérations atomiques <<avance>>
++ Condition variables, barrières (C++20) <<avance>>

+ Optimisation & analyse
++ CppCoreGuidelines & clang-tidy <<avance>>
++ Optimisations : inlining, cache locality <<avance>>
++ Benchmarking : Google Benchmark <<avance>>
++ Analyse statique : cppcheck, PVS-Studio <<avance>>

+ Templates & expressions
++ Expression templates <<tres_avance>>
++ Policy-based design avancé <<tres_avance>>
++ Barton-Nackman trick <<tres_avance>>

+ Métaprogrammation profonde
++ TMP (Template Metaprogramming) pur <<tres_avance>>
++ Listes de types (typelists) <<tres_avance>>
++ Génération de code à la compilation <<tres_avance>>
++ Réflexion statique (C++26 preview) <<tres_avance>>

+ Concurrence experte
++ Lock-free programming <<tres_avance>>
++ Memory ordering (acquire/release/seq_cst) <<tres_avance>>
++ Coroutines (C++20) <<tres_avance>>

@endmindmap
{{< /plantuml >}}
