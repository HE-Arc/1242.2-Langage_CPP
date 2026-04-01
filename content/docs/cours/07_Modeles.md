---
title: "7. Modèles"
type: docs
weight: 10
---

# Chapitre 7 : modèles

## Slides
{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/07_Modeles.html" >}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/07_Modeles.html?print-pdf)

## Exemples

{{<details "1242.2_07.01_FunctionTemplateMaxi" >}}
**`Time.h`**
<!-- SNIPPET:BEGIN source_file=Time.h id=1242.2_Examples_07.01_FunctionTemplateMaxi_Time.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>

class Time
{
public:
    Time(int h = 0, int m = 0, int s = 0) : m_hour(h), m_minute(m), m_second(s) {}

    bool operator>(const Time& other) const
    {
        return toSeconds() > other.toSeconds();
    }

    int getHour() const { return m_hour; }
    int getMinute() const { return m_minute; }
    int getSecond() const { return m_second; }

    friend std::ostream& operator<<(std::ostream& os, const Time& t);

private:
    int toSeconds() const
    {
        return m_hour * 3600 + m_minute * 60 + m_second;
    }

    int m_hour{0};
    int m_minute{0};
    int m_second{0};
};

inline std::ostream& operator<<(std::ostream& os, const Time& t)
{
    return os << t.m_hour << "h" << t.m_minute << "'" << t.m_second << "\"";
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_07.01_FunctionTemplateMaxi_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include "Time.h"

template <typename T>
T maxi(const T& a, const T& b)
{
    return (a > b) ? a : b;
}

int main()
{
    Time t1(9, 57, 59);
    Time t2(9, 58, 37);

    auto maxTime = maxi<Time>(t1, t2); // Explicit type specification
    maxTime = maxi(t1, t2);            // Automatic type deduction

    // Time has operator<< but no std::formatter, so use std::cout
    std::cout << maxTime << " = maxi(" << t1 << ", " << t2 << ")" << '\n';

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_07.02_FunctionTemplateRectangle" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_07.02_FunctionTemplateRectangle_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <iostream>

class Rectangle
{
public:
  Rectangle(double w = 0, double h = 0) : m_width(w), m_height(h) {}

  bool operator>=(const Rectangle &other) const
  {
    return (m_width * m_height) >= (other.m_width * other.m_height);
  }

  friend std::ostream &operator<<(std::ostream &os, const Rectangle &r);

private:
  double m_width{0};
  double m_height{0};
};

std::ostream &operator<<(std::ostream &os, const Rectangle &r)
{
  return os << "[" << r.m_width << ", " << r.m_height << "]";
}

template <typename T>
T maxi(const T &a, const T &b)
{
  return (a >= b) ? a : b;
}

int main()
{
  auto i1 = 3;
  auto i2 = 4;
  auto d1 = 2.34;
  auto d2 = 2.35;
  Rectangle r1(10, 20);
  Rectangle r2(20, 30);

  auto maxInt = maxi(i1, i2);             // Automatic type deduction
  auto maxDouble1 = maxi(d1, d2);         // Automatic type deduction
  auto maxDouble2 = maxi<double>(i1, d1); // Explicit: compiler can't deduce mixed types
  // maxi(i1, d1);                        // Would not compile: ambiguous types
  auto maxRectangle = maxi(r1, r2); // Rectangle must overload operator>=

  std::println("maxi(int, int)           : ({}, {}) --> {}", i1, i2, maxInt);
  std::println("maxi(double, double)     : ({}, {}) --> {}", d1, d2, maxDouble1);
  std::println("maxi<double>(int, double): ({}, {}) --> {}", i1, d1, maxDouble2);

  // Rectangle has operator<< but no std::formatter
  std::cout << "maxi(Rectangle, Rectangle): (" << r1 << ", " << r2 << ") --> " << maxRectangle << '\n';

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_07.03_ClassTemplateConversion" >}}
**`Wrapper.h`**
<!-- SNIPPET:BEGIN source_file=Wrapper.h id=1242.2_Examples_07.03_ClassTemplateConversion_Wrapper.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <typeinfo>

template <typename T>
class Wrapper
{
public:
  Wrapper(const T &val = T()) : m_value(val) {}

  // Cross-type converting constructor (not a copy constructor)
  template <typename U>
  Wrapper(const Wrapper<U> &other) : m_value(static_cast<T>(other.getValue())) {}

  T getValue() const { return m_value; }

  template <typename T2>
  friend std::ostream &operator<<(std::ostream &os, const Wrapper<T2> &w);

private:
  T m_value;
};

template <typename T2>
std::ostream &operator<<(std::ostream &os, const Wrapper<T2> &w)
{
  return os << w.m_value << " (type: " << typeid(w.m_value).name() << ")";
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_07.03_ClassTemplateConversion_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include "Wrapper.h"

int main()
{
    Wrapper<float> a(3.1f);   // Value is float
    Wrapper<int> b(a);        // Value is int (converted from float)
    Wrapper<float> f = a;     // Copy constructor (same type)

    // Wrapper has operator<< but no std::formatter
    std::cout << a << '\n';   // Prints 3.1 (float)
    std::cout << b << '\n';   // Prints 3 (int, truncated)
    std::cout << f << '\n';   // Prints 3.1 (float)

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_07.04_ClassTemplateNonType" >}}
**`Array.h`**
<!-- SNIPPET:BEGIN source_file=Array.h id=1242.2_Examples_07.04_ClassTemplateNonType_Array.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

// Class template with non-type template parameter (compile-time constant)
template <typename T, int Size>
class Array
{
public:
  Array() = default;

  T getAt(int pos) const
  {
    if (pos >= 0 && pos < Size)
    {
      return m_data[pos];
    }
    // Invalid position: could throw an exception instead
    return T{-1};
  }

  void setAt(int pos, T val)
  {
    if (pos >= 0 && pos < Size)
    {
      m_data[pos] = val;
    }
  }

  int getSize() const { return Size; }

private:
  T m_data[Size];
};
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_07.04_ClassTemplateNonType_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include "Array.h"

int main()
{
  Array<double, 5> t1;
  t1.setAt(0, 1.5);
  using TabInt7 = Array<int, 7>;
  TabInt7 t2;

  std::println("Array of double, size = {}", t1.getSize());
  std::println("Values outside bounds return -1\n");
  for (int i = -1; i <= t1.getSize(); i++)
  {
    t1.setAt(i, i / 2.0);
    std::print("{}\t", t1.getAt(i));
  }

  std::println("\n");

  std::println("Array of int, size = {}", t2.getSize());
  std::println("Values outside bounds return -1\n");
  for (int i = -1; i <= t2.getSize(); i++)
  {
    t2.setAt(i, i / 2);
    std::print("{}\t", t2.getAt(i));
  }
  std::println("");

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_07.05_TemplateMemberSpecialization" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_07.05_TemplateMemberSpecialization_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

template <typename T>
class Point
{
public:
    Point(T x = 0, T y = 0) : m_x(x), m_y(y) {}
    void show();

private:
    T m_x;
    T m_y;
};

template <typename T>
void Point<T>::show()
{
    std::println("Point<T>::show()    Coordinates: {} {}", m_x, m_y);
}

// Full specialization of member function for char
template <>
void Point<char>::show()
{
    std::println("Point<char>::show() Coordinates: {} {}", static_cast<int>(m_x), static_cast<int>(m_y));
}

int main()
{
    Point<int> ptInt(3, 5);
    ptInt.show();

    Point<char> ptChar('d', 'y');
    ptChar.show();

    Point<double> ptDbl(3.5, 2.3);
    ptDbl.show();

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_07.06_FunctionTemplateOverload" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_07.06_FunctionTemplateOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <cstring>

// Generic template function
template <typename T>
T minVal(T tab[], int n)
{
  std::println("minVal() template");
  auto min = tab[0];
  for (int i = 1; i < n; i++)
  {
    auto current = tab[i];
    if (current < min)
    {
      min = tab[i];
    }
  }
  return min;
}

// Non-template overload (not a specialization) — preferred over template<>
// for char* because it participates correctly in overload resolution
const char *minVal(const char *tab[], int n)
{
  std::println("minVal() overload for char*");
  auto result = tab[0];
  for (int i = 1; i < n; i++)
  {
    if (std::strcmp(tab[i], result) < 0)
    {
      result = tab[i];
    }
  }
  return result;
}

int main()
{
  int tabInt[5] = {5, 7, 2, 6, 9};
  char tabChar[10] = {'H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'};
  const char *tabStr[] = {"Hello", "Bonjour", "Gruezi", "Buenos dias", "Konichiwa"};

  std::println("minVal<int>({{5,7,2,6,9}}, 5): {}", minVal<int>(tabInt, 5));
  std::println("minVal<char>(\"HelloWorld\", 10): {}", minVal<char>(tabChar, 10));
  std::println("minVal({{\"Hello\",\"Bonjour\",...}}, 5): {}", minVal(tabStr, 5));

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_07.07_OverloadResolutionOrder" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_07.07_OverloadResolutionOrder_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

// Non-template function
void f(int)
{
    std::println("Non-template");
}

// Template function
template <typename T>
void f(T)
{
    std::println("Template");
}

// Explicit specialization of the template for int
template <>
void f<int>(int)
{
    std::println("Specialization f<int>");
}

int main()
{
    f(1);    // Calls the non-template version (exact match preferred)
    f('c');  // Calls the template version (T = char)
    f<>(1);  // Calls the specialized template version (f<> forces template)

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 7.1

### Exercice 1 : modèle de fonction

1. Écrire un modèle de fonction **`exchange`** utilisant un paramètre de type **`T`**
2. Réaliser un programme permettant de tester la fonction avec : 
   * deux valeurs entières
   * deux valeurs réelles 
   * deux objets de type **`Time`** (série 3.1)

**Question :** que doit implémenter la classe **`Time`** au minimum ?

### Exercice 2 : paramètre de type et paramètre expressions

Écrire un modèle de fonction **`sum`** muni d'un paramètre de type **`< T >`** et d'un paramètre expression.
La fonction aura deux paramètres :
1.	l’adresse d’un tableau dont les éléments sont de type quelconque (**`float`**, **`int`**, **`Point`**);
2.	le nombre d’éléments qu’il faut additionner.

Cette fonction retourne la somme des éléments indiqués par le deuxième paramètre.

On pourra tester cette fonction avec le programme ci-dessous :

```cpp
int main ()
{
    int   intTable[]   = {3, 5, 2, 1};
    float floatTable[] = {2.5, 3.2, 1.8};
    char  charTable[]  = { 'A', '0', 'i', 'o', 'u' };
    Time timeTable[] = { {5, 10},  {3, 22} };

    std::println("sum(intTable, 4): {}", sum (intTable, 4)); // type deduction
    std::println("sum(floatTable, 3): {}", sum (floatTable, 3)); // type deduction
    std::println("sum(charTable, 5): {}", sum (charTable, 5)); // type deduction
    std::println("sum(timeTable, 2): {}", sum (timeTable, 2)); // type deduction

    return 0;
}
```

## Série 7.2

### Exercice 1 : modèle de classe

Écrire une classe générique **`Vector`** qui permet de manipuler des données de n’importe quel type.
On utilisera un tableau par valeur.

```cpp
Vector<float> myFloatVector;
```
L’instruction ci-dessus va créer une variable **`myFloatVector`** de 3 composantes de type **`float`**.

Pour créer un vector d'une taille différente de 3, la création se fera comme suit : 

```cpp
Vector<int, 4> myIntVector;
```

#### Indications
Il faudra prévoir un constructeur par recopie, un opérateur = pour attribuer un vecteur à partir d’un autre de même type. 
Exemple : 

```cpp
myFloatVector2 = myFloatVector;
```

Une autre surcharge de l'opérateur =  permettra d'initialiser un vecteur avec une même valeur.
Dans cet exemple, tous les éléments de **`myFloatVector`** auront la valeur 5.5.

```cpp
myFloatVector = 5.5;
```

Il est également demandé d'implémenter l'opérateur [] pour protéger l'exécution contre les débordements de tableau.

L'opérateur de flux << sera également implémenté.

Reprenez la classe **`Point`**.
Que faut-il modifier ?

Le programme ci-dessous montre un exemple d’utilisation :

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_07.03_ClassTemplateVector_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int main()
{
    Vector<int, 4> vi = {37};
    vi[3] = 5;
    vi[2] = 2;
    std::cout << vi;

    Vector<double> vd; // 3 elements by default
    vd[0] = 0.0;
    vd[1] = 0.1;
    vd[2] = 0.2;
    std::cout << vd;
    std::println("\nvd[-8] --> out of range: {}", vd[-8]); // clamped to first element
    std::println("\nvd[12] --> out of range: {}", vd[12]); // clamped to last element
    std::println("vd[12] = 99.99");
    vd[12] = 99.99; // clamped to last element
    std::println("vd[2]: {}", vd[2]);

    Vector<double> vd3;
    std::cout << vd;
    vd3 = vd;
    std::cout << vd3;

    Vector<Point, 2> vpt = {Point(0.0, 0.0, "default")};
    Vector<Point, 2> vpt2 = {Point(1.0, 2.0, "other")};
    std::cout << vpt;
    vpt = vpt2;
    std::cout << vpt;

    // Class Template Argument Deduction (C++17)
    // No need to specify template arguments if deducible
    Vector vpt3(vpt2);
    std::cout << vpt3;

    std::println("");

    return 0;
}
```
<!-- SNIPPET:END -->
