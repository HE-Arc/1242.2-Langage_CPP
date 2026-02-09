---
title: "1. De C à C++"
type: docs
weight: 10
draft: false
---

# Chapitre 1 : de C à C++

## Exemples

### 1242.2_01.01_HelloWorld

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_01.01_HelloWorld -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int main()
{  
  std::cout << "Hello world++!" << std::endl;

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.02_VariablesDeclarations

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_01.02_VariablesDeclarations -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>

int main()
{
    for (int i = 0; i < 3; ++i)
    {
        int x = i * 2;
        std::cout << x << std::endl;
    }

    return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.03_Namespaces

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_01.03_Namespaces -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>

namespace language::english
{
  std::string colors[] = {"White", "Red", "Black"};
  void colorName(int index)
  {
    std::cout << "The color is: " << colors[index] << std::endl;
  }
}

namespace language
{
  namespace french
  {
    std::string colors[] = {"Blanc", "Rouge", "Noir"};
    void colorName(int index)
    {
      std::cout << "La couleur est : " << colors[index] << std::endl;
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

  // GGC: error: call of overloaded 'colorName(int)' is ambiguous
  // colorName(1);

  return 0;
}
```
<!-- SNIPPET:END -->

### 1242.2_01.04_CinCout

{{<attention>}}
Les modificateurs de formatage sont persistants.
{{</attention>}}

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_01.04_CinCout -->
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
            << std::setw(25) << std::right << "Colonne 1"
            << "Colonne 3"
            << "\n"
            << std::setw(10) << std::left << "Colonne 2\n";

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
  std::cout << "Entrez un chiffre entre 1 et 6 : ";
  while (!(std::cin >> N) || N < 1 || N > 6)
  {
    if (std::cin.fail())
    {
      std::cout << "Saisie incorrecte, recommencez : ";
      std::cin.clear();
      std::cin.ignore(256, '\n');
    }
    else
    {
      std::cout << "Le chiffre n'est pas entre 1 et 6: ";
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

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_01.05_Print -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

int main()
{  
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

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_01.06_References -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>

int &getRefOnCount()
{
  static int count = 0;
  return count;
}

const int N = 2;
std::string tabNoms[N] = {"Bob", "John"};
int tabAges[N] = {20, 30};

int &age(std::string nom)
{
  for (int i = 0; i < N; i++)
  {
    if (nom == tabNoms[i])
      return tabAges[i];
  }

  // If we are here, the name was not found
  // See chapter on exceptions for more details
  throw std::out_of_range("nom not found");
}

int main()
{
  double d1 = 1.0;
  double &rd1 = d1;
  std::cout << "double" << std::endl;
  // sizeof(ref) is the size of the variable it references
  std::cout << " - Adresse de d1  = " << &d1 << " "
            << sizeof(d1) << std::endl;
  std::cout << " - Adresse de rd1 = " << &rd1 << " "
            << sizeof(rd1) << std::endl
            << std::endl;

  int i1 = 10;
  int &ri1 = i1;
  std::cout << "int" << std::endl;
  // sizeof(ref) is the size of the variable it references
  std::cout << " - Adresse de i1  = " << &i1 << " "
            << sizeof(i1) << std::endl;
  std::cout << " - Adresse de ri1 = " << &ri1 << " "
            << sizeof(ri1) << std::endl
            << std::endl;

  struct STRUCT
  {
    double x, y, z;
  };

  // Note: no need for struct keyword in C++
  STRUCT varStruct{1.0, 2.0, 3.0};
  STRUCT &refStruct = varStruct;
  std::cout << "STRUCT" << std::endl;
  // sizeof(ref) is the size of the variable it references
  std::cout << " - Adresse de varStruct = " << &varStruct << " "
            << sizeof(varStruct) << std::endl;
  std::cout << " - Adresse de refStruct = " << &refStruct << " "
            << sizeof(refStruct) << std::endl;

  // getRefOnCount() returns a reference on the static variable count
  // So we modify count directly
  std::cout << "Count: " << getRefOnCount()++ << std::endl;
  std::cout << "Count: " << ++getRefOnCount() << std::endl;

  for (int i = 0; i < N; i++)
  {
    std::cout << tabNoms[i] << " " << tabAges[i] << std::endl;
  }

  age("Bob") = 50;

  for (int i = 0; i < N; i++)
  {
    std::cout << tabNoms[i] << " " << tabAges[i] << std::endl;
  }

  age("John")++;

  for (int i = 0; i < N; i++)
  {
    std::cout << tabNoms[i] << " " << tabAges[i] << std::endl;
  }

  return 0;
}
```
<!-- SNIPPET:END -->

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
-5.3451e+003
-5345.12
```

### Exercice 2 : surcharge de fonctions
1) Écrire deux fonctions **`minimum()`** qui retournent le plus petit des 2 nombres passés en arguments.
La première utilise des nombres entiers (**`int`**) et la seconde des nombres décimaux (**`double`**).
2) Laquelle de ces fonctions sera appelée si on lui passe les paramètres suivants :
    
	  **`minimum(7, 3)`**, **`minimum(7.0, 3)`**, **`minimum(7, 3.0)`** et **`minimum(7.0, 3.0)`** ?

    Que se passe-t-il si on supprime la méthode qui reçoit deux entiers en arguments ?

### Exercice 3 : passage de paramètres
Écrire deux fonctions **`divide(dividend, divisor, remainder)`** qui à partir de deux entiers, passés en paramètre, doivent retourner le **quotient** et le **reste** de la division entière. 

**Exemple**

13 divisé par 2 donne un quotient de 6 et un reste de 1.

Tester les différentes possibilités de passage de paramètres en C++. Lesquelles vous semblent les plus appropriées à ce problème ?

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

Pourquoi ne peut-on pas faire cette copie SIMPLEMENT avec le nouveau **`for`** ?
      
```cpp 
#include <iostream>
using namespace std;
int main()
{
  int primeNumbers[] = { 1, 2, 3, 5, 7, 11, 13};
  int copy[7]  = { 0, 0, 0, 0, 0, 0, 0 };
  int sizeArray = sizeof(primeNumbers) / sizeof(int);

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

## Solutions
<!-- [Serie1_SOLUTIONS](/zips/Serie1_SOLUTIONS.zip) -->

## Slides
{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/01_De_C_a_C++.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/01_De_C_a_C++.html?print-pdf)
