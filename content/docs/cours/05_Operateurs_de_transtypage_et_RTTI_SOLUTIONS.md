---
title: "5. Transtypage et RTTI — Solutions"
type: docs
weight: 10
draft: false
---

# Chapitre 5 : opérateurs de transtypage et RTTI — Solutions

## Série 5.1

### Exercice 1 : RTTI et `dynamic_cast`

{{<details "1242.2_05.01_RTTIAndDynamicCast" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>

class Point
{
public:
    Point(double x = 0., double y = 0., std::string name = "Point");
    Point(const Point& other);
    ~Point();

    void show() const;

    double getX() const { return m_x; }
    double getY() const { return m_y; }

    bool operator==(const Point& p) const { return m_x == p.m_x && m_y == p.m_y; }

    void translate(double dx, double dy);
    void translate(const Point& other);

    static int counter;

private:
    double m_x{0.};
    double m_y{0.};
    std::string m_name;
};
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::counter = 0;

Point::Point(double x, double y, std::string name)
    : m_x(x), m_y(y), m_name(name)
{
  counter++;
}

Point::Point(const Point &other)
    : m_x(other.m_x), m_y(other.m_y), m_name(other.m_name)
{
  counter++;
}

Point::~Point()
{
  counter--;
}

void Point::show() const
{
  std::print("{} : ({}, {})", m_name, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
  m_x += dx;
  m_y += dy;
}

void Point::translate(const Point &other)
{
  translate(other.m_x, other.m_y);
}
```
<!-- SNIPPET:END -->

**`Figure.h`**
<!-- SNIPPET:BEGIN source_file=Figure.h id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Figure.h -->
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

    Point getPos() const { return m_pos; }
    virtual void translate(const Point& shift);

protected:
    Point m_pos{0., 0.};
};
```
<!-- SNIPPET:END -->

**`Figure.cpp`**
<!-- SNIPPET:BEGIN source_file=Figure.cpp id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Figure.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
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
<!-- SNIPPET:BEGIN source_file=Circle.h id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Circle.h -->
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

    double getRadius() const { return m_radius; }
    void show() const override;

private:
    double m_radius{0.};
};
```
<!-- SNIPPET:END -->

**`Circle.cpp`**
<!-- SNIPPET:BEGIN source_file=Circle.cpp id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Circle.cpp -->
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
<!-- SNIPPET:BEGIN source_file=Rectangle.h id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Rectangle.h -->
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
    double m_height{0.};
    double m_width{0.};
};
```
<!-- SNIPPET:END -->

**`Rectangle.cpp`**
<!-- SNIPPET:BEGIN source_file=Rectangle.cpp id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Rectangle.cpp -->
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
<!-- SNIPPET:BEGIN source_file=Triangle.h id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Triangle.h -->
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
    Point m_pos2{0., 0.};
    Point m_pos3{0., 0.};
};
```
<!-- SNIPPET:END -->

**`Triangle.cpp`**
<!-- SNIPPET:BEGIN source_file=Triangle.cpp id=1242.2_Exercises_05.01_RTTIAndDynamicCast_Triangle.cpp -->
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
    std::println("");
}

void Triangle::translate(const Point& shift)
{
    Figure::translate(shift);
    m_pos2.translate(shift);
    m_pos3.translate(shift);
}
```
<!-- SNIPPET:END -->

**`compareShapes()`** (dans `main.cpp`)
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_05.01_RTTIAndDynamicCast_compareShapes.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Returns true if both figures are the same type and share the same position.
// typeid checks for exact type match — a Circle and a derived SpecialCircle would not match.
bool compareShapes(Figure *fig1, Figure *fig2)
{
  std::println("\n-- Comparing {} with {}", typeid(*fig1).name(), typeid(*fig2).name());

  if (typeid(*fig1) != typeid(*fig2))
  {
    std::println("   typeid differ");
    return false;
  }
  std::println("   typeid match");

  bool samePos = fig1->getPos() == fig2->getPos();
  std::println("   position: {}", samePos ? "same" : "different");
  return samePos;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_05.01_RTTIAndDynamicCast_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int main()
{
  std::println("========== Exercise 1 : typeid ==========");

  Rectangle r1(Point(1, 2), 4.0, 10.0);
  Rectangle r2(Point(1, 2), 4.0, 10.0);
  Rectangle r3(Point(10, 20), 10.0, 20.0);
  Circle c1(Point(1.1, 5.3), 5.0);

  std::println("\n### r1 and r2");
  std::println("same: {}", compareShapes(&r1, &r2));

  std::println("\n### r1 and r3");
  std::println("same: {}", compareShapes(&r1, &r3));

  std::println("\n### r1 and c1");
  std::println("same: {}", compareShapes(&r1, &c1));

  std::println("\n========== Exercise 2 : dynamic_cast ==========");

  Figure *myShapes[3];
  myShapes[0] = new Circle(Point(1.1, 5.3), 5.0);
  myShapes[1] = new Triangle(Point(2, 2), Point(10, 3), Point(-1, -1));
  myShapes[2] = new Rectangle(Point(4, 2), 4.0, 10.0);

  std::println("\n-- Shapes with radius when applicable --");
  for (auto shapePtr : myShapes)
  {
    shapePtr->show();
  }

  // Use auto & to modify the pointers in the array
  for (auto &shape : myShapes)
  {
    delete shape;
    shape = nullptr;
  }

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 5.2

### Exercice 1 : copie par `dynamic_cast`

{{<details "1242.2_05.02_CloneDynamicCast" >}}
> Hiérarchie Point/Figure/Circle/Rectangle/Triangle identique à la série 5.1.

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_05.02_CloneDynamicCast_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int main()
{
    Figure* myShapes[3];
    myShapes[0] = new Circle(Point(1.1, 5.3), 5.0);
    myShapes[1] = new Triangle(Point(2, 2), Point(10, 3), Point(-1, -1));
    myShapes[2] = new Rectangle(Point(4, 2), 4.0, 10.0);

    Figure* myShapesCopy[3];

    // dynamic_cast identifies the concrete type so we can call the right copy constructor.
    // Without clone(), there is no polymorphic way to copy through a base pointer.
    for (int i = 0; i < 3; ++i) {
        if (auto c = dynamic_cast<Circle*>(myShapes[i])) {
            myShapesCopy[i] = new Circle(*c);
        } else if (auto t = dynamic_cast<Triangle*>(myShapes[i])) {
            myShapesCopy[i] = new Triangle(*t);
        } else if (auto r = dynamic_cast<Rectangle*>(myShapes[i])) {
            myShapesCopy[i] = new Rectangle(*r);
        }
    }

    for (auto &shape : myShapes) {
        delete shape;
        shape = nullptr;
    }

    std::println("\n-- Copied shapes --");
    for (auto shape : myShapesCopy) {
        shape->show();
    }

    for (auto &shape : myShapesCopy) {
        delete shape;
        shape = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 2 : copie via `clone()` virtuel

{{<details "1242.2_05.03_CloneVirtual" >}}
> Point.h/cpp et les .cpp de la hiérarchie sont identiques à la série 5.1.

**`Figure.h`** (ajout de `clone()` pure virtuelle)
<!-- SNIPPET:BEGIN source_file=Figure.h id=1242.2_Exercises_05.03_CloneVirtual_Figure.h -->
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

    // Returns a heap-allocated copy of this object with the correct derived type.
    // Avoids the need for dynamic_cast when copying a heterogeneous collection.
    virtual Figure* clone() const = 0;

    Point getPos() const { return m_pos; }
    virtual void translate(const Point& shift);

protected:
    Point m_pos{0., 0.};
};
```
<!-- SNIPPET:END -->

**`Circle.h`**
<!-- SNIPPET:BEGIN source_file=Circle.h id=1242.2_Exercises_05.03_CloneVirtual_Circle.h -->
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

    Figure* clone() const override { return new Circle(*this); }

    double getRadius() const { return m_radius; }
    void show() const override;

private:
    double m_radius{0.};
};
```
<!-- SNIPPET:END -->

**`Rectangle.h`**
<!-- SNIPPET:BEGIN source_file=Rectangle.h id=1242.2_Exercises_05.03_CloneVirtual_Rectangle.h -->
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

    Figure* clone() const override { return new Rectangle(*this); }

    void show() const override;

private:
    double m_height{0.};
    double m_width{0.};
};
```
<!-- SNIPPET:END -->

**`Triangle.h`**
<!-- SNIPPET:BEGIN source_file=Triangle.h id=1242.2_Exercises_05.03_CloneVirtual_Triangle.h -->
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

    Figure* clone() const override { return new Triangle(*this); }

    void show() const override;
    void translate(const Point& shift) override;

private:
    Point m_pos2{0., 0.};
    Point m_pos3{0., 0.};
};
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_05.03_CloneVirtual_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int main()
{
    Figure* myShapes[3];
    myShapes[0] = new Circle(Point(1.1, 5.3), 5.0);
    myShapes[1] = new Triangle(Point(2, 2), Point(10, 3), Point(-1, -1));
    myShapes[2] = new Rectangle(Point(4, 2), 4.0, 10.0);

    Figure* myShapesCopy[3];

    // clone() dispatches to the correct derived type — no dynamic_cast needed.
    for (int i = 0; i < 3; ++i) {
        myShapesCopy[i] = myShapes[i]->clone();
    }

    for (auto &shape : myShapes) {
        delete shape;
        shape = nullptr;
    }

    std::println("\n-- Copied shapes --");
    for (auto shape : myShapesCopy) {
        shape->show();
    }

    for (auto &shape : myShapesCopy) {
        delete shape;
        shape = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
