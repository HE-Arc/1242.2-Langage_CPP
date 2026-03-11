---
title: "1. De C à C++ — Solutions"
type: docs
weight: 10
draft: false
---

# Chapitre 1 : de C à C++ — Solutions

## Série 1.1

### Exercice 1 : affichage

{{<details "1242.2_01.01_Formatting" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_01.01_Formatting_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <iomanip>
#include <print>

void exercise1();
void exercise1_cpp23();

int main()
{
  exercise1();
  exercise1_cpp23();
  return 0;
}

void exercise1()
{
  bool isNumber = true;
  std::cout << std::boolalpha << isNumber << " " << !isNumber << std::endl;
  std::cout << std::noboolalpha << isNumber << " " << !isNumber << std::endl;
  std::cout << std::endl;

  int x = 15;
  std::cout << "hexadecimal: " << std::hex << x << " decimal: " << std::dec << x << " octal: " << std::oct << x << std::endl;
  std::cout << std::dec << x << " " << x << " " << x << std::endl;
  std::cout << std::endl;

  double dbl = -5345.123456789;
  // Default: 6 significant digits
  // -> -5345.12
  std::cout << dbl << std::endl;
  std::cout << std::setprecision(8) << std::fixed << dbl << std::endl;
  std::cout << std::setprecision(4) << std::scientific << dbl << std::endl;
  std::cout << std::setprecision(6) << std::defaultfloat << dbl << std::endl;
  std::cout << std::endl;
}

void exercise1_cpp23()
{
  bool isNumber = true;
  // std::print (and std::println) prints bool values as "true" and "false" by default
  std::println("{} {}", isNumber, !isNumber);
  std::println("{} {}", static_cast<int>(isNumber), static_cast<int>(!isNumber));
  std::println();

  int x = 15;
  std::println("hexadecimal: {:x} decimal: {:d} octal: {:o}", x, x, x);
  std::println("{} {} {}", x, x, x);
  std::println();

  double dbl = -5345.123456789;
  // Default: shortest round-trip (double -> string -> double) representation
  // -> -5345.123456789
  std::println("{}", dbl);
  std::println("{:.8f}", dbl);
  std::println("{:.4e}", dbl);
  std::println("{:.6g}", dbl);
  std::println();
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 2 : surcharge de fonctions

{{<details "1242.2_01.02_FunctionOverloading" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_01.02_FunctionOverloading_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

double minimum(double val1, double val2)
{
  return val1 < val2 ? val1 : val2;
}

int minimum(int val1, int val2)
{
  return val1 < val2 ? val1 : val2;
}

int main()
{
  std::println("{}", minimum(7, 3));
  std::println("{}", minimum(7.0, 3.0));

  // The next two instructions are rejected by the compiler because their arguments types
  // do not match exactly neither of the overloaded minimum functions: "ambiguous call".
  // They are accepted however if only one function is available (no longer ambiguous)
  // Note, that the behavior will change with float instead of double.
  // std::println("{}", minimum(7.0, 3));
  // std::println("{}", minimum(7, 3.0));

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 3 : passage de paramètres

{{<details "1242.2_01.03_ParameterPassing" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_01.03_ParameterPassing_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
// See exceptions chapter
// #include <stdexcept> to use std::domain_error and std::overflow_error

int divide(int dividend, int divisor, int &remainder);
int divide(int dividend, int divisor, int *pRemainder);
bool divide(int dividend, int divisor, int &remainder, int &quotient);

int main()
{
  int remainder = 0;
  std::println("** Division of 37 by 2 **\n");

  int quotient = divide(37, 2, remainder);
  std::println("= Pass by reference =");
  std::println("quotient: {}, remainder: {}\n", quotient, remainder);

  quotient = divide(37, 2, &remainder);
  std::println("= Pass by pointer =");
  std::println("quotient: {}, remainder: {}", quotient, remainder);

  bool ok = divide(37, 2, remainder, quotient);
  // Could be if (!ok) instead, but this more explicit
  if (ok == false)
  {
    std::println("Something went wrong");
    return 1;
  }

  std::println("= Pass by reference (multiple outputs) =");
  std::println("quotient: {}, remainder: {}\n", quotient, remainder);

  return 0;
}

int divide(int dividend, int divisor, int &remainder)
{
  if (divisor == 0)
  {
    if (dividend == 0)
    {      
      // See exceptions chapter
      // throw std::domain_error("0/0 is undefined");
    }
    else
    {
      // See exceptions chapter
      // throw std::overflow_error("x/0 is infinite");
    }

    // Unreachable once exceptions are thrown above
    return 0;
  }

  remainder = dividend % divisor;
  return dividend / divisor;
}

int divide(int dividend, int divisor, int *pRemainder)
{
  if (divisor == 0)
  {
    if (dividend == 0)
    {
      // See exceptions chapter
      // throw std::domain_error("0/0 is undefined");
    }
    else
    {
      // See exceptions chapter
      // throw std::overflow_error("x/0 is infinite");
    }

    // Unreachable once exceptions are thrown above
    return 0;
  }

  *pRemainder = dividend % divisor;
  return dividend / divisor;
}

bool divide(int dividend, int divisor, int &remainder, int &quotient)
{
  if (divisor == 0)
  {
    if (dividend == 0)
    {
      // See exceptions chapter
      // throw std::domain_error("0/0 is undefined");
    }
    else
    {
      // See exceptions chapter
      // throw std::overflow_error("x/0 is infinite");
    }

    // Unreachable once exceptions are thrown above
    return false;
  }

  remainder = dividend % divisor;
  quotient = dividend / divisor;

  return true;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 4 : string

{{<details "1242.2_01.04_DynamicStrings" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_01.04_DynamicStrings_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>
#include <cstdio>

constexpr int MAX_LENGTH = 256;

char *askForAString();

int main()
{
    auto ptrInput = askForAString();
    std::print("{}", ptrInput);
    auto inputString = std::string(ptrInput);
    delete[] ptrInput;
    ptrInput = nullptr;

    std::println("\nLength: {}\t\tCapacity: {}", inputString.size(), inputString.capacity());
    
    auto spaceAvailable = inputString.capacity() - inputString.size();
    inputString.append(spaceAvailable, '.');
    std::println("\n{}", inputString);

    return 0;
}

char *askForAString()
{
    char *sentence = new char[MAX_LENGTH];
    std::print("Please type a sentence with a few words: ");
    fgets(sentence, MAX_LENGTH, stdin);
    return sentence;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 5 : range-based for loop

{{<details "1242.2_01.05_RangeBasedFor" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_01.05_RangeBasedFor_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

int main()
{
    int primeNumbers[] = {2, 3, 5, 7, 11, 13, 17};
    constexpr auto sizeArray = sizeof(primeNumbers) / sizeof(primeNumbers[0]);
    // Zero-initialized
    int copy[sizeArray] = {};

    for (auto i = 0u; i < sizeArray; i++)
    {
        std::println("{}", primeNumbers[i]);
    }

    // 1. Range-based for loop
    for (const auto &elem : primeNumbers)
    {
        std::println("{}", elem);
    }

    // 2. Copy using range-based for loop
    int i = 0;
    for (const auto &elem : primeNumbers)
    {
        copy[i++] = elem;
    }

    // 3. Print the copy
    for (const auto &elem : copy)
    {
        std::println("{}", elem);
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 6 : structure

{{<details "1242.2_01.06_StructMethods" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_01.06_StructMethods_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

struct Room
{
  double width{0.0};
  double length{0.0};
  double height{0.0};
  std::string name;

  double surfaceFloor() const { return width * length; }
  double surfaceWalls() const { return 2 * (width + length) * height; }
  double volume() const { return width * length * height; }
  void show() const
  {
    std::println("{}[L:W:H]{}:{}:{}", name, length, width, height);
    std::println("Walls surface:{}", surfaceWalls());
    std::println("Floor surface:{}", surfaceFloor());
    std::println("Volume:{}", volume());
  }
};

int main()
{
  Room myBedroom;
  myBedroom.height = 3.5;
  myBedroom.width = 4.0;
  myBedroom.length = 3.0;
  myBedroom.name = "Bedroom";

  // Access to struct members and methods
  std::println("{}[L:W:H]{}:{}:{}", myBedroom.name, myBedroom.length, myBedroom.width, myBedroom.height);
  std::println("Walls surface:{}", myBedroom.surfaceWalls());
  std::println("Floor surface:{}", myBedroom.surfaceFloor());
  std::println("Volume:{}", myBedroom.volume());

  // GCC warning: missing initializer for member 'Room::name'
  // Room otherRoom = {2.5, 5, 6};
  // otherRoom.name is empty
  // Using show() instead
  // otherRoom.show();

  Room kitchen = {2.5, 3.5, 2.4, "Kitchen"};
  kitchen.show();

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
