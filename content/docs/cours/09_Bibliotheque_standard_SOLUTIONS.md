---
title: "9. Bibliothèque standard — Solutions"
type: docs
weight: 10
draft: false
---

# Chapitre 9 : bibliothèque standard — Solutions

## Série 9.1

### Exercice 1 : écriture binaire

{{<details "1242.2_09.01_BinaryFileWrite" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.01_BinaryFileWrite_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <fstream>
#include <iostream>
#include <limits>
#include <print>
#include <string>

static bool fileExists(const std::string &name)
{
  std::ifstream f(name);
  return !f.fail();
}

int main()
{
  std::string fileName;
  std::print("File name to create: ");
  std::getline(std::cin, fileName);

  std::ofstream output;
  bool ready = false;
  while (!ready)
  {
    if (fileExists(fileName))
    {
      std::print("File already exists. Overwrite? (y/n)");
      std::string answer;
      std::cin >> answer;
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      if (answer == "y" || answer == "Y")
      {
        output.open(fileName, std::ios::out | std::ios::binary);
        ready = true;
      }
      else
      {
        std::print("New file name: ");
        std::getline(std::cin, fileName);
      }
    }
    else
    {
      output.open(fileName, std::ios::out | std::ios::binary);
      ready = true;
    }
  }

  if (output.fail())
  {
    std::println("Cannot create file");
    return 1;
  }

  int n = 0;
  do
  {
    std::print("Enter an integer (0 to stop): ");
    std::cin >> n;

    if (std::cin.fail())
    {
      std::println("Invalid input");
      std::cin.clear();
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      n = 1; // continue jumps to while(n!=0), possibly with n = 0
    }
    else if (n != 0)
    {
      output.write(reinterpret_cast<const char *>(&n), sizeof(int));
    }
  } while (n != 0 && output);

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 2 : lecture binaire

{{<details "1242.2_09.02_BinaryFileRead" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.02_BinaryFileRead_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <fstream>
#include <iostream>
#include <print>
#include <string>

int main()
{
  std::string fileName;
  std::print("File name to read: ");
  std::cin >> fileName;

  std::ifstream input(fileName, std::ios::in | std::ios::binary);
  if (!input)
  {
    std::println("Cannot open file");
    return 1;
  }

  std::println("\nContent of {}:", fileName);
  int n = 0;
  while (input.read(reinterpret_cast<char *>(&n), sizeof(int)))
  {
    std::println("{}", n);
  }
  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 3 : rang

{{<details "1242.2_09.03_BinaryFileRank" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.03_BinaryFileRank_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <fstream>
#include <iostream>
#include <print>
#include <string>

int main()
{
    std::string fileName;
    std::print("File name: ");
    std::cin >> fileName;

    std::ifstream input(fileName, std::ios::in | std::ios::binary);
    if (!input)
    {
        std::println("Cannot open file");
        return 1;
    }

    int rank = 0;
    do
    {
        std::print("Rank of the integer to read (0 to stop): ");
        std::cin >> rank;
        if (rank > 0)
        {
            input.seekg(sizeof(int) * (rank - 1), std::ios::beg);
            int n = 0;
            if (input.read(reinterpret_cast<char*>(&n), sizeof(int)))
            {
                std::println("-- value: {}", n);
            }
            else
            {
                std::println("-- out of range");
                input.clear();
            }
        }
    } while (rank != 0);

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 4 : lecture formatée

{{<details "1242.2_09.04_TextFileLineNumbers" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.04_TextFileLineNumbers_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <fstream>
#include <iostream>
#include <print>
#include <string>

int main()
{
    std::string fileName;
    std::print("File name: ");
    std::cin >> fileName;

    std::ifstream input(fileName);
    if (!input)
    {
        std::println("Cannot open file");
        return 1;
    }

    std::string line;
    int i = 0;
    // std::getline strips the newline, so we rely on println to add one
    while (std::getline(input, line))
    {
        std::println("{} : {}", ++i, line);
    }

    std::println("***** End of file *****");
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 9.2

### Exercice 1 : **`std::vector`**

{{<details "1242.2_09.05_VectorExplore" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.05_VectorExplore_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <print>
#include <stdexcept>
#include <vector>

using DynIntArray = std::vector<int>;

static void show(const DynIntArray& tab)
{
    for (std::size_t i = 0; i < tab.size(); i++)
    {
        std::print("{}{}", tab[i], (i + 1 < tab.size() ? ", " : ""));
    }
    std::println("");
}

// Question A: value pushed equals the current size → output 0..9
static void questionA()
{
    std::println("Question 1.A:");
    DynIntArray tab1;
    for (int i = 0; i < 10; i++)
    {
        tab1.push_back(static_cast<int>(tab1.size()));
    }
    show(tab1);
}

// Question B: foo() pushes tab1.front() once per element of tab1 into tab2
static void foo(const DynIntArray& tab1, DynIntArray& tab2)
{
    for (std::size_t i = 0; i < tab1.size(); i++)
    {
        tab2.push_back(tab1.front());
    }
}

static void questionB()
{
    std::println("\nQuestion 1.B:");
    DynIntArray tab1{1, 2, 3, 4, 5};
    DynIntArray tab2{-3, -2, -1, 0};
    std::print("tab1: ");
    show(tab1);
    std::print("tab2: ");
    show(tab2);
    foo(tab1, tab2);
    std::print("tab2 after foo(tab1, tab2): ");
    show(tab2);
}

// Question C: max_size() is a theoretical maximum; the OS won't let us
// actually reserve that much memory.
static void questionC()
{
    DynIntArray tab;
    std::println("\nQuestion 1.C:");
    std::println("tab.max_size() : {:e}", static_cast<double>(tab.max_size()));
    std::println("tab.size()     : {}", tab.size());
    std::println("tab.capacity() : {}", tab.capacity());

    std::println("\nTry tab.reserve({:e})", static_cast<double>(tab.max_size() / 8 + 1000));
    try
    {
        tab.reserve(tab.max_size() / 8 + 1000);
    }
    catch (const std::bad_alloc& e)
    {
        std::println("Reservation error: {}", e.what());
    }

    int incSize = 1;
    do
    {
        std::print("Elements to add (0 to stop): ");
        std::cin >> incSize;
        for (int i = 0; i < incSize; i++)
        {
            tab.push_back(incSize);
        }
        std::println("size / capacity = {} / {}", tab.size(), tab.capacity());
    } while (incSize > 0);
}

// Question D: operator[] does NOT bounds-check → undefined behaviour
[[maybe_unused]]
static void questionD()
{
    std::println("\nQuestion 1.D:");
    DynIntArray tab(3, 27);
    show(tab);
    std::println("tab[{}] = {}  (undefined behaviour!)", tab.size(), tab[tab.size()]);
}

// Question E: at() throws std::out_of_range on invalid index
static void questionE()
{
    std::println("\nQuestion 1.E:");
    DynIntArray tab(3, 11);
    show(tab);
    try
    {
        std::println("tab.at(tab.size()) = {}", tab.at(tab.size()));
    }
    catch (const std::out_of_range& e)
    {
        std::println("tab.at() threw out_of_range: {}", e.what());
    }
}

int main()
{
    questionA();
    questionB();
    // questionD(); // UB — enable with caution
    questionE();
    questionC(); // interactive — keep last

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 2 : comportement dynamique de `vector`

{{<details "1242.2_09.06_VectorIteration" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.06_VectorIteration_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <vector>

int main()
{
  std::vector<int> myvector;

  // set some content in the vector:
  for (auto i = 0; i < 100; ++i)
  {
    myvector.push_back(i);
  }

  std::println("size: {}", myvector.size());
  std::println("capacity: {}", myvector.capacity());
  std::println("max_size: {}", myvector.max_size());

  for (int i = 0; i < 20; i++)
  {
    myvector.push_back(i);
  }

  // 1. Explicit iterator type
  for (std::vector<int>::iterator it = myvector.begin(); it != myvector.end(); ++it)
  {
    std::print(" {}", *it);
  }
  std::println("");

  // 2. Implicit iterator type (auto)
  for (auto it = myvector.begin(); it != myvector.end(); ++it)
  {
    std::print(" {}", *it);
  }
  std::println("");

  // 3. Range-based for with const reference
  for (const int &i : myvector)
  {
    std::print(" {}", i);
  }
  std::println("");

  // 4. Range-based for with auto and no copy
  for (const auto &i : myvector)
  {
    std::print(" {}", i);
  }
  std::println("");

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 9.3

### Exercice 1 : performance des opérations avec `std::vector` et `std::list`

{{<details "1242.2_09.07_ContainerPerformance" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.07_ContainerPerformance_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <chrono>
#include <forward_list>
#include <list>
#include <print>
#include <vector>

constexpr std::size_t FEW_ELEMENTS = 50'000;
constexpr std::size_t MANY_ELEMENTS = 500'000;
constexpr std::size_t MANY_MANY_ELEMENTS = 100'000'000;

class Timer
{
public:
  Timer() = default;
  void Start()
  {
    m_start = std::chrono::high_resolution_clock::now();
  }
  void Stop()
  {
    m_stop = std::chrono::high_resolution_clock::now();
  }
  std::chrono::milliseconds ElapsedMs() const
  {
    return std::chrono::duration_cast<std::chrono::milliseconds>(m_stop - m_start);
  }
  std::chrono::nanoseconds ElapsedNsPerInsertion(std::size_t count) const
  {
    if (count == 0)
    {
      throw std::invalid_argument("Count must be positive");
    }
    auto totalNs = std::chrono::duration_cast<std::chrono::nanoseconds>(m_stop - m_start);
    return std::chrono::nanoseconds(totalNs.count() / count);
  }

private:
  std::chrono::high_resolution_clock::time_point m_start;
  std::chrono::high_resolution_clock::time_point m_stop;
};

Timer part1(std::size_t count);
Timer part2(std::size_t count);
Timer part3(std::size_t count);
Timer part4(std::size_t count);
Timer part5(std::size_t count);
Timer part6(std::size_t count);
Timer part7(std::size_t count);
Timer part8(std::size_t count);

int main()
{
  using Fn = Timer (*)(std::size_t);
  Fn methods[] = {part1, part2, part3, part4, part5, part6, part7, part8};
  std::size_t methodsOperations[] = {MANY_MANY_ELEMENTS, MANY_MANY_ELEMENTS, MANY_ELEMENTS, MANY_ELEMENTS, MANY_ELEMENTS, MANY_ELEMENTS, MANY_ELEMENTS, FEW_ELEMENTS};

  int argumentIndex = 0;
  for (auto method : methods)
  {
    auto nbOperations = methodsOperations[argumentIndex++];
    auto timer = method(nbOperations);
    auto elapsedMs = timer.ElapsedMs();
    auto nsPerInsertion = timer.ElapsedNsPerInsertion(nbOperations);
    std::println("   Total insertion time: {:>6} ms", elapsedMs.count());
    std::println("   Time per insertion: {:>6} ns", nsPerInsertion.count());
  }

  std::println("\nNote: push_back at end of vector is fastest (1&2); insert at beginning of vector is VERY slow (3&4);");
  std::println("lists are slower and their destruction takes time (5-7); insert at END of a forward_list is bad (8).");

  return 0;
}

// 1. Insertion at end of vector
Timer part1(std::size_t count)
{
  std::vector<int> tab;
  std::println("1. push_back {} into vector (initial capacity {})", count, tab.capacity());

  Timer timer;
  timer.Start();
  for (std::size_t i = 0; i < count; i++)
  {
    tab.push_back(static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}

// 2. Insertion at end of vector with reserve()
Timer part2(std::size_t count)
{
  std::vector<int> tab;
  tab.reserve(count);
  std::println("\n2. push_back {} into vector WITH reserve (capacity {})", count, tab.capacity());

  Timer timer;
  timer.Start();
  for (std::size_t i = 0; i < count; i++)
  {
    tab.push_back(static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}

// 3. Insertion at beginning of vector (VERY slow — O(n²))
Timer part3(std::size_t count)
{
  std::vector<int> tab;
  std::println("\n3. insert {} at begin of vector (no reserve)", count);

  Timer timer;
  timer.Start();
  auto it = tab.begin();
  for (std::size_t i = 0; i < count; i++)
  {
    it = tab.insert(it, static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}

// 4. Same as 3 with reserve (still slow — reserve doesn't help with shifts)
Timer part4(std::size_t count)
{
  std::println("\n4. insert {} at begin of vector WITH reserve", count);
  std::vector<int> tab;
  tab.reserve(count);

  Timer timer;
  timer.Start();
  auto it = tab.begin();
  for (std::size_t i = 0; i < count; i++)
  {
    it = tab.insert(it, static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}

// 5. Insertion at end of a doubly-linked list
Timer part5(std::size_t count)
{
  std::println("\n5. push_back {} into list (doubly-linked)", count);
  std::list<int> myList;

  Timer timer;
  timer.Start();
  for (std::size_t i = 0; i < count; i++)
  {
    myList.push_back(static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}

// 6. Insertion at beginning of a doubly-linked list
Timer part6(std::size_t count)
{
  std::println("\n6. push_front {} into list (doubly-linked)", MANY_ELEMENTS);
  std::list<int> myList;

  Timer timer;
  timer.Start();
  for (std::size_t i = 0; i < count; i++)
  {
    myList.push_front(static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}

// 7. Insertion at beginning of a forward_list
Timer part7(std::size_t count)
{
  std::println("\n7. push_front {} into forward_list", count);
  std::forward_list<int> fList;

  Timer timer;
  timer.Start();
  for (std::size_t i = 0; i < count; i++)
  {
    fList.push_front(static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}

// 8. Insertion at END of a forward_list (must traverse each time → BAD)
Timer part8(std::size_t count)
{
  std::println("\n8. insert_after at end of forward_list - {} elements (O(n^2))", count);
  std::forward_list<int> fList;

  Timer timer;
  timer.Start();
  for (std::size_t i = 0; i < count; i++)
  {
    auto it = fList.before_begin();
    for (std::size_t offset = 0; offset < i; offset++)
    {
      ++it;
    }
    it = fList.insert_after(it, static_cast<int>(i));
  }
  timer.Stop();

  return timer;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 9.4

### Exercice 1 : conteneurs associatifs et template

{{<details "1242.2_09.08_MultimapTemplates" >}}
**`ShowMultimap.h`**
<!-- SNIPPET:BEGIN source_file=ShowMultimap.h id=1242.2_Exercises_09.08_MultimapTemplates_ShowMultimap.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#pragma once

#include <print>
#include <map>

// Display every (key, value) pair using structured bindings.
template <typename Key, typename T>
void showMultimap(const std::multimap<Key, T> &map)
{
  for (const auto &[key, value] : map)
  {
    std::println("{}\t{}", key, value);
  }
  std::println();
}

// Display every value sharing the given key using lower_bound / upper_bound.
template <typename Key, typename T>
void showMultimapRange(const std::multimap<Key, T> &map, const Key &key)
{
  auto itLow = map.lower_bound(key);
  auto itUp = map.upper_bound(key);

  std::println("{}===> ", key);
  for (auto it = itLow; it != itUp; ++it)
  {
    std::println(" | {}", it->second);
  }
  std::println();
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.08_MultimapTemplates_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <map>
#include <string>

#include "ShowMultimap.h"

int main()
{
    std::multimap<std::string, std::string> stateMap = {
        {"USA", "New York"},
        {"USA", "Washington"},
        {"USA", "Boston"},
        {"Switzerland", "Berne"}};

    showMultimap(stateMap);

    std::string filter = "USA";
    showMultimapRange(stateMap, filter);
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 2 : conteneurs associatifs et algorithmes

{{<details "1242.2_09.09_WordOccurrences" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.09_WordOccurrences_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <algorithm>
#include <fstream>
#include <map>
#include <print>
#include <string>
#include <utility>
#include <vector>

static void showResults(const std::map<std::string, int>& occurrences, int totalWords)
{
    std::println("The file contains {} words", totalWords);
    std::println("Distinct words : {}", occurrences.size());

    using Entry = std::pair<int, std::string>;
    std::vector<Entry> sorted;
    sorted.reserve(occurrences.size());
    for (const auto& [word, count] : occurrences)
    {
        sorted.emplace_back(count, word);
    }

    std::sort(sorted.begin(), sorted.end(), [](const Entry& a, const Entry& b) {
        const auto& [countA, wordA] = a;
        const auto& [countB, wordB] = b;
        if (countA != countB)
        {
            return countA > countB; // primary: descending count
        }
        return wordA < wordB;       // secondary: ascending word
    });

    for (const auto& [count, word] : sorted)
    {
        std::println("{}x \"{}\"", count, word);
    }
}

int main(int argc, char* argv[])
{
    std::string filePath = (argc > 1) ? argv[1] : "jobs.txt";

    std::ifstream file(filePath);
    if (!file)
    {
        std::println("Error: cannot open '{}'", filePath);
        return 1;
    }

    std::map<std::string, int> occurrences;
    std::string word;
    int totalWords = 0;
    while (file >> word)
    {
        ++occurrences[word]; // operator[] creates-with-zero then increments
        ++totalWords;
    }

    showResults(occurrences, totalWords);
    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 9.5 : smart pointers

### Exercice 1 : "de natif à smart !"

{{<details "1242.2_09.10_SmartPointerPoint" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_09.10_SmartPointerPoint_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#pragma once

class Point
{
public:
    Point(char label, double x = 0, double y = 0);
    Point(const Point& other);
    ~Point();

    void show() const;
    void translate(double dx, double dy);

private:
    double m_x{0};
    double m_y{0};
    char m_label{'P'};
};
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_09.10_SmartPointerPoint_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

#include <print>

Point::Point(char label, double x, double y)
    : m_x(x), m_y(y), m_label(label)
{
    std::println("[Standard constructor] {}", m_label);
}

Point::Point(const Point& other)
    : m_x(other.m_x), m_y(other.m_y), m_label(other.m_label)
{
    std::println("[Copy constructor] {}", m_label);
}

Point::~Point()
{
    std::println("[Destructor] {}", m_label);
}

void Point::show() const
{
    std::println("{} : ({}, {})", m_label, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
    m_x += dx;
    m_y += dy;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_09.10_SmartPointerPoint_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <cmath>
#include <iostream>
#include <memory>
#include <numbers>
#include <print>
#include <vector>

#include "Point.h"

using UPtrPoint = std::unique_ptr<Point>;
using PolygonPointArray = std::vector<UPtrPoint>;

// Places n points regularly on the unit circle, labelled 'A', 'B', 'C', …
static auto generatePolygon(int sideCount)
{
    PolygonPointArray points;
    points.reserve(sideCount);
    for (int i = 0; i < sideCount; ++i)
    {
        double angle = (static_cast<double>(i) / sideCount) * 2 * std::numbers::pi;
        points.push_back(std::make_unique<Point>(
            static_cast<char>('A' + i), std::cos(angle), std::sin(angle)));
    }
    return points; // copy elision / implicit move
}

int main()
{
    constexpr int MIN_SIDES = 3;

    std::println("\nDYNAMIC ALLOCATION (SMART POINTER)");
    std::println("==================================");
    auto upPt = std::make_unique<Point>('D', 10, -5);
    upPt->show();

    int sideCount = 4;
    std::print("\nHow many points should the polygon have? ");
    std::cin >> sideCount;

    if (sideCount >= MIN_SIDES)
    {
        PolygonPointArray polygon = generatePolygon(sideCount);
        std::println("POLYGON with {} points:", sideCount);
        for (const auto& p : polygon)
        {
            p->show();
        }
    }
    else
    {
        std::println("Impossible: a polygon needs at least {} sides", MIN_SIDES);
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
