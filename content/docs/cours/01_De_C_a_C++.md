---
title: "1. De C à C++"
type: docs
weight: 10
draft: false
---

# Chapitre 1 : de C à C++

## Slides
{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/01_De_C_a_C++.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/01_De_C_a_C++.html?print-pdf)

## Exemples

### 1242.2_01.01_HelloWorld

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.01_HelloWorld_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <print>

int main()
{
  std::cout << "Hello world++!" << std::endl;

  // Since C++23
  std::println("Hello world from C++23!");

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.02_VariablesDeclarations

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.02_VariablesDeclarations_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

int main()
{
    for (int i = 0; i < 3; ++i)
    {
        int x = i * 2;
        std::println("{}", x);
    }

    return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.03_Namespaces

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.03_Namespaces_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

namespace language::english
{
  std::string colors[] = {"White", "Red", "Black"};
  void colorName(int index)
  {
    std::println("The color is: {}", colors[index]);
  }
}

namespace language
{
  namespace french
  {
    std::string colors[] = {"Blanc", "Rouge", "Noir"};
    void colorName(int index)
    {
      std::println("La couleur est : {}", colors[index]);
    }
  }
}

// Promote language namespace in the global namespace
using namespace language;

int main()
{
  // GCC: error: 'colorName' was not declared in this scope
  // colorName(1);

  // OK: we specify the namespace for the colorName function
  english::colorName(1);

  // following brackets { }  are to show scope limitation
  {
    using namespace french;
    colorName(1); // -> "Rouge"
  } // end of scope for the using namespace french directive

  // Promote english namespace in the global namespace
  using namespace english;
  colorName(1);         // -> "Red"
  french::colorName(1); // -> "Rouge"

  // Promote french namespace in the global namespace
  using namespace french;

  // GCC: error: call of overloaded 'colorName(int)' is ambiguous
  // colorName(1);

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.04_CinCout

{{<attention>}}
Les modificateurs de formatage sont persistants.
{{</attention>}}

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.04_CinCout_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
  // Store the current formatting flags, precision and fill character of std::cout
  auto flags = std::cout.flags();
  auto precision = std::cout.precision();
  auto fill = std::cout.fill();

  std::cout << std::setfill('.')
            << std::setw(25) << std::right << "Column 1"
            << "Column 3"
            << "\n"
            << std::setw(10) << std::left << "Column 2\n";

  std::cout << std::setprecision(5) << std::fixed << std::setw(25)
            << std::left << 158.82589 << std::endl
            << std::setw(10) << std::left << 456.10288432 // --> 456.10288
            << std::endl;

  std::cout << std::hex << std::uppercase
            << std::setw(25) << std::left << 255
            << std::setw(10) << std::left << 128 // Note: the format is still hex
            << std::endl;

  std::cout << std::setw(25) << std::left << std::boolalpha << true //--> "true"
            << std::setw(10) << std::left << false                  //--> "false"
            << std::endl;

  std::cout << true << std::endl;                     //--> "true"
  std::cout << std::noboolalpha << true << std::endl; //--> "1"

  // Reset std::cout to default formatting
  std::cout.flags(flags);
  std::cout.precision(precision);
  std::cout.fill(fill);
  
  int n;
  std::cin >> n;
  std::cout << "val " << n;

  int j = 10;
  std::cout << std::hex << std::nouppercase << j << std::endl;
  std::cout << std::hex << std::uppercase << j << std::endl;
  std::cout << std::dec << std::showpos << j << std::endl;

  int N = 0;
  std::cout << "Enter a number between 1 and 6: ";
  while (!(std::cin >> N) || N < 1 || N > 6)
  {
    if (std::cin.fail())
    {
      std::cout << "Wrong input, try again: ";
      std::cin.clear();
      std::cin.ignore(256, '\n');
    }
    else
    {
      std::cout << "The number is out of range: ";
    }
  }

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.05_Print
{{<a_noter>}}
**C++23**

La fonction **`std::print()`** affiche du texte formaté de manière plus simple que les fonctions d'affichage précédentes.
En particulier, les modificateurs de formatage sont locaux à l'appel de la fonction **`std::print()`** et ne sont pas persistants.
{{</a_noter>}}

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.05_Print_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

int main()
{
  // C++20/23: std::format syntax with {:.Nf} instead of std::setprecision
  double pi = 3.1415926535897932384626433832795;
  std::println("{:.2f}", pi);
  std::println("{:.8f}", pi);
  std::println("{:.4e}", pi);
  std::println("{:.2f}", pi);

  // C++23: print and println instead of std::cout and std::endl
  std::string firstname = "Donald";
  std::string lastname = "Knuth";
  int answerToEverything = 42;

  std::println("Hello, {} {}!", firstname, lastname);
  std::print("The answer is = {}\n", answerToEverything);

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.06_References

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.06_References_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>
#include <stdexcept>

int &getRefOnCount()
{
  static int count = 0;
  return count;
}

const int N = 2;
std::string names[N] = {"Bob", "John"};
int ages[N] = {20, 30};

int &age(const std::string &name)
{
  for (int i = 0; i < N; i++)
  {
    if (name == names[i])
      return ages[i];
  }

  // If we are here, the name was not found
  // See chapter on exceptions for more details
  throw std::out_of_range("name not found");
}

int main()
{
  double d1 = 1.0;
  double &rd1 = d1;
  std::println("double");
  // sizeof(ref) is the size of the variable it references
  std::println(" - Address for d1  = {} {}", static_cast<const void*>(&d1), sizeof(d1));
  std::println(" - Address for rd1 = {} {}", static_cast<const void*>(&rd1), sizeof(rd1));
  std::println("");

  int i1 = 10;
  int &ri1 = i1;
  std::println("int");
  // sizeof(ref) is the size of the variable it references
  std::println(" - Address for i1  = {} {}", static_cast<const void*>(&i1), sizeof(i1));
  std::println(" - Address for ri1 = {} {}", static_cast<const void*>(&ri1), sizeof(ri1));
  std::println("");

  struct STRUCT
  {
    double x, y, z;
  };

  // Note: no need for struct keyword in C++
  STRUCT varStruct{1.0, 2.0, 3.0};
  STRUCT &refStruct = varStruct;
  std::println("STRUCT");
  // sizeof(ref) is the size of the variable it references
  std::println(" - Address for varStruct = {} {}", static_cast<const void*>(&varStruct), sizeof(varStruct));
  std::println(" - Address for refStruct = {} {}", static_cast<const void*>(&refStruct), sizeof(refStruct));

  // getRefOnCount() returns a reference on the static variable count
  // So we modify count directly
  std::println("Count: {}", getRefOnCount()++);
  std::println("Count: {}", ++getRefOnCount());

  for (int i = 0; i < N; i++)
  {
    std::println("{} {}", names[i], ages[i]);
  }

  age("Bob") = 50;

  for (int i = 0; i < N; i++)
  {
    std::println("{} {}", names[i], ages[i]);
  }

  age("John")++;

  for (int i = 0; i < N; i++)
  {
    std::println("{} {}", names[i], ages[i]);
  }

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.07_MemoryAllocation

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.07_MemoryAllocation_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

int main()
{
  // [[maybe_unused]] to avoid the compiler warning about an unused variable
  // GCC: warning: variable 'x' set but not used [-Wunused-but-set-variable]
  [[maybe_unused]] int *x = nullptr;

  // See chapter on exceptions for more details
  try
  {
    for (int n = 1;; n++)
    {
      std::println("{}", n);
      // throws std::bad_alloc if no more memory is available
      x = new int[1024 * 1024];
      // Comment to provoke a memory leak
      delete[] x;
    }
  }
  // See chapter on exceptions for more details
  catch (const std::bad_alloc &e)
  {
    std::println("Memory allocation failed: {}", e.what());
  }

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.08_Strings

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.08_Strings_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

int main()
{
  std::string x = "Hello";
  // Or
  // auto x = std::string("Hello");

  std::string y = x;
  std::string z = x + "_" + y;
  std::println("{} {} {}", x, y, z);
  std::println("cap: {}", z.capacity());
  std::println("size: {}", z.size());

  // C++14: string literals
  // Need to add "using namespace std::string_literals;"
  using namespace std::string_literals;
  auto s = "Hello"s;

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.09_Vectors

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.09_Vectors_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>
#include <vector>

using Line = std::vector<double>;
using Matrix = std::vector<Line>;

int main()
{
  // {10, 11}
  std::vector<int> myVector1{10,11};

  // {10.0, 11.0}
  std::vector<double> myVector2;
  myVector2.push_back(10.0);
  myVector2.push_back(11.0);
  
  // {5, 5}
  std::vector<int> myVector3(2,5);
  // {10, 11}
  myVector3[0]=10;
  myVector3[1]=11;
  
  Matrix m(5); 
  for (int i = 0; i < 5; ++i)
  {
    m[i].resize(5); // rows size is 5
    for (int j = 0; j < 5; ++j)
    {
      if (i == j)
      {
        m[i][j] = 1;
      }
      else
      {
        m[i][j] = 0;
      }
    }
  }

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.10_Double2String

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.10_Double2String_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>

#include <sstream>
#include <iomanip>

#include <print>

int main()
{
  auto pi = 3.1415926535897932384626433832795;
  // C++11: std::to_string, with no control over the format
  auto s1 = std::to_string(pi);
  std::print("C++11: std::to_string: {}\n", s1);

  // C++11: std::ostringstream, with control over the format
  std::ostringstream oss;
  oss << std::fixed << std::setprecision(2) << pi;
  auto s2 = oss.str();
  std::print("C++11: std::ostringstream: {}\n", s2);

  // C++20: std::format
  auto s3 = std::format("{:.2f}", pi);
  std::print("C++20: std::format: {}\n", s3);
}
```
<!-- SNIPPET:END -->

### 1242.2_01.11_DefaultParameters
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.11_DefaultParameters_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <vector>
#include <print>
#include <algorithm>

void sort(const std::vector<int> &v, bool ascending = true)
{
  auto sorted = v;

  if (ascending)
  {
    std::sort(sorted.begin(), sorted.end());
  }
  else
  {
    std::sort(sorted.rbegin(), sorted.rend());
  }
  std::print("Sorted vector: ");
  for (const auto &elem : sorted)
  {
    std::print("{} ", elem);
  }
  std::print("\n");
}

int main()
{
  auto v = std::vector<int>{5, 2, 9, 1, 5, 6};
  sort(v);
  sort(v, false);
}
```
<!-- SNIPPET:END -->

### 1242.2_01.12_FunctionsOverloading
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_01.12_FunctionsOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

int add(int a, int b)
{
  return a + b;
}

int add(int a, int b, int c)
{
  return a + b + c;
}

double add(double a, double b)
{
  return a + b;
}

double add(double a, double b, double c)
{
  return a + b + c;
}

int main()
{
  // Same name, different parameters
  std::println("add(2, 3) = {}", add(2, 3));
  std::println("add(2.5, 3.5) = {}", add(2.5, 3.5));
  std::println("add(2, 3, 4) = {}", add(2, 3, 4));
  std::println("add(2.5, 3.5, 4.5) = {}", add(2.5, 3.5, 4.5));
}
```
<!-- SNIPPET:END -->

### Les types de containers dans la bibliothèque standard

{{< plantuml id="chap1_Containers">}}
@startuml

skin rose
skinparam defaultFontSize 20
skinparam classFontStyle bold
skinparam classAttributeIconSize 0
hide circle

package "Conteneurs" as containers #F0F0F0 {

    package "Conteneurs séquentiels" as seq #D6EAF8 {
        class "std::array" as array #AED6F1 {
            Taille fixe
        }
        class "std::vector" as vector #AED6F1 {
            Taille dynamique
        }
        class "std::deque" as deque #AED6F1 {
            Double-ended
        }
        class "std::list" as list #AED6F1 {
            Liste doublement chaînée
        }
        class "std::forward_list" as flist #AED6F1 {
            Liste simplement chaînée
        }
    }

    package "Conteneurs associatifs ordonnés" as assoc #D5F5E3 {
        class "std::set" as set #ABEBC6 {
            Éléments uniques
        }
        class "std::multiset" as mset #ABEBC6 {
            Doublons autorisés
        }
        class "std::map" as map #ABEBC6 {
            Clés uniques
        }
        class "std::multimap" as mmap #ABEBC6 {
            Clés dupliquées
        }
    }

    package "Conteneurs associatifs non ordonnés (C++11)" as uassoc #FAD7A0 {
        class "std::unordered_set" as uset #F9E79F {
            Éléments uniques
        }
        class "std::unordered_multiset" as umset #F9E79F {
            Doublons autorisés
        }
        class "std::unordered_map" as umap #F9E79F {
            Clés uniques
        }
        class "std::unordered_multimap" as ummap #F9E79F {
            Clés dupliquées
        }
    }

    package "Adaptateurs de conteneurs" as adapt #E8DAEF {
        class "std::stack" as stack #D7BDE2 {
            LIFO
        }
        class "std::queue" as queue #D7BDE2 {
            FIFO
        }
        class "std::priority_queue" as pqueue #D7BDE2 {
            Plus grande priorité en tête
        }
    }
}

' Relations : adaptateurs vers conteneurs sous-jacents
stack ..> deque
queue ..> deque
pqueue ..> vector

@enduml
{{< /plantuml >}}

## Série 1.1

### Exercice 1 : affichage
Compléter le code suivant :

```cpp
bool isNumber = true;
std::cout <<  isNumber << " " << !isNumber << std::endl;
std::cout <<  isNumber << " "  << !isNumber << std::endl;

int x = 15;
std::cout  << x << " " << x << " " << x << std::endl;
std::cout  << x << " " << x << " " << x << std::endl;

double dbl = -5345.123456789;
std::cout << dbl << std::endl;
std::cout << dbl << std::endl;
std::cout << dbl << std::endl;
std::cout << dbl << std::endl;
```

de manière à obtenir le résultat suivant:

```cpp
true false
1 0

hexadecimal: f decimal: 15 octal: 17
15 15 15

-5345.12
-5345.12345679
-5.3451e+03
-5345.12
```

### Exercice 2 : surcharge de fonctions
1) Écrire deux fonctions **`minimum()`** qui retournent le plus petit des 2 nombres passés en arguments.
La première utilise des nombres entiers (**`int`**) et la seconde des nombres décimaux (**`double`**).
2) Laquelle de ces fonctions sera appelée si on lui passe les paramètres suivants :
    
	  **`minimum(7, 3)`**, **`minimum(7.0, 3)`**, **`minimum(7, 3.0)`** et **`minimum(7.0, 3.0)`** ?

    Que se passe-t-il si on supprime la méthode qui reçoit deux entiers en arguments ?

Pour aller plus loin : [Résolution de surcharge et conversions implicites]({{< relref "posts/surcharge_et_conversions_implicites.md" >}})

### Exercice 3 : passage de paramètres
Écrire des fonctions **`<return> divide(dividend, divisor, <other_params>)`** qui, à partir de deux entiers passés en paramètre, retournent le **quotient** et le **reste** de la division entière.

**Exemple**

13 divisé par 2 donne un quotient de 6 et un reste de 1.

Tester les différentes possibilités de passage de paramètres en C++.
Lesquelles vous semblent les plus appropriées à ce problème, et pourquoi ?

### Exercice 4 : string
Écrire un programme qui :
- utilise une fonction **`askForAString()`** demandant à l'utilisateur de saisir une phrase et renvoyant cette phrase au programme principal sous la forme d'un pointeur **`char*`**.
Le programme déclarera ensuite  une variable de type **`string`** pour y copier cette phrase et en calculer sa longueur avec la fonction **`size()`**.
Une fois la copie faite, libérer la mémoire allouée dynamiquement et afficher le message contenu dans le **`string`**.
  
Bonus : concaténer au **`string`** des points ('.') jusqu'à concurrence de sa capacité.

**Consigne :** gérer l'allocation dynamique et la récupération de la mémoire avec les opérateurs C++ **`new`** et **`delete`**.

### Exercice 5 : range-based for loop
Compléter le programme suivant :
1) remplacer la boucle **`for`** suivante par une boucle **`range-based`**
2) copier les valeurs du tableau **`primeNumbers`** dans le tableau **`copie`**

Pourquoi ne peut-on pas faire cette copie **SIMPLEMENT** avec le nouveau **`for`** ?
      
```cpp 
#include <iostream>

int main()
{
  int primeNumbers[] = {2, 3, 5, 7, 11, 13, 17};
  int copy[7]  = {0, 0, 0, 0, 0, 0, 0};
  int sizeArray = sizeof(primeNumbers) / sizeof(primeNumbers[0]);

  //TODO
  for (int i=0; i < sizeArray; i++)
  {
    std::cout << primeNumbers [i] << std::endl;
  }

  // TODO

  return 0;
}
```

### Exercice 6 : structure
1) Définir une structure **`Room`** capable de contenir les dimensions d'une chambre (largeur, longueur, hauteur), de lui donner un nom à l'aide d'un champ de type **`string`**, et possédant les fonctions suivantes : 
   - **`surfaceFloor()`** : calcule et renvoie la surface au sol de la pièce
   - **`surfaceWalls()`** : calcule et renvoie la surface des murs de la pièce
   - **`volume()`** : calcule et renvoie le volume de la pièce

2) Écrire un programme utilisant ce nouveau type, qui lui affecte des valeurs et utilise ses fonctions (méthodes)
