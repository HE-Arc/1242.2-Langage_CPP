---
title: "2. Des classes et des objets — Solutions"
type: docs
weight: 10
draft: false
---

# Chapitre 2 : des classes et des objets — Solutions

## Série 2.1

### Exercice 1 : classe compte bancaire

<!-- SNIPPET:BEGIN source_file=BankAccount.h id=1242.2_Exercises_02.01_BankAccount_BankAccount.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
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
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=BankAccount.cpp id=1242.2_Exercises_02.01_BankAccount_BankAccount.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
void BankAccount::deposit(double amount)
{
    if (amount > 0)
    {
      m_balance += amount;
    }
}

void BankAccount::withdraw(double amount)
{
    if (amount > 0 && m_balance >= amount)
    {
        m_balance -= amount;
    }
}

void BankAccount::show() const
{
    std::println("The amount on your bank account is : {:.2f}", m_balance);
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_02.01_BankAccount_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

#include "BankAccount.h"

int main()
{
  BankAccount myBankAccount;
  myBankAccount.show();

  // Impossible
  myBankAccount.withdraw(100);
  myBankAccount.show();
  myBankAccount.deposit(100);
  myBankAccount.show();
  // Impossible
  myBankAccount.withdraw(200);
  myBankAccount.show();
  // OK
  myBankAccount.withdraw(20);
  myBankAccount.show();

  BankAccount mySavings = myBankAccount;
  mySavings.show();
  myBankAccount.show();
}
```
<!-- SNIPPET:END -->

### Exercice 2 : classe Time

<!-- SNIPPET:BEGIN source_file=Time.h id=1242.2_Exercises_02.02_Time_Time.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Time
{
public:
    Time();
    Time(int hour, int minute);
    explicit Time(double realTime);
    virtual ~Time() = default;

    int getHour() const { return m_hour; }
    int getMinute() const { return m_minute; }

    // Not inlined because they involve validation logic
    void setHour(int hour);
    void setMinute(int minute);

    void show() const;

private:
    int m_hour{12};
    int m_minute{0};

    static constexpr int m_hours_per_day{24};
    static constexpr int m_minutes_per_hour{60};
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Time.cpp id=1242.2_Exercises_02.02_Time_Time.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
Time::Time()
{
  std::println("  -> Default constructor");
}

Time::Time(int hour, int minute) : m_hour(hour),
                                   m_minute(minute)
{
  std::println("  -> Standard constructor");
}

Time::Time(double decimalTime) : m_hour(static_cast<int>(decimalTime)),
                                 m_minute(static_cast<int>((decimalTime - m_hour) * 60))
{
  std::println("  -> Conversion constructor");
}

void Time::setHour(int hour)
{
  m_hour = (hour >= 0) ? hour % m_hours_per_day : 0;
}

void Time::setMinute(int minute)
{
  if (minute >= 0)
  {
    m_minute = minute % m_minutes_per_hour;
    setHour(m_hour + minute / m_minutes_per_hour); // carry over to hours
  }
  else
  {
    m_minute = 0;
  }
}

void Time::show() const
{
  std::println("{:02d}H{:02d}", m_hour, m_minute);
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_02.02_Time_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include "Time.h"

int main()
{
	std::print("Time t1; ");
	Time t1;
	t1.show(); //-> t1: 12H00

	std::print("Time t2(10,9); ");
	Time t2(10, 9);
	t2.show();      //-> t2: 10H09

	std::print("Time t3(17.75); ");
	Time t3(17.75);
	t3.show();      //-> t3: 17H45

	std::print("t2.setHour(23); ");
	t2.setHour(23);
	t2.show(); //-> t2: 23H09

	std::print("t2.setMinute(-40); ");
	t2.setMinute(-40);
	t2.show();         //-> t2: 23H00

	std::print("t2.setMinute(86); ");
	t2.setMinute(86);
	t2.show();        //-> t2: 00H26

  t2.setMinute(t2.getMinute() + 5);
  std::print("t2.setMinute(t2.getMinute() + 5); ");

	return 0;
}
```
<!-- SNIPPET:END -->

### Exercice 3 : classe Point

<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_02.03_Point_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Point
{
public:
    explicit Point(char label, double x = 0, double y = 0);
    Point(const Point&);
    virtual ~Point() = default;

    void show() const;
    void translate(double dx, double dy);

private:
    double m_x{0.};
    double m_y{0.};
    char m_label{'?'};
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_02.03_Point_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
Point::Point(char label, double x, double y) : m_x(x), m_y(y), m_label(label)
{
  std::println("[Standard constructor]");
}

Point::Point(const Point &other) : m_x(other.m_x), m_y(other.m_y), m_label(other.m_label)
{
  std::println("[Copy constructor]");
}

void Point::show() const
{
  std::print("\n{} : ({:.2f},{:.2f})", m_label, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
  m_x += dx;
  m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_02.03_Point_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

#include <print>
#include <iostream>
#include <cmath>
#include <numbers>

// OPTIONAL exercise
Point **generatePolygon(int n);

int main()
{
  std::println("\nPoint p1('B');");
  Point p1('B');
  p1.show();

  std::println("\nPoint p2('A', 3, 4);");
  Point p2('A', 3, 4);
  p2.show();

  std::println("\np2.translate(-12,7);");
  p2.translate(-12, 7);
  p2.show();

  std::println("\n\nDYNAMIC ALLOCATION");
  std::println("==================");
  Point *ptrPt3 = new Point('D', 10, -5);
  ptrPt3->show();
  delete ptrPt3;
  ptrPt3 = nullptr;

  int N = 4;
  std::print("\nHow many points do you want the polygon to have ? ");
  std::cin >> N;

  if (N > 2)
  {
    Point **polygonPoints = generatePolygon(N);
    std::println("\nPOLYGON {} points:", N);
    for (int i = 0; i < N; i++)
    {
      polygonPoints[i]->show();
    }
    for (int i = 0; i < N; i++)
    {
      delete polygonPoints[i];
      polygonPoints[i] = nullptr;
    }
    delete[] polygonPoints;
    polygonPoints = nullptr;
  }
  else
  {
    std::println("that is IMPOSSIBLE !");
  }

  std::println();
}

Point **generatePolygon(int n)
{
  Point **polygonPoints = new Point *[n];
  for (int i = 0; i < n; ++i)
  {
    double angle = (static_cast<double>(i) / n) * 2 * std::numbers::pi;
    polygonPoints[i] = new Point('A' + char(i), std::cos(angle), std::sin(angle));
  }
  return polygonPoints;
}
```
<!-- SNIPPET:END -->

## Série 2.2

### Exercice 1 : classe Point améliorée

<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_02.04_PointStatic_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Point
{
public:
  Point();
  // Could be a conversion constructor
  explicit Point(char name, double x=0, double y=0);
  Point(const Point &);

  virtual ~Point(){--m_counter;}

  void show() const;
  void translate(double dx, double dy);

  static int getCounter(){return m_counter;}

private:
  double m_x{0.};
  double m_y{0.};
  char m_label{'?'};

  static int m_counter;
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_02.04_PointStatic_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::m_counter = 0;

Point::Point() : m_x(0.), m_y(0.), m_label('?')
{
  std::println("[Default constructor]");
  ++m_counter;
}

Point::Point(char name, double x, double y) : m_x(x), m_y(y), m_label(name)
{
  std::println("[Standard constructor]");
  ++m_counter;
}

Point::Point(const Point &other) : m_x(other.m_x), m_y(other.m_y), m_label(other.m_label)
{
  std::println("[Copy constructor]");
  ++m_counter;
}

void Point::show() const
{
  std::print("\n{} : ({},{})", m_label, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
  m_x += dx;
  m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_02.04_PointStatic_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

#include <print>

int main()
{
  Point *ptrPoint = nullptr;
  {
    Point p1('A');
    Point p2('B', 3, 4);
    std::println("Point count (2): {}", Point::getCounter());

    ptrPoint = new Point('D', 10, -5);
    std::println("Point count (3): {}", Point::getCounter());
  } // p1 and p2 are destroyed here

  std::println("Point count (1): {}", Point::getCounter());

  delete ptrPoint;
  ptrPoint = nullptr;
  std::println("Point count (0): {}", Point::getCounter());
}
```
<!-- SNIPPET:END -->

### Exercice 2 : classe Rectangle (composition de points)

<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_02.05_Rectangle_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Point
{
public:
  explicit Point(char label, double x=0, double y=0);
  Point(const Point &);

  virtual ~Point(){--m_counter;}

  void show() const;
  void translate(double dx, double dy);

  static int getCounter(){return m_counter;}

private:
  double m_x{0.};
  double m_y{0.};
  char m_label{'?'};

  static int m_counter;

  friend class Rectangle;
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_02.05_Rectangle_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::m_counter = 0;

Point::Point(char label, double x, double y) : m_x(x), m_y(y), m_label(label)
{
  std::println("[ctor] Point(char, double, double)");
  ++m_counter;
}

Point::Point(const Point &other) : m_x(other.m_x), m_y(other.m_y), m_label(other.m_label)
{
  std::println("[ctor] Point(const Point&)");
  ++m_counter;
}

void Point::show() const
{
  std::print("{} : ({},{})", m_label, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
  m_x += dx;
  m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Rectangle.h id=1242.2_Exercises_02.05_Rectangle_Rectangle.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

class Rectangle
{
public:
  // Could be a conversion constructor
  explicit Rectangle(double xLL=0, double yLL=0, double xUR=0, double yUR=0);
  // Passing by const ref avoids constructing extra Point copies
  Rectangle(const Point &cornerLL, const Point &cornerUR);
  virtual ~Rectangle() = default;

  bool contains(const Point &) const;
  double getPerimeter() const;
  void show() const;
  void translate(double dx, double dy);

private:
  Point m_cornerLL;
  Point m_cornerUR;
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Rectangle.cpp id=1242.2_Exercises_02.05_Rectangle_Rectangle.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Initializer list required: Point has no default constructor
Rectangle::Rectangle(const Point &p1, const Point &p2) : m_cornerLL(p1), m_cornerUR(p2)
{
  std::println("[ctor] Rectangle(const Point&, const Point&)");
}

Rectangle::Rectangle(double xLL, double yLL, double xUR, double yUR) : m_cornerLL('A', xLL, yLL), m_cornerUR('B', xUR, yUR)
{
  std::println("[ctor] Rectangle(double, double, double, double)");
}

bool Rectangle::contains(const Point &p) const
{
  return (p.m_x >= m_cornerLL.m_x && p.m_x <= m_cornerUR.m_x &&
          p.m_y >= m_cornerLL.m_y && p.m_y <= m_cornerUR.m_y);
}

double Rectangle::getPerimeter() const
{
  double width = m_cornerUR.m_x - m_cornerLL.m_x;
  double height = m_cornerUR.m_y - m_cornerLL.m_y;
  return 2 * (width + height);
}

void Rectangle::show() const
{
  std::print("[");
  m_cornerLL.show();
  std::print("  -  ");
  m_cornerUR.show();
  std::println("]  Perimeter: {}", getPerimeter());
}

void Rectangle::translate(double dx, double dy)
{
  m_cornerLL.m_x += dx;
  m_cornerUR.m_x += dx;
  m_cornerLL.m_y += dy;
  m_cornerUR.m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_02.05_Rectangle_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"
#include "Rectangle.h"

#include <print>

int main()
{
  std::println("*** POINTS CONSTRUCTION ***");
  Point pt1('A', 5., 5.), pt2('B', 10., 12.), ptX('X', 7., 8.);

  std::println("*** R CONSTRUCTION (from 2 points) ***");
  Rectangle R(pt1, pt2); // 2 calls to the Point copy constructor

  std::println("*** R2 CONSTRUCTION (from coordinates) ***");
  Rectangle R2(1, 2, 3, 4);
  std::println("---");

  R.show();
  std::println("Perimeter: {}", R.getPerimeter());
  std::print("is ptX ");
  ptX.show();
  std::println(" contained in R ? {}", R.contains(ptX));

  pt1.translate(3, 5);
  R.show(); // R is unchanged: constructor copied pt1 and pt2 by value

  std::println("*** COPY CONSTRUCTION ***");
  Rectangle anotherRectangle(R);
  R.translate(-10., -15.);
  std::println("R after translate(-10,-15):");
  R.show();
  std::println("anotherRectangle (independent copy):");
  anotherRectangle.show();
}
```
<!-- SNIPPET:END -->

### Exercice 3 : classe RectangleAgreg (agrégation de points)

<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_02.06_RectangleAgreg_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Point
{
public:
  // Could be a conversion constructor
  explicit Point(char label, double x=0, double y=0);
  Point(const Point &);
  virtual ~Point(){--m_counter;}

  void show() const;
  void translate(double dx, double dy);

  static int getCounter(){return m_counter;}

private:
  double m_x{0.};
  double m_y{0.};
  char m_label{'?'};

  static int m_counter;

  friend class RectangleAgreg;
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_02.06_RectangleAgreg_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::m_counter = 0;

Point::Point(char label, double x, double y) : m_x(x), m_y(y), m_label(label)
{
  std::println("[ctor] Point(char, double, double)");
  ++m_counter;
}

Point::Point(const Point &other) : m_x(other.m_x), m_y(other.m_y), m_label(other.m_label)
{
  std::println("[ctor] Point(const Point&)");
  ++m_counter;
}

void Point::show() const
{
  std::print("{} : ({},{})", m_label, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
  m_x += dx;
  m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=RectangleAgreg.h id=1242.2_Exercises_02.06_RectangleAgreg_RectangleAgreg.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

class RectangleAgreg
{
public:
  RectangleAgreg(Point *ptrLL, Point *ptrUR);
  RectangleAgreg(const RectangleAgreg &other);

  virtual ~RectangleAgreg();

  double getPerimeter() const;
  void show() const;
  void translate(double dx, double dy);

private:
  Point *m_cornerLL{nullptr};
  Point *m_cornerUR{nullptr};
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=RectangleAgreg.cpp id=1242.2_Exercises_02.06_RectangleAgreg_RectangleAgreg.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Shallow copy
RectangleAgreg::RectangleAgreg(Point *ptrLL, Point *ptrUR)
    : m_cornerLL(ptrLL), m_cornerUR(ptrUR)
{
}

// Shallow copy
RectangleAgreg::RectangleAgreg(const RectangleAgreg &other)
    : m_cornerLL(other.m_cornerLL), m_cornerUR(other.m_cornerUR)
{
}

RectangleAgreg::~RectangleAgreg()
{
  // Do not delete the points
  m_cornerLL = nullptr;
  m_cornerUR = nullptr;
}

void RectangleAgreg::show() const
{
  std::print("[");
  m_cornerLL->show();
  std::print(" - ");
  m_cornerUR->show();
  std::println("]");
}

double RectangleAgreg::getPerimeter() const
{
  return 2 * (m_cornerUR->m_x - m_cornerLL->m_x + m_cornerUR->m_y - m_cornerLL->m_y);
}

void RectangleAgreg::translate(double dx, double dy)
{
  m_cornerLL->m_x += dx;
  m_cornerUR->m_x += dx;
  m_cornerLL->m_y += dy;
  m_cornerUR->m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_02.06_RectangleAgreg_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"
#include "RectangleAgreg.h"

#include <print>

int main()
{
  Point pt1('A', 5, 5), pt2('B', 10, 12);

  RectangleAgreg R(&pt1, &pt2);
  std::print("R before translation: ");
  R.show();
  pt1.translate(3, 5);
  std::print("R after translating pt1: ");
  R.show();

  RectangleAgreg copyR(R);
  std::print("copyR before translation: ");
  copyR.show();
  R.translate(-5, -5);
  std::print("R after translation: ");
  R.show();
  std::print("copyR after translating R: ");
  copyR.show();
}
```
<!-- SNIPPET:END -->

### Exercice 4 : classe RectangleComp (composition de points avec copie en profondeur)

<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_02.07_RectangleComp_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Point
{
public:
  // Could be a conversion constructor
  explicit Point(char label, double x=0, double y=0);
  Point(const Point &);
  virtual ~Point(){--m_counter;}

  void show() const;
  void translate(double dx, double dy);

  static int getCounter(){return m_counter;}

private:
  double m_x{0.};
  double m_y{0.};
  char m_label{'?'};

  static int m_counter;

  friend class RectangleComp;
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_02.07_RectangleComp_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::m_counter = 0;

Point::Point(char label, double x, double y) : m_x(x), m_y(y), m_label(label)
{
  std::println("[ctor] Point(char, double, double)");
  ++m_counter;
}

Point::Point(const Point &other) : m_x(other.m_x), m_y(other.m_y), m_label(other.m_label)
{
  std::println("[ctor] Point(const Point&)");
  ++m_counter;
}

void Point::show() const
{
  std::print("{} : ({},{})", m_label, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
  m_x += dx;
  m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=RectangleComp.h id=1242.2_Exercises_02.07_RectangleComp_RectangleComp.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

class RectangleComp
{
public:
  RectangleComp(Point *ptrLL, Point *ptrUR);
  RectangleComp(const RectangleComp &other);

  virtual ~RectangleComp();

  double getPerimeter() const;
  void show() const;
  void translate(double dx, double dy);

private:
  Point *m_cornerLL{nullptr};
  Point *m_cornerUR{nullptr};
};
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=RectangleComp.cpp id=1242.2_Exercises_02.07_RectangleComp_RectangleComp.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Deep copy
RectangleComp::RectangleComp(Point *ptrLL, Point *ptrUR)
    : m_cornerLL(new Point(*ptrLL)), m_cornerUR(new Point(*ptrUR))
{
}

// Deep copy
RectangleComp::RectangleComp(const RectangleComp &other)
    : m_cornerLL(new Point(*other.m_cornerLL)), m_cornerUR(new Point(*other.m_cornerUR))
{
}

RectangleComp::~RectangleComp()
{
  // Must delete the points
  delete m_cornerLL;
  m_cornerLL = nullptr;
  delete m_cornerUR;
  m_cornerUR = nullptr;
}

void RectangleComp::show() const
{
  std::print("[");
  m_cornerLL->show();
  std::print(" - ");
  m_cornerUR->show();
  std::println("]");
}

double RectangleComp::getPerimeter() const
{
  return 2 * (m_cornerUR->m_x - m_cornerLL->m_x + m_cornerUR->m_y - m_cornerLL->m_y);
}

void RectangleComp::translate(double dx, double dy)
{
  m_cornerLL->m_x += dx;
  m_cornerUR->m_x += dx;
  m_cornerLL->m_y += dy;
  m_cornerUR->m_y += dy;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_02.07_RectangleComp_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"
#include "RectangleComp.h"

#include <print>

int main()
{
  Point pt1('A', 5, 5), pt2('B', 10, 12);

  RectangleComp R(&pt1, &pt2);
  std::print("R before translation: ");
  R.show();
  pt1.translate(3, 5);
  std::print("R after translating pt1: ");
  R.show();

  RectangleComp copyR(R);
  std::print("copyR before translation: ");
  copyR.show();
  R.translate(-5, -5);
  std::print("R after translation: ");
  R.show();
  std::print("copyR after translating R: ");
  copyR.show();
}
```
<!-- SNIPPET:END -->
