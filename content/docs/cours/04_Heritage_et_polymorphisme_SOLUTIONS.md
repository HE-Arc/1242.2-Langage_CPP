---
title: "4. Héritage et polymorphisme — Solutions"
type: docs
weight: 10
draft: false
---

# Chapitre 4 : héritage et polymorphisme — Solutions

## Série 4.1

### Exercice 1 : héritage simple

{{<details "1242.2_04.01_PixelInheritance" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_04.01_PixelInheritance_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>

class Point
{
public:
    Point(double x = 0.0, double y = 0.0, std::string name = "Point");
    Point(const Point& other);
    virtual ~Point();

    void show() const;
    void translate(double dx, double dy);
    void translate(const Point& other);

    static int counter;

protected:
    double m_x{0.0};
    double m_y{0.0};
    std::string m_name;
};
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_04.01_PixelInheritance_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::counter = 0;

Point::Point(double x, double y, std::string name) : m_x(x), m_y(y), m_name(name)
{
    ++counter;
    std::print("[Cstd:{}]", counter);
}

Point::Point(const Point& other) : m_x(other.m_x), m_y(other.m_y), m_name(other.m_name)
{
    ++counter;
    std::print("[Ccop:{}]", counter);
}

Point::~Point()
{
    std::print("[Dstr:{}]", counter);
    --counter;
}

void Point::show() const
{
    std::println("{} : ({}, {})", m_name, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
    m_x += dx;
    m_y += dy;
}

void Point::translate(const Point& other)
{
    translate(other.m_x, other.m_y);
}
```
<!-- SNIPPET:END -->

**`Pixel.h`**
<!-- SNIPPET:BEGIN source_file=Pixel.h id=1242.2_Exercises_04.01_PixelInheritance_Pixel.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

class Pixel : public Point
{
public:
    Pixel(double x = 0.0, double y = 0.0, int red = 0, int green = 0, int blue = 0,
          std::string name = "Pixel");
    ~Pixel();

    int getR() const;
    int getG() const;
    int getB() const;
    void setColor(int red, int green, int blue);
    void show() const;

private:
    int m_red{0};
    int m_green{0};
    int m_blue{0};
};
```
<!-- SNIPPET:END -->

**`Pixel.cpp`**
<!-- SNIPPET:BEGIN source_file=Pixel.cpp id=1242.2_Exercises_04.01_PixelInheritance_Pixel.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
Pixel::Pixel(double x, double y, int red, int green, int blue, std::string name)
    : Point(x, y, name), m_red(red), m_green(green), m_blue(blue)
{
}

Pixel::~Pixel()
{
}

int Pixel::getR() const { return m_red; }
int Pixel::getG() const { return m_green; }
int Pixel::getB() const { return m_blue; }

void Pixel::setColor(int red, int green, int blue)
{
    if (red >= 0 && red < 256 && green >= 0 && green < 256 && blue >= 0 && blue < 256)
    {
        m_red   = red;
        m_green = green;
        m_blue  = blue;
    }
    else
    {
        std::println("Color values are not valid");
    }
}

void Pixel::show() const
{
    Point::show();
    std::println("Color (RGB): ({}, {}, {})", m_red, m_green, m_blue);
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_04.01_PixelInheritance_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Pixel.h"

#include <print>

int main()
{
    Pixel p1;
    Pixel p2(3.2, 5.5, 0, 0, 0);
    std::println();
    p1.show();

    std::println();
    p2.show();

    p2.setColor(255, 0, 128);
    std::println();
    p2.show();

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 2 : virtual show()

{{<details "1242.2_04.02_VirtualShowPixel" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_04.02_VirtualShowPixel_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

class Point
{
protected:
    double m_x{0.0};
    double m_y{0.0};

public:
    Point(double x = 0.0, double y = 0.0) : m_x(x), m_y(y) {}
    virtual ~Point() = default;

    virtual void show() const
    {
        std::println("I'm a point.");
        std::println("  my coordinates are: {} {}", m_x, m_y);
    }
};

class Pixel : public Point
{
    short m_color{0};

public:
    Pixel(double x = 0.0, double y = 0.0, short color = 1) : Point(x, y), m_color(color) {}

    void show() const override
    {
        std::println("I'm a pixel.");
        std::println("  my coordinates are: {}, {}", m_x, m_y);
        std::println("  and my color is:    {}", m_color);
    }
};

int main()
{
    Point  p(3.0, 5.0);
    Point* adp = &p;
    Pixel  pc(8.0, 6.0, 2);
    Pixel* adpc = &pc;

    // Calls Point::show() — static type is Point
    adp->show();
    // Calls Pixel::show() — static type is Pixel
    adpc->show();

    std::println("------------------");

    // adp now points to a Pixel object
    adp = adpc;
    // Calls Pixel::show() — show() is virtual, resolved at runtime
    adp->show();
    adpc->show();

    return 0;
}
```
<!-- SNIPPET:END -->

**Affichage :**
```
I'm a point.
  my coordinates are: 3 5
I'm a pixel.
  my coordinates are: 8, 6
  and my color is:    2
------------------
I'm a pixel.
  my coordinates are: 8, 6
  and my color is:    2
I'm a pixel.
  my coordinates are: 8, 6
  and my color is:    2
```
{{</details>}}

### Exercice 3 : virtual identify()

{{<details "1242.2_04.03_VirtualIdentifyPixel" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_04.03_VirtualIdentifyPixel_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

class Point
{
protected:
    double m_x{0.0};
    double m_y{0.0};

public:
    Point(double x = 0.0, double y = 0.0) : m_x(x), m_y(y) {}
    virtual ~Point() = default;

    // show() is NOT virtual: always calls Point::show() regardless of pointer type
    void show() const
    {
        identify();  // virtual dispatch: calls the actual object's identify()
        std::println("  my coordinates are: {}, {}", m_x, m_y);
    }

    virtual void identify() const
    {
        std::println("I'm a point.");
    }
};

class Pixel : public Point
{
    short m_color{0};

public:
    Pixel(double x = 0.0, double y = 0.0, short color = 1) : Point(x, y), m_color(color) {}

    void identify() const override
    {
        std::println("I'm a pixel of color: {}", m_color);
    }
};

int main()
{
    Point  p(3.0, 4.0);
    Pixel  pc(5.0, 9.0, 5);

    // Point::show() → Point::identify()
    p.show();
    // Point::show() → Pixel::identify() (virtual dispatch)
    pc.show();

    std::println("---------------");

    Point* adp  = &p;
    Pixel* adpc = &pc;

    adp->show();   // Point::show() → Point::identify()
    adpc->show();  // Point::show() → Pixel::identify()

    std::println("---------------");

    adp = adpc;
    adp->show();   // Point::show() → Pixel::identify()
    adpc->show();  // Point::show() → Pixel::identify()

    return 0;
}
```
<!-- SNIPPET:END -->

**Affichage :**
```
I'm a point.
  my coordinates are: 3, 4
I'm a pixel of color: 5
  my coordinates are: 5, 9
---------------
I'm a point.
  my coordinates are: 3, 4
I'm a pixel of color: 5
  my coordinates are: 5, 9
---------------
I'm a pixel of color: 5
  my coordinates are: 5, 9
I'm a pixel of color: 5
  my coordinates are: 5, 9
```
{{</details>}}

## Série 4.2

### Exercice 1 : polymorphisme

{{<details "1242.2_04.04_FigurePolymorphism" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_04.04_FigurePolymorphism_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>

class Point
{
public:
    Point(double x = 0.0, double y = 0.0, std::string name = "Point");
    Point(const Point& other);
    virtual ~Point();

    void show() const;
    void translate(double dx, double dy);
    void translate(const Point& other);

    static int counter;

protected:
    double m_x{0.0};
    double m_y{0.0};
    std::string m_name;
};
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_04.04_FigurePolymorphism_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::counter = 0;

Point::Point(double x, double y, std::string name) : m_x(x), m_y(y), m_name(name)
{
    ++counter;
    std::print("[Cstd:{}]", counter);
}

Point::Point(const Point& other) : m_x(other.m_x), m_y(other.m_y), m_name(other.m_name)
{
    ++counter;
    std::print("[Ccop:{}]", counter);
}

Point::~Point()
{
    std::print("[Dstr:{}]", counter);
    --counter;
}

void Point::show() const
{
    std::print("({}, {})", m_x, m_y);
}

void Point::translate(double dx, double dy)
{
    m_x += dx;
    m_y += dy;
}

void Point::translate(const Point& other)
{
    translate(other.m_x, other.m_y);
}
```
<!-- SNIPPET:END -->

**`Figure.h`**
<!-- SNIPPET:BEGIN source_file=Figure.h id=1242.2_Exercises_04.04_FigurePolymorphism_Figure.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Point.h"

class Figure
{
public:
    explicit Figure(const Point& pos) : m_pos(pos) {}
    virtual ~Figure() = default;

    virtual void show() const = 0;
    virtual void translate(const Point& shift);

protected:
    Point m_pos{0.0, 0.0};
};
```
<!-- SNIPPET:END -->

**`Figure.cpp`**
<!-- SNIPPET:BEGIN source_file=Figure.cpp id=1242.2_Exercises_04.04_FigurePolymorphism_Figure.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Provides a default implementation that subclasses can call via Figure::show()
void Figure::show() const
{
    m_pos.show();
}

void Figure::translate(const Point& shift)
{
    m_pos.translate(shift);
}
```
<!-- SNIPPET:END -->

**`Circle.h`**
<!-- SNIPPET:BEGIN source_file=Circle.h id=1242.2_Exercises_04.04_FigurePolymorphism_Circle.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Figure.h"

class Circle : public Figure
{
public:
    Circle(const Point& pos, double radius) : Figure(pos), m_radius(radius) {}
    ~Circle() override = default;

    void show() const override;

private:
    double m_radius{0.0};
};
```
<!-- SNIPPET:END -->

**`Circle.cpp`**
<!-- SNIPPET:BEGIN source_file=Circle.cpp id=1242.2_Exercises_04.04_FigurePolymorphism_Circle.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
void Circle::show() const
{
    std::print("Circle: ");
    Figure::show();
    std::println(", radius={}", m_radius);
}
```
<!-- SNIPPET:END -->

**`Rectangle.h`**
<!-- SNIPPET:BEGIN source_file=Rectangle.h id=1242.2_Exercises_04.04_FigurePolymorphism_Rectangle.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Figure.h"

class Rectangle : public Figure
{
public:
    Rectangle(const Point& pos, double height, double width)
        : Figure(pos), m_height(height), m_width(width) {}
    ~Rectangle() override = default;

    void show() const override;

private:
    double m_height{0.0};
    double m_width{0.0};
};
```
<!-- SNIPPET:END -->

**`Rectangle.cpp`**
<!-- SNIPPET:BEGIN source_file=Rectangle.cpp id=1242.2_Exercises_04.04_FigurePolymorphism_Rectangle.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
void Rectangle::show() const
{
    std::print("Rectangle: ");
    Figure::show();
    std::println(", w={}, h={}", m_width, m_height);
}
```
<!-- SNIPPET:END -->

**`Triangle.h`**
<!-- SNIPPET:BEGIN source_file=Triangle.h id=1242.2_Exercises_04.04_FigurePolymorphism_Triangle.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Figure.h"

class Triangle : public Figure
{
public:
    Triangle(const Point& pos, Point pos2, Point pos3)
        : Figure(pos), m_pos2(pos2), m_pos3(pos3) {}
    ~Triangle() override = default;

    void show() const override;
    void translate(const Point& shift) override;

private:
    Point m_pos2{0.0, 0.0};
    Point m_pos3{0.0, 0.0};
};
```
<!-- SNIPPET:END -->

**`Triangle.cpp`**
<!-- SNIPPET:BEGIN source_file=Triangle.cpp id=1242.2_Exercises_04.04_FigurePolymorphism_Triangle.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
void Triangle::show() const
{
    std::print("Triangle: ");
    Figure::show();
    std::print(", ");
    m_pos2.show();
    std::print(", ");
    m_pos3.show();
    std::println();
}

void Triangle::translate(const Point& shift)
{
    Figure::translate(shift);
    m_pos2.translate(shift);
    m_pos3.translate(shift);
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_04.04_FigurePolymorphism_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Circle.h"
#include "Rectangle.h"
#include "Triangle.h"

#include <print>

int main()
{
    Figure* myShapes[3];
    myShapes[0] = new Circle(Point(1.1, 5.3), 5.0);
    myShapes[1] = new Triangle(Point(2, 2), Point(10, 3), Point(-1, -1));
    myShapes[2] = new Rectangle(Point(4, 2), 4.0, 10.0);

    std::println("\n--- Shapes ---");
    for (auto shape : myShapes)
    {
        shape->show();
    }

    std::println("\n--- After translation by (-1.5, -1.5) ---");
    for (auto shape : myShapes)
    {
        shape->translate(Point(-1.5, -1.5));
    }
    for (auto shape : myShapes)
    {
        shape->show();
    }

    for (auto shape : myShapes)
    {
        delete shape;
        shape = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 4.3

### Exercice 1 : héritage multiple

{{<details "1242.2_04.05_MultipleInheritance" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_04.05_MultipleInheritance_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

class A
{
public:
  A(int na) : m_na(na)
  {
    std::println("A constructor {}", m_na);
  }

protected:
  int m_na{0};
};

class B : public A
{
public:
  B() : A(1)
  {
    std::println("B constructor {}", m_nb);
  }

protected:
  int m_nb{1};
};

class C : public A
{
public:
  C() : A(2)
  {
    std::println("C constructor {}", m_nc);
  }

protected:
  int m_nc{2};
};

class D : public B, public C
{
  int m_nd{3};

public:
  // GCC - warning: base 'C' will be initialized after [-Wreorder]
  // D() : C(), B()
  D() : B(), C()
  {
    std::println("D constructor {}", m_nd);
  }
};

int main()
{
  D d;
  return 0;
}
```
<!-- SNIPPET:END -->

**Affichage :**
```
A constructor 1
B constructor 1
A constructor 2
C constructor 2
D constructor 3
```
{{</details>}}

### Exercice 2 : héritage multiple virtuel

{{<details "1242.2_04.06_VirtualMultipleInheritance" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_04.06_VirtualMultipleInheritance_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

class A
{
public:
    // Default parameter required: D initializes A without arguments (virtual base initialization)
    A(int na = 1) : m_na(na)
    {
        std::println("A constructor {}", m_na);
    }

protected:
    int m_na{0};
};

// Virtual inheritance: only one A instance is shared across the hierarchy
class B : virtual public A
{
public:
    B()
    {
        std::println("B constructor {}", m_nb);
    }

protected:
    int m_nb{1};
};

class C : virtual public A
{
public:
    C() : A(2)
    {
        std::println("C constructor {}", m_nc);
    }

protected:
    int m_nc{2};
};

// With virtual inheritance, D (the most-derived class) initializes A once
class D : public B, public C
{
public:
    D() : B(), C()
    {
        A::m_na = 3;  // unambiguous: only one A object exists
        std::println("D constructor {}", m_nd);
    }

protected:
    int m_nd{3};
};

int main()
{
    D d;
    return 0;
}
```
<!-- SNIPPET:END -->

**Affichage :**
```
A constructor 1
B constructor 1
C constructor 2
D constructor 3
```
{{</details>}}