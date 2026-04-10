---
title: "4. Héritage et polymorphisme"
type: docs
weight: 10
---

# Chapitre 4 : héritage et polymorphisme

## Slides

{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/04_Heritage_et_polymorphisme.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/04_Heritage_et_polymorphisme.html?print-pdf)

## Exemples

{{<details "1242.2_04.01_InheritanceCircleCylinder" >}}
**`Circle.h`**
<!-- SNIPPET:BEGIN source_file=Circle.h id=1242.2_Examples_04.01_InheritanceCircleCylinder_Circle.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Circle
{
public:
    explicit Circle(double r = 1.0);
    virtual ~Circle();

    double getRadius() const;
    void setRadius(double r);

    // Not virtual: pointer type determines which surface() is called
    double surface() const;

private:
    double m_r{1.0};
};
```
<!-- SNIPPET:END -->

**`Circle.cpp`**
<!-- SNIPPET:BEGIN source_file=Circle.cpp id=1242.2_Examples_04.01_InheritanceCircleCylinder_Circle.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Circle.h"

#include <numbers>
#include <print>

Circle::Circle(double r) : m_r(r > 0.0 ? r : 1.0)
{
    std::println("[ctor] Circle(r={})", m_r);
}

Circle::~Circle()
{
    std::println("[dtor] ~Circle()");
}

double Circle::getRadius() const { return m_r; }

void Circle::setRadius(double r)
{
    m_r = (r > 0.0) ? r : 1.0;
}

double Circle::surface() const
{
    return m_r * m_r * std::numbers::pi;
}
```
<!-- SNIPPET:END -->

**`Cylinder.h`**
<!-- SNIPPET:BEGIN source_file=Cylinder.h id=1242.2_Examples_04.01_InheritanceCircleCylinder_Cylinder.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Cylinder : public Circle
{
public:
    explicit Cylinder(double r = 1.0, double h = 1.0);
    virtual ~Cylinder() override;

    // Redefines Circle::surface()
    // This is not an override (surface is not virtual)
    double surface() const;
    double volume() const;

private:
    double m_h{1.0};
};
```
<!-- SNIPPET:END -->

**`Cylinder.cpp`**
<!-- SNIPPET:BEGIN source_file=Cylinder.cpp id=1242.2_Examples_04.01_InheritanceCircleCylinder_Cylinder.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Cylinder.h"

#include <numbers>
#include <print>

Cylinder::Cylinder(double r, double h) : Circle(r), m_h(h > 0.0 ? h : 1.0)
{
    std::println("[ctor] Cylinder(r={}, h={})", getRadius(), m_h);
}

Cylinder::~Cylinder()
{
    std::println("[dtor] ~Cylinder()");
}

double Cylinder::surface() const
{
    return 2.0 * Circle::surface() + 2.0 * std::numbers::pi * getRadius() * m_h;
}

double Cylinder::volume() const
{
    return Circle::surface() * m_h;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.01_InheritanceCircleCylinder_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Cylinder.h"

#include <print>

int main()
{
  std::println("=== Automatic allocation ===");
  {
    auto c1 = Circle(10.0);
    auto c2 = Circle(); // default r = 1.0
    auto cyl = Cylinder(3.0, 5.0);

    std::println("\nc1.surface():  {:.4f}", c1.surface());
    std::println("c2.surface():  {:.4f}", c2.surface());
    std::println("cyl.surface(): {:.4f}", cyl.surface());
    std::println("cyl.volume():  {:.4f}", cyl.volume());

    // surface() is NOT virtual
    auto pCircle = &c1;
    std::println("\npCircle->surface() [points to c1]:  {:.4f}", pCircle->surface());

    pCircle = &cyl;
    std::println("pCircle->surface() [points to cyl]: {:.4f}  <- Circle::surface, not Cylinder::surface!", pCircle->surface());

    auto pCylinder = &cyl;
    std::println("pCylinder->surface() [points to cyl]: {:.4f}  <- Cylinder::surface", pCylinder->surface());

    std::println("\n=== Dynamic allocation ===");
    pCylinder = new Cylinder(1.0, 2.0);
    delete pCylinder;
    pCylinder = nullptr;

    std::println("\n=== End of scope — automatic objects destroyed in reverse order ===");
  }

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.02_AnimalsNonVirtual" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.02_AnimalsNonVirtual_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>
#include <vector>

class Animal
{
public:
    virtual ~Animal() = default;
    std::string id() const { return "animal"; }
};

class Cat : public Animal
{
public:
    std::string id() const { return "cat"; }
};

class StrayCat : public Cat
{
public:
    std::string id() const { return "stray cat"; }
};

class Dog : public Animal
{
public:
    std::string id() const { return "dog"; }
};

int main()
{
    auto animal = Animal();
    auto cat = Cat();
    auto straycat = StrayCat();
    auto dog = Dog();

    // Warning: slicing -> potential memory leak
    // OK: Cat IS-A Animal
    animal = cat;
    // OK: StrayCat IS-A Cat
    cat    = straycat; 

    std::println("--- Direct object calls ---");
    std::println("animal.id():   {}", animal.id());
    std::println("cat.id():      {}", cat.id());
    std::println("straycat.id(): {}", straycat.id());
    std::println("dog.id():      {}", dog.id());

    // Without virtual, the declared pointer type determines which id() is called
    std::println("\n--- Via Animal* array (id() is NOT virtual) ---");
    std::vector<Animal*> pA = { new Animal, new Dog, new Cat, new StrayCat };
    for (auto p : pA)
    {
        std::println("{}", p->id()); // always "animal" 
    }

    for (auto p : pA)
    {
        delete p;
        p = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.03_AnimalsVirtual" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.03_AnimalsVirtual_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

class Animal
{
public:
    virtual ~Animal() = default;
    virtual std::string id() const { return "animal"; }
};

class Cat : public Animal
{
public:
    std::string id() const override { return "cat"; }
};

class StrayCat : public Cat
{
public:
    std::string id() const override { return "stray cat"; }
};

class Dog : public Animal
{
public:
    std::string id() const override { return "dog"; }
};

int main()
{
    auto animal = Animal();
    auto cat = Cat();
    auto straycat = StrayCat();
    auto dog = Dog();

    std::println("--- Direct object calls ---");
    std::println("a.id():  {}", animal.id());
    std::println("c.id():  {}", cat.id());
    std::println("sc.id(): {}", straycat.id());
    std::println("d.id():  {}", dog.id());

    // With virtual, the actual object type determines which id() is called (dynamic dispatch)
    std::println("\n--- Via Animal* array (id() IS virtual) ---");
    Animal *pA[] = {new Animal, new Dog, new Cat, new StrayCat};
    for (auto p : pA)
    {
        std::println("{}", p->id()); // calls the actual object's id() at runtime
    }
    for (auto p : pA)
    {
        delete p;
        p = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.04_BaseAndDerivedPointers" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.04_BaseAndDerivedPointers_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

class Base
{
public:
    virtual ~Base() = default;
    std::string all() const { return "Base::all()"; }
    std::string baseOnly() const { return "Base::baseOnly()"; }
};

class Derived : public Base
{
public:
    std::string all() const { return "Derived::all()"; }
    std::string derivedOnly() const { return "Derived::derivedOnly()"; }
};

int main()
{
    std::println("=== Object variables ===");
    auto oB = Base();
    auto oD = Derived();

    std::println("oB.all():      {}", oB.all());
    std::println("oB.baseOnly(): {}", oB.baseOnly());
    // oB.derivedOnly() — compile error: Base has no member derivedOnly

    std::println("\noD.all():         {}", oD.all());
    std::println("oD.baseOnly():    {}", oD.baseOnly()); // inherited
    std::println("oD.derivedOnly(): {}", oD.derivedOnly());

    std::println("\n=== Object assignment (slicing) ===");
    oB = oD;                                               // OK: Derived IS-A Base — Derived part is sliced off
    std::println("After oB = oD, oB.all(): {}", oB.all()); // Base::all() — oB is still a Base
    // oD = oB — compile error: Base is not always a Derived

    std::println("\n=== Pointer assignment ===");
    auto poD = new Derived;
    auto poB = new Base;

    std::println("poD->all():         {}", poD->all());
    std::println("poD->derivedOnly(): {}", poD->derivedOnly());

    poB = poD; // OK: Base* can point to a Derived object
    std::println("After poB = poD:");
    std::println("  poB->all():      {}", poB->all()); // Base::all() — all() is not virtual
    std::println("  poB->baseOnly(): {}", poB->baseOnly());
    // poB->derivedOnly() — compile error: Base* has no derivedOnly

    // Downcast via C-style cast — compiles but dangerous if the object is not actually a Derived
    std::println("  ((Derived*)poB)->derivedOnly(): {}", ((Derived *)poB)->derivedOnly());

    // poD = poB1 — compile error without explicit cast: invalid conversion Base* → Derived*
    auto poB1 = new Base;
    poD = static_cast<Derived *>(poB1); // unsafe cast: poB1 is a Base, not a Derived
    std::println("\nAfter poD = static_cast<Derived*>(poB1) [UB if Derived members accessed]:");
    std::println("  poD->all(): {}", poD->all()); // accesses Base part — may appear to work

    delete poB1;
    poB1 = nullptr;
    delete poB; // poB points to the original Derived object (assigned above)
    poB = nullptr;
    poD = nullptr; // poD pointed to poB1 which is already deleted

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.05_FigureNonVirtual" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.05_FigureNonVirtual_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

class Figure
{
public:
    virtual ~Figure() = default;
    std::string draw() const { return "Figure"; }
};

class Triangle : public Figure
{
public:
    std::string draw() const { return "Triangle"; }
};

class Ellipse : public Figure
{
public:
    std::string draw() const { return "Ellipse"; }
};

int main()
{
    // draw() is NOT virtual: Figure* always calls Figure::draw()
    Figure* image[] = { new Figure(), new Triangle(), new Ellipse() };

    std::println("draw() via Figure* (not virtual):");
    for (auto p : image)
    {
        std::println("  {}", p->draw()); // always "Figure"
    }
    for (auto p : image)
    {
        delete p;
        p = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.06_FigureVirtual" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.06_FigureVirtual_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

class Figure
{
public:
    virtual ~Figure() = default;
    virtual std::string draw() const { return "Figure"; }
};

class Triangle : public Figure
{
public:
    std::string draw() const override { return "Triangle"; }
};

class Ellipse : public Figure
{
public:
    std::string draw() const override { return "Ellipse"; }
};

int main()
{
    // draw() IS virtual: each object's own draw() is called regardless of pointer type
    Figure* image[] = { new Figure(), new Triangle(), new Ellipse() };

    std::println("draw() via Figure* (virtual — polymorphism):");
    for (auto p : image)
    {
        std::println("  {}", p->draw()); // Figure, Triangle, Ellipse
    }
    for (auto p : image)
    {
        delete p;
        p = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.07_VTableMemoryLayout" >}}
**`Circle.h`**
<!-- SNIPPET:BEGIN source_file=Circle.h id=1242.2_Examples_04.07_VTableMemoryLayout_Circle.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Circle
{
public:
    explicit Circle(int r = 0);
    virtual ~Circle();

    int getRadius() const;
    void setRadius(int r);

    virtual double area() const;

private:
    int m_r{0};
};
```
<!-- SNIPPET:END -->

**`Circle.cpp`**
<!-- SNIPPET:BEGIN source_file=Circle.cpp id=1242.2_Examples_04.07_VTableMemoryLayout_Circle.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Circle.h"

#include <numbers>
#include <print>

Circle::Circle(int r) : m_r(r) {}

Circle::~Circle()
{
    std::println("[dtor] ~Circle()");
}

int  Circle::getRadius() const { return m_r; }
void Circle::setRadius(int r)  { m_r = r; }

double Circle::area() const
{
    return m_r * m_r * std::numbers::pi;
}
```
<!-- SNIPPET:END -->

**`Cylinder.h`**
<!-- SNIPPET:BEGIN source_file=Cylinder.h id=1242.2_Examples_04.07_VTableMemoryLayout_Cylinder.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
class Cylinder : public Circle
{
public:
    explicit Cylinder(int r = 0, int length = 0);
    ~Cylinder() override;

    double area() const override;

private:
    int m_length{0};
};
```
<!-- SNIPPET:END -->

**`Cylinder.cpp`**
<!-- SNIPPET:BEGIN source_file=Cylinder.cpp id=1242.2_Examples_04.07_VTableMemoryLayout_Cylinder.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Cylinder.h"

#include <numbers>
#include <print>

Cylinder::Cylinder(int r, int length) : Circle(r), m_length(length) {}

Cylinder::~Cylinder()
{
    std::println("[dtor] ~Cylinder()");
}

double Cylinder::area() const
{
    return 2.0 * std::numbers::pi * getRadius() * (getRadius() + m_length);
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.07_VTableMemoryLayout_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Cylinder.h"

#include <print>

int main()
{
    Circle   c(10);
    Cylinder cyl(10, 10);

    // A virtual method adds a hidden vtable pointer to every object.
    // sizeof reflects this: with virtual ~Circle() + virtual area(), each object
    // carries an extra pointer (typically 8 bytes on 64-bit).
    std::println("sizeof(Circle):   {}", sizeof(c));   // larger than just int m_r
    std::println("sizeof(Cylinder): {}", sizeof(cyl)); // larger than int m_r + int m_length

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.08_FigurePureVirtual" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.08_FigurePureVirtual_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

// Figure is now an abstract class
class Figure
{
public:
    virtual ~Figure() = default;
    virtual std::string draw() const = 0;
};

class Triangle : public Figure
{
public:
    std::string draw() const override { return "Triangle"; }
};

class Ellipse : public Figure
{
public:
    std::string draw() const override { return "Ellipse"; }
};

int main()
{
    // GCC - error: invalid new-expression of abstract class type 'Figure'
    // Figure* image[] = { new Figure(), new Triangle(), new Ellipse() };
    Figure *image[] = { new Ellipse(), new Triangle(), new Ellipse() };
    std::println("draw() via Figure* (virtual — polymorphism):");
    for (auto p : image)
    {
        std::println("  {}", p->draw());
    }
    for (auto p : image)
    {
        delete p;
        p = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_04.09_FigureProtectedCTor" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_04.09_FigureProtectedCTor_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <string>

class Figure
{
    protected:
    Figure() = default;
};

class Triangle : public Figure
{
};

class Ellipse : public Figure
{
};

int main()
{
    // GCC - error: 'constexpr Figure::Figure()' is protected within this context
    // Figure fig;

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 4.1
### Exercice 1 : héritage simple

Écrire une classe **`Pixel`** permettant de manipuler des points colorés.
Une couleur sera représentée par 3 entiers (voir schéma UML), chacun compris entre 0 et 255.
Cette classe disposera de la méthode **`show()`** qui affichera les coordonnées et la couleur d’un point.
Cette classe devra mettre en œuvre la notion d’héritage, en utilisant la classe **`Point`** définie dans la série 2.3.

On donne aussi le diagramme de classe des classes suivant :

{{<plantuml id="chap4_exo1.1">}}
@startuml

skin rose
skinparam classAttributeIconSize 0
hide circle

class Pixel extends Point

class Point
{
  + {static} counter : int
  # name : string
  # x : double
  # y : double
  +Point (x : double, y : double, name : string)
  +Point (pt : const Point &)
  +show () : void {query}
  +translate (dx : double, dy : double) : void
  +translate (pt : const Point&) : void
}

class Pixel
{
  - red : int
  - green : int
  - blue : int
  + Pixel (x : double, y : double, red : int, green : int, blue : int, name : string)
  + show () : void
  + getR () : int
  + getG () : int
  + getB () : int
  + setColor (red : int, green : int, blue : int)
}

note right of Point : Reprendre la classe de l'exercice 2.3
note right of Pixel : Implémenter la classe
@enduml
{{< /plantuml >}}

{{<a_noter>}}
Comme les couleurs R, G et B sont des entiers compris entre 0 et 255, on peut les stocker dans des variables de type **`unsigned char`** (alias **`uint8_t`**), ce qui permet d'économiser de la mémoire.
Cependant, pour simplifier l'exercice, nous utiliserons des **`int`** pour les couleurs.
{{</a_noter>}}

## Série 4.2

### Exercice 1 : polymorphisme

On souhaite écrire une hiérarchie de classes afin de manipuler des figures géométriques.
Cette hiérarchie pourra être enrichie grâce à l'héritage, mais on souhaite **imposer** que toutes ces nouvelles classes possèdent la méthode **`show()`** et puissent redéfinir la méthode **`translate()`**.

1.	Écrire la classe **`Figure`** pouvant servir de superclasse à cette hiérarchie.
2.	Écrire les classes **`Circle`**, **`Triangle`** et **`Rectangle`** qui héritent de **`Figure`**.
3.	Créer un tableau permettant de manipuler les 3 types de figures, y placer des cercles, triangles et rectangles, puis les afficher tous au moyen d’une seule boucle, en utilisant le polymorphisme.

{{< plantuml id="chap4_exo2.1">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
hide circle

class Triangle extends Figure
class Rectangle extends Figure
class Circle extends Figure

abstract class Figure
{
    # pos:Point
    + Figure(pos:const Point &)
    + ~Figure () {virtual}
    {abstract} + show () : void
    + translate (newPos:const Point&) : void {virtual}
}

class Triangle
{
    - p2:Point
    - p3:Point
    + Triangle(p1:const Point&, p2:const Point&, p3:const Point&)
    + ~Triangle() {virtual}
    + show():void {virtual}
    + translate(shift : const Point&):void {virtual}
}

class Rectangle
{
    - height:double
    - width:double
    + Rectangle(p:const Point&, width:double, height:double)
    + ~Rectangle() {virtual}
    + show() : void {virtual}
    + translate(shift:const Point&):void {virtual}
}

class Circle
{
    - radius:double
    + Circle(p:const Point &, radius:double)
    + ~Circle() {virtual}
    + show() : void {virtual}
    + translate(shift:const Point&) : void {virtual}
}

note left of Figure
Use class from exercise 1 of serie 4.1
end note
Note "Override translate() in subclasses when necessary" as N1

@enduml
{{< /plantuml >}}

## Série 4.3

### Exercice 1 : Héritage multiple

Quel sera l’affichage à l’exécution du programme ci-dessous.
Il n'est pas demandé de faire tourne le programme, mais juste de comprendre l'ordre de construction des objets.

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
    D() : C(), B()
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

### Exercice 2 : Héritage multiple virtuel

Modifier les classes ci-dessus pour produire la sortie suivante : 

```
A constructor 1
B constructor 1
C constructor 2
D constructor 3
Press any key to continue...
```

{{<attention>}}
Il ne faut pas modifier la fonction **`main()`**.
{{</attention>}}
