---
title: "3. Surcharge des opérateurs"
type: docs
weight: 10
---

# Chapitre 3 : surcharge des opérateurs

## Slides

{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/03_Surcharge_des_operateurs.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/03_Surcharge_des_operateurs.html?print-pdf)

## Exemples

{{<details "1242.2_03.01_AdditionOverload" >}}
**`Complex.h`**
<!-- SNIPPET:BEGIN source_file=Complex.h id=1242.2_Examples_03.01_AdditionOverload_Complex.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Complex
{
public:
  Complex() = default;
  // No explicit as we want implicit conversion for operator+
  Complex(int n) : m_r(n), m_i(0) {}
  Complex(double r, double i) : m_r(r), m_i(i) {}

  double getR() const {return m_r;}
  double getI() const {return m_i;}
  
  // operator+ as an external overload: both operands are treated the same
  // friend so that it can access private members of Complex
  friend Complex operator+(const Complex &c1, const Complex &c2);

  void show() const;

private:

  double m_r{0};
  double m_i{0};
};
```
<!-- SNIPPET:END -->

**`Complex.cpp`**
<!-- SNIPPET:BEGIN source_file=Complex.cpp id=1242.2_Examples_03.01_AdditionOverload_Complex.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// External overload: both operands are treated symmetrically,
// so implicit conversion applies to either side.
Complex operator+(const Complex &c1, const Complex &c2)
{
  return Complex(c1.m_r + c2.m_r, c1.m_i + c2.m_i);
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_03.01_AdditionOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Complex.h"

#include <print>

int main()
{
  Complex c1(3., -5.), c2(7., 1.), cSum;
  std::print("c1 = ");
  c1.show();
  std::print("c2 = ");
  c2.show();

  cSum = c1 + c2;
  std::print("c1 + c2 = ");
  cSum.show();

  // int is implicitly converted to Complex
  int value = 99;
  cSum = c1 + value;
  std::print("c1 + value = ");
  cSum.show();

  // Only possible with an EXTERNAL overload: conversion applies to the lhs too
  cSum = value + c2;
  std::print("value + c2 = ");
  cSum.show();

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_03.02_AssignmentOverload" >}}
**`NamedPoint.h`**
<!-- SNIPPET:BEGIN source_file=NamedPoint.h id=1242.2_Examples_03.02_AssignmentOverload_NamedPoint.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class NamedPoint
{
public:
  NamedPoint(int x=0, int y=0, const char *name = "?");
  NamedPoint(const NamedPoint &p);
  virtual ~NamedPoint();

  NamedPoint &operator=(const NamedPoint &p);

  void show() const;
  void setName(const char *newName);

private:
  int m_x{0};
  int m_y{0};
  char *m_name{nullptr};
};
```
<!-- SNIPPET:END -->

**`NamedPoint.cpp`**
<!-- SNIPPET:BEGIN source_file=NamedPoint.cpp id=1242.2_Examples_03.02_AssignmentOverload_NamedPoint.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "NamedPoint.h"

#include <print>
#include <cstring>

NamedPoint::NamedPoint(int x, int y, const char *name)
    : m_x(x), m_y(y)
{
  m_name = new char[strlen(name) + 1];
  strcpy_s(m_name, strlen(name) + 1, name);
}

NamedPoint::NamedPoint(const NamedPoint &p)
    : m_x(p.m_x), m_y(p.m_y)
{
  m_name = new char[strlen(p.m_name) + 1];
  strcpy_s(m_name, strlen(p.m_name) + 1, p.m_name);
}

NamedPoint::~NamedPoint()
{
  delete[] m_name;
  m_name = nullptr;
}

// Warning: the self-assignment guard prevents freeing memory we are about to read
NamedPoint &NamedPoint::operator=(const NamedPoint &p)
{
  // Self-assignment guard
  if (this == &p)
  {
    return *this;
  }

  m_x = p.m_x;
  m_y = p.m_y;
  delete[] m_name;
  m_name = nullptr;
  m_name = new char[strlen(p.m_name) + 1];
  strcpy_s(m_name, strlen(p.m_name) + 1, p.m_name);

  return *this;
}

void NamedPoint::show() const
{
  std::println("{}: ({}, {})", m_name, m_x, m_y);
}

void NamedPoint::setName(const char *newName)
{
  delete[] m_name;
  m_name = nullptr;
  m_name = new char[strlen(newName) + 1];
  strcpy_s(m_name, strlen(newName) + 1, newName);
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_03.02_AssignmentOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "NamedPoint.h"

int main()
{
    NamedPoint pt1(1, 4, "Pt1");

    NamedPoint copyPt = pt1;
    NamedPoint copyPt2;
    copyPt2 = pt1;

    copyPt.setName("copyPt");
    copyPt2.setName("copyPt2");

    pt1.show();
    copyPt.show();
    copyPt2.show();

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_03.03_StreamOperatorsOverload" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Examples_03.03_StreamOperatorsOverload_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Point
{
public:
  Point();

  // Allows implicit conversion from int
  Point(int a);
  Point(int x, int y);
  Point(const Point &p);

  Point &operator=(const Point &p);

  friend Point operator+(const Point &p, const Point &q);
  friend std::ostream &operator<<(std::ostream &s, const Point &p);
  friend std::istream &operator>>(std::istream &in, Point &p);

private:
  int m_x{0};
  int m_y{0};
};
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Examples_03.03_StreamOperatorsOverload_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

// Full definitions
#include <iostream>
#include <print>

Point::Point() : m_x(0), m_y(0) {}

Point::Point(int a) : m_x(a), m_y(a) {}

Point::Point(int x, int y) : m_x(x), m_y(y) {}

Point::Point(const Point &p) : m_x(p.m_x), m_y(p.m_y) {}

Point &Point::operator=(const Point &p)
{
  if (this != &p)
  {
    m_x = p.m_x;
    m_y = p.m_y;
  }

  return *this;
}

Point operator+(const Point &p, const Point &q)
{
  return Point(p.m_x + q.m_x, p.m_y + q.m_y);
}

// Returns the stream to support chaining: cout << p1 << p2
std::ostream &operator<<(std::ostream &s, const Point &p)
{
  return s << '(' << p.m_x << ',' << p.m_y << ')';
}

// Reads a Point in the format (x,y)
// Returns the stream to support chaining: cin >> p1 >> p2
std::istream &operator>>(std::istream &in, Point &p)
{
  char c;
  in >> c;
  if (c == '(')
  {
    in >> p.m_x >> c;
    if (c == ',')
    {
      in >> p.m_y >> c;
      if (c == ')')
        return in;
    }
  }

  std::println(stderr, "Read error: expected format (x,y)");
  in.setstate(std::ios::failbit);
  return in;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_03.03_StreamOperatorsOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

#include <iostream>
#include <print>

int main()
{
    std::println("1. INSERTION (<<) and EXTRACTION (>>) OPERATORS");
    Point p1;
    std::print("Enter a point in format (x,y): ");
    std::cin >> p1;
    std::cout << "\nPoint entered: " << p1 << '\n';  // uses operator<<

    std::println("\nPoint p2 = Point(2)");
    Point p2 = Point(2);
    std::cout << "p2 = " << p2 << '\n';

    std::println("\n2. ADDITION OPERATOR  +");
    std::println("Point r = 5 + p1 + p2;");
    Point r = 5 + p1 + p2;  // 5 is implicitly converted via Point(int)
    std::cout << "r = " << r << '\n';

    // operator<< returns a reference, enabling chaining
    std::print("\nr, p1, p2 chained: ");
    std::cout << r << p1 << p2 << '\n';

    std::println("\n3. ASSIGNMENT OPERATOR  =");
    std::println("r = p1 = p2;");
    r = p1 = p2;  // r.operator=(p1.operator=(p2))
    std::cout << r << p1 << p2 << '\n';

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_03.04_IncrementOverload" >}}
**`Counter.h`**
<!-- SNIPPET:BEGIN source_file=Counter.h id=1242.2_Examples_03.04_IncrementOverload_Counter.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Counter
{
public:
    Counter() = default;
    // Should be explicit but not here on purpose
    Counter(int x);

    Counter& operator++();
    Counter operator++(int);

    friend std::ostream& operator<<(std::ostream& o, const Counter& c);

private:
    int m_x{0};
};
```
<!-- SNIPPET:END -->

**`Counter.cpp`**
<!-- SNIPPET:BEGIN source_file=Counter.cpp id=1242.2_Examples_03.04_IncrementOverload_Counter.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Counter.h"

#include <iostream>

Counter::Counter(int x) : m_x(x) {}

// Returns a reference: no copy, and can be used as an lvalue (++x = 5 is valid)
Counter& Counter::operator++()
{
    ++m_x;
    return *this;
}

// The dummy int parameter distinguishes post from pre at the call site.
// Returns a copy of the state before increment — cannot be used as an lvalue.
Counter Counter::operator++(int)
{
    Counter temp(*this);
    ++m_x;
    return temp;
}

std::ostream& operator<<(std::ostream& o, const Counter& c)
{
    return o << c.m_x;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_03.04_IncrementOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Counter.h"

#include <iostream>

int main()
{
  Counter x = 10;
  std::cout << "x: " << x << '\n';
  x++;
  std::cout << "After x++: " << x << '\n';

  std::cout << "\nx: " << x << '\n';
  ++x;
  std::cout << "After ++x: " << x << '\n';

  std::cout << "\nx: " << x << '\n';
  Counter a = ++x; // pre-increment: a gets the incremented value
  std::cout << "After Counter a = ++x  =>  x: " << x << "   a: " << a << '\n';

  std::cout << "\nx: " << x << '\n';
  Counter b = x++; // post-increment: b gets the value before increment
  std::cout << "After Counter b = x++  =>  x: " << x << "   b: " << b << '\n';

  // Valid but bad practice: the increment is immediately overwritten by the assignment.
  // Avoid this in real code — it is confusing and serves no practical purpose.
  ++x = 5;
  std::cout << "\n++x = 5  (unusual but valid for pre-increment)" << '\n';
  std::cout << "x = " << x << '\n';

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_03.05_ConversionOverload" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Examples_03.05_ConversionOverload_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Point
{
public:
  Point(int a);

  void show() const;

  operator int() const;
  operator double() const;

private:
  int m_x{0};
  int m_y{0};
};
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Examples_03.05_ConversionOverload_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

#include <cstdlib>
#include <print>

Point::Point(int a) : m_x(a), m_y(0) {}

void Point::show() const
{
  std::println("({}, {})", m_x, m_y);
}

// Conversion from Point to int: Manhattan distance from origin
Point::operator int() const { return std::abs(m_x) + std::abs(m_y); }

// Conversion from Point to double: same with a fractional marker
Point::operator double() const { return std::abs(m_x) + std::abs(m_y) + 0.01; }
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_03.05_ConversionOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

#include <print>

int main()
{
  Point pt(3);
  std::print("pt = ");
  pt.show();

  int n = static_cast<int>(pt);
  std::println("(int)pt = {}", n);

  double d = static_cast<double>(pt);
  std::println("(double)pt = {}", d);

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_03.06_FunctorOverload" >}}
**`Linear.h`**
<!-- SNIPPET:BEGIN source_file=Linear.h id=1242.2_Examples_03.06_FunctorOverload_Linear.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Linear
{
public:
  Linear(double a, double b);

  double operator()(double x) const;

private:
  double m_a{0};
  double m_b{0};
};
```
<!-- SNIPPET:END -->

**`Linear.cpp`**
<!-- SNIPPET:BEGIN source_file=Linear.cpp id=1242.2_Examples_03.06_FunctorOverload_Linear.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Linear.h"

Linear::Linear(double a, double b) : m_a(a), m_b(b) {}

double Linear::operator()(double x) const
{
  return m_a * x + m_b;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_03.06_FunctorOverload_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Linear.h"

#include <print>

int main()
{
  Linear f(2, 1);  // f(x) = 2x + 1
  Linear g(-1, 0); // g(x) = -x

  std::println("f(x) = 2x + 1,  g(x) = -x");
  std::println("f(4) = {}", f(4));
  std::println("g(7) = {}", g(7));

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_03.07_OperatorsOverloadMisc" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Examples_03.07_OperatorsOverloadMisc_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#pragma once

class Point
{
public:
  Point() = default;
  virtual ~Point() = default;
  Point &operator=(const Point &) = default;

  Point operator+(const Point &p) const
  {
    Point temp;
    temp.m_x = m_x + p.m_x;
    temp.m_y = m_y + p.m_y;
    return temp;
  }

  friend Point operator+(const Point& self, const Point& other);

private:
  int m_x{0};
  int m_y{0};
};

Point operator+(const Point &self, const Point &other);
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Examples_03.07_OperatorsOverloadMisc_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

Point operator+(const Point &self, const Point &other)
{
  Point temp(self);
  temp.m_x += other.m_x;
  temp.m_y += other.m_y;
  return temp;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_03.07_OperatorsOverloadMisc_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

#include <print>

int main()
{
  Point p1;
  Point p2;

  // GCC - error: ambiguous overload for 'operator+' (operand types are 'Point' and 'Point')
  // auto p4 = p1 + p2;

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 3.1

### Exercice 1 : classe **`Time`** surcharge 
Reprendre la classe **`Time`** de l'exercice 2 de la série 2.1, et :

1. surcharger l'opérateur d'insertion de flux **`operator<<()`** afin de pouvoir afficher un temps  **`std::cout << t << std::  endl;`**
2. surcharger l'opérateur d'affectation **`operator=()`**
3. surcharger les opérateurs arithmétiques :
   1. l’opérateur **`+`** doit être implémenté par une fonction non membre de la classe et amie
   2. l’opérateur **`-`** doit être implémenté par une fonction membre de la classe.
   Est-ce que toutes les utilisations proposées dans le `main()` sont possibles ? 
   Laquelle de ces deux opérations est commutative ?
4. surcharger les opérateurs relationnels
   1. de manière explicite, implémenter :
      1.  l' **`operator==()`** avec des opérateurs logiques
      2.  l' **`operator<()`** en comparant la valeur renvoyée par une méthode privée **`evaluate()`** qui retourne heure*60+minute
   2. en se basant sur ces deux opérateurs, implémenter :
      1. **`operator>=()`**
      2. **`operator<=()`** 
      3. **`operator!=()`**

5. surchargez les méthodes d'incrémentation préfixée et postfixée   
6. implémentez l'opérateur d'insertion de flux, capable de lire un temps sous la forme : 4:45

{{< plantuml id="chap3_exo1.1">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
hide circle

class Time {
    - hour : int
    - minute : int

+ Time()
+ Time(Int, Int)
+ Time(Int)

+ operator = ( const Time& ) : Time& 

<<friend>> operator + (const Time&, const Time&) : Time
+ operator - (const Time&): Time

- evaluate() : int

+ operator == ( const Time& ) : Boolean {query}
+ operator <  ( const Time& ) : Boolean {query}
+ operator >= ( const Time& ) : Boolean {query}
+ operator <= ( const Time& ) : Boolean {query}
+ operator != ( const Time& ) : Boolean {query}

+ operator ++ ()    : Time& 
+ operator ++ (Int) : Time 

<<friend>> operator<<(ostream&,  const Time&): ostream& 
<<friend>> operator>>(istream&,  Time&) : istream& 

} 
@enduml
{{< /plantuml >}}

**Exemple de `main()`**

{{<details "1242.2_03.01_OverloadingTime" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_03.01_OverloadingTime_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Time.h"

#include <iostream>

int main()
{
  // Constructors
  std::cout << "Time t1 (default): ";
  Time t1;
  std::cout << t1 << '\n';

  std::cout << "Time t2(10, 9):    ";
  Time t2(10, 9);
  std::cout << t2 << '\n';

  std::cout << "Time t3(17.75):    ";
  Time t3(17.75);
  std::cout << t3 << '\n';

  // Setters
  std::cout << "\nt2.setHour(7):      ";
  t2.setHour(7);
  std::cout << t2 << '\n';

  std::cout << "t2.setMinute(-40):  ";
  t2.setMinute(-40); // negative -> clamped to 0
  std::cout << t2 << '\n';

  std::cout << "t2.setMinute(86):   ";
  t2.setMinute(86); // 86 % 60 = 26 min, +1 hour
  std::cout << t2 << '\n';

  // operator=
  std::cout << "\nt1 = t2:  ";
  t1 = t2;
  std::cout << "t1=" << t1 << "  t2=" << t2 << '\n';

  // operator+ (non-member friend)
  t1.setMinute(0);
  std::cout << "\nt1=" << t1 << "  t3=" << t3 << '\n';
  std::cout << "t1 = t1 + t3: ";
  t1 = t1 + t3;
  std::cout << t1 << '\n';

  std::cout << "t3 = t3 + 4:  ";
  t3 = t3 + 4; // implicit conversion: 4 -> Time(4.0)
  std::cout << t3 << '\n';

  std::cout << "t3 = 4 + t3:  ";
  t3 = 4 + t3;
  std::cout << t3 << '\n';

  // operator- (member)
  std::cout << "\nt1=" << t1 << "  t3=" << t3 << '\n';
  std::cout << "t1 = t1 - t3: ";
  t1 = t1 - t3;
  std::cout << t1 << '\n';

  std::cout << "t3 = t3 - 1:  ";
  t3 = t3 - 1;
  std::cout << t3 << '\n';

  // t3 = 1 - t3 // ???

  // Comparison operators
  std::cout << '\n';
  std::cout << t1 << " == " << t1 << std::boolalpha << " : " << (t1 == t1) << '\n';
  std::cout << t1 << " == " << t2 << std::boolalpha << " : " << (t1 == t2) << '\n';
  std::cout << t1 << " <  " << t1 << std::boolalpha << " : " << (t1 < t1) << '\n';
  std::cout << t1 << " <  " << t2 << std::boolalpha << " : " << (t1 < t2) << '\n';
  std::cout << t1 << " >= " << t1 << std::boolalpha << " : " << (t1 >= t1) << '\n';
  std::cout << t1 << " >= " << t2 << std::boolalpha << " : " << (t1 >= t2) << '\n';
  std::cout << t1 << " != " << t1 << std::boolalpha << " : " << (t1 != t1) << '\n';
  std::cout << t1 << " != " << t2 << std::boolalpha << " : " << (t1 != t2) << '\n';

  // Increment operators
  std::cout << "\nt2=" << t2 << "  t3=" << t3 << '\n';
  std::cout << "t2 = t3++: ";
  t2 = t3++;
  std::cout << "t2=" << t2 << "  t3=" << t3 << '\n';

  std::cout << "t2 = ++t3: ";
  t2 = ++t3;
  std::cout << "t2=" << t2 << "  t3=" << t3 << '\n';

  // operator>>
  std::cout << "\nEnter a time (hh:mm): ";
  std::cin >> t2;
  std::cout << "t2: " << t2 << '\n';

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Serie 3.2 : surcharge des opérateurs

### Exercice 1 : classe Vecteur, surcharge de <<, =, et []
Implémenter une classe de vecteurs dynamique, dans le sens où les constructeurs doivent allouer dynamiquement la mémoire nécessaire.
Les éléments sont de type **`double`**. En particulier, il faut :
1. implémenter les constructeurs :
   1. par défaut (pas d'allocation)
   2. standard (le premier argument définit la taille et le second le contenu; par défaut le contenu est nul)
   3. par recopie 
2. surcharger les opérateurs suivants :
   1. insertion de flux  **`operator<<()`**
   2. affectation  **`operator=()`**. Il faut faire une copie en profondeur
   3. addition **`operator+()`**. À déclarer comme fonction amie
   4. accès  **`operator[]()`**. Il doit permettre :
      * de lire un élément du vecteur **`x=v[4];`**
      * de modifier un élément. **`v[4]=4;`**
  
      Si l'indice est hors du vecteur, l'operateur utilise la première case du vecteur **`v[0]`**.

**Exemple de `main()`**

{{<details "1242.2_03.02_OverloadingVector" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_03.02_OverloadingVector_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Vector.h"

#include <iostream>

int main()
{
    Vector v1;
    Vector v2(3);
    Vector v3 = Vector(3, 10);
    std::cout << "v1: " << v1 << "  v2: " << v2 << "  v3: " << v3 << "\n\n";

    // operator=
    std::cout << "v1: " << v1 << "  v3: " << v3 << '\n';
    std::cout << "v1 = v3;\n";
    v1 = v3;
    std::cout << "v1: " << v1 << "  v3: " << v3 << "\n\n";

    // operator[] — write
    std::cout << "v1: " << v1 << '\n';
    std::cout << "v1[2] = 100;\n";
    v1[2] = 100;
    std::cout << "v1: " << v1 << "\n\n";

    // operator[] — read
    std::cout << "v1[2] = " << v1[2] << '\n';
    std::cout << "v3[2] = " << v3[2] << "\n\n";

    // operator[] — out of bounds falls back to v[0]
    std::cout << "v1: " << v1 << '\n';
    std::cout << "v1[1000] = 200;\n";
    v1[1000] = 200;
    std::cout << "v1: " << v1 << "\n\n";

    // operator+ (non-member friend)
    Vector v4(5, 5);
    std::cout << "v1: " << v1 << "  v3: " << v3 << "  v4: " << v4 << '\n';
    std::cout << "v1 = v3 + v4;\n";
    v1 = v3 + v4;
    std::cout << "v1: " << v1 << "  v3: " << v3 << "  v4: " << v4 << "\n\n";

    std::cout << "v1: " << v1 << "  v2: " << v2 << "  v3: " << v3 << '\n';
    std::cout << "v1 = v3 + v3;\n";
    v1 = v3 + v3;
    std::cout << "v1: " << v1 << "  v2: " << v2 << "  v3: " << v3 << '\n';

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Solutions

<!-- [Serie3_1_SOLUTIONS](/zips/Serie3_1_SOLUTIONS.zip) -->

