---
title: "5. Transtypage et RTTI"
type: docs
weight: 10
---

# Chapitre 5 : opérateurs de transtypage et RTTI

## Slides

{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/05_Operateurs_de_transtypage_et_RTTI.html" >}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/05_Operateurs_de_transtypage_et_RTTI.html?print-pdf)

## Exemples

{{<details "1242.2_05.01_DynamicCast" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_05.01_DynamicCast_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <typeinfo>

class Pet
{
public:
  virtual void show() const { std::println("Pet"); }
  virtual ~Pet() = default;
};

class Dog : public Pet
{
public:
  void show() const override { std::println("Dog"); }
};

class Cat : public Pet
{
public:
  void show() const override { std::println("Cat"); }
};

class Siamese : public Cat
{
public:
  void show() const override { std::println("Siamese cat"); }
  void siamFunction() {}
};

int main()
{
  Pet *myPet = new Cat; // upcast: always safe
  // %p: pointer as a void*
  std::println("myPet = {:p}\n", static_cast<void *>(myPet));

  // dynamic_cast returns nullptr when the runtime type does not match
  auto myDog = dynamic_cast<Dog *>(myPet);
  auto myCat = dynamic_cast<Cat *>(myPet);

  std::println("myDog = {:p}  (nullptr: cast failed)", static_cast<void *>(myDog));
  std::println("myCat = {:p}  (not nullptr: cast succeeded)\n", static_cast<void *>(myCat));

  // C-style casts compile without error but bypass runtime type checks
  auto myDog2 = (Dog *)myPet;
  auto myCat2 = (Cat *)myPet;
  std::println("myDog2 = {:p}", static_cast<void *>(myDog2));
  std::println("myCat2 = {:p}\n", static_cast<void *>(myCat2));

  auto mySiamese = dynamic_cast<Siamese *>(myPet); // fails: Cat is not a Siamese
  std::println("mySiamese = {:p}  (nullptr: cast failed)\n", static_cast<void *>(mySiamese));

  Pet *myOtherPet = new Siamese;
  auto mySiamese2 = dynamic_cast<Siamese *>(myOtherPet); // succeeds
  std::println("mySiamese2 = {:p}  (not nullptr: cast succeeded)\n", static_cast<void *>(mySiamese2));

  myCat = dynamic_cast<Cat *>(myOtherPet); // succeeds: Siamese IS-A Cat
  std::println("myCat = {:p}", static_cast<void *>(myCat));
  std::println("Type of *myCat: {}", typeid(*myCat).name());

  // Virtual dispatch still calls Siamese::show() even through a Cat*
  myCat->show();

  delete myPet;
  delete myOtherPet;

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_05.02_TypeidPolymorphic" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_05.02_TypeidPolymorphic_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <typeinfo>

class Animal
{
public:
  virtual ~Animal() = default;
};
class Mammal : public Animal
{
};
class Dog : public Mammal
{
};
class Poodle : public Dog
{
};

int main()
{
  Animal *ptr = new Poodle;

  std::println("{}", typeid(bool).name());

  // typeid on a pointer gives the declared pointer type
  std::println("Type of ptr  : {}", typeid(ptr).name());
  // typeid on the dereferenced pointer gives the actual runtime type
  // (only accurate for polymorphic classes — requires at least one virtual method)
  std::println("Type of *ptr : {}", typeid(*ptr).name());

  std::println("\nThe animal pointed to by ptr {} a Dog",
               typeid(*ptr) == typeid(Dog) ? "is" : "is not");
  std::println("The animal pointed to by ptr {} a Poodle",
               typeid(*ptr) == typeid(Poodle) ? "is" : "is not");

  std::println("\nThe animal pointed to by ptr is a {}", typeid(*ptr).name());

  delete ptr;
  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_05.03_TypeidSimpleTypes" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_05.03_TypeidSimpleTypes_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <typeinfo>

int main()
{
  auto integer = 3;
  auto real = 3.14f;
  auto vDouble = 2.12;
  auto character = 'a';

  std::println("Type of integer   : {}", typeid(integer).name());
  std::println("Type of real      : {}", typeid(real).name());
  std::println("Type of vDouble   : {}", typeid(vDouble).name());
  std::println("Type of character : {}", typeid(character).name());

  if (typeid(integer) == typeid(int))
  {
    std::println("integer is an int");
  }
  else
  {
    std::println("integer is not an int");
  }

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_05.04_DowncastingDanger" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_05.04_DowncastingDanger_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

class A
{
public:
  virtual void display() const { std::println("Class A"); }
  void functionA() const { std::println("functionA"); }
  virtual ~A() = default;
};

class B : public A
{
public:
  void display() const override { std::println("Class B"); }
  void functionB() const { std::println("functionB"); }
};

class C : public B
{
public:
  void display() const override { std::println("Class C"); }
  int c[100];
  virtual void functionC()
  {
    std::println("functionC");
    c[99] = 1;
    std::println("c[99] = {}", c[99]);
  }
};

int main()
{
  A *objAB = new B;
  std::println("objAB = {:p}", static_cast<void *>(objAB));
  objAB->display();
  objAB->functionA();
  // Cannot call functionB() through A*, even though the object is a B
  std::println("");

  // dynamic_cast succeeds: objAB actually points to a B
  B *objB = dynamic_cast<B *>(objAB);
  std::println("objB = {:p}", static_cast<void *>(objB));
  objB->display();
  objB->functionA();
  objB->functionB();
  std::println("");

  // dynamic_cast returns nullptr: objAB is B, not C
  C *objC = dynamic_cast<C *>(objB);
  std::println("objC = {:p}  (null: objB is not a C)\n", static_cast<void *>(objC));

  // C-style cast bypasses the runtime check — objC2 points to a B object
  // but the compiler treats it as C*. Accessing C-specific data is undefined behavior.
  C *objC2 = (C *)objB;
  std::println("objC2 = {:p}", static_cast<void *>(objC2));
  objC2->display();
  objC2->functionA();
  objC2->functionB();
  objC2->c[50] = 1;
  // Calling a virtual function through an invalid cast crashes at runtime
  // objC2->functionC();   // uncomment to observe crash

  C *objC3 = new C;
  std::println("\nobjC3 = {:p}", static_cast<void *>(objC3));
  for (int i = 0; i < 100; i++)
  {
    objC3->c[i] = 3;
  }
  // objC2->c[50] was 1 but the value depends on where objC3 was allocated
  std::println("objC2->c[50] = {}", objC2->c[50]);
  std::println("objC3->c[0]  = {}", objC3->c[0]);

  delete objAB;
  delete objC3;

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_05.05_TypeidVsDynamicCast" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_05.05_TypeidVsDynamicCast_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <typeinfo>

class Animal
{
public:
  virtual ~Animal() = default;
};
class Mammal : public Animal
{
};
class Dog : public Mammal
{
};
class Poodle : public Dog
{
};

int main()
{
  Animal *ptr = new Poodle;

  // typeid ignores the inheritance hierarchy: Poodle is NOT Dog (exactly)
  std::println("typeid == Dog    : {}", typeid(*ptr) == typeid(Dog));    // false
  std::println("typeid == Poodle : {}", typeid(*ptr) == typeid(Poodle)); // true

  // dynamic_cast respects inheritance: Poodle IS-A Dog IS-A Mammal IS-A Animal
  std::println("dynamic_cast<Dog*>    : {}", dynamic_cast<Dog *>(ptr) != nullptr);    // true
  std::println("dynamic_cast<Poodle*> : {}", dynamic_cast<Poodle *>(ptr) != nullptr); // true
  std::println("dynamic_cast<Mammal*> : {}", dynamic_cast<Mammal *>(ptr) != nullptr); // true

  delete ptr;

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_05.06_BasicCasts" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_05.06_BasicCasts_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

int main()
{
  // static_cast
  {
    int i = 100;
    [[maybe_unused]]
    auto c = static_cast<char>(i); // int -> char

    auto f = 100.0f;
    i = static_cast<int>(f); // float -> int

    class Base
    {
    };
    class Deri : public Base
    {
    };
    [[maybe_unused]]
    auto d = new Deri;
    [[maybe_unused]]
    auto b = static_cast<Base *>(d); // Deri* -> Base*
  }

  // reinterpret_cast
  {
    auto f = 99.0f;
    auto pf = &f;
    auto d = 99.0;
    auto pd = &d;
    // Wont compile
    // pd = static_cast<double>(pf);
    pd = reinterpret_cast<double *>(pf);

    int i = 99;
    // UB but compiles
    [[maybe_unused]]
    auto ptr = reinterpret_cast<char *>(i); // int -> char*
    [[maybe_unused]]
    auto ref = reinterpret_cast<char &>(i); // int -> char&
    [[maybe_unused]]
    auto pf2 = reinterpret_cast<float *>(pd); // double* -> float*
  }

  // const_cast
  {
    class A
    {
    };

    [[maybe_unused]]
    const A *cptr = new A;
    [[maybe_unused]]
    auto ptr = const_cast<A *>(cptr); // const A* -> A*

    A a;
    [[maybe_unused]]
    const A &cref = a;
    [[maybe_unused]]
    auto ref = const_cast<A &>(cref); // const A& -> A&
  }

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Serie 5.1
### Exercice 1 : RTTI

On aimerait pouvoir comparer des objets afin de savoir s'ils sont de la même classe et si leur contenu est identique.

1.  Reprendre le projet de la série 4.2 concernant les figures.
2.  Implémentez la méthode suivante  **`bool compareShapes(Figure *fig1, Figure *fig2)`** qui retoune vrai si :
       * les objets sont des instances de la même classe (utiliser typeid)
       * le point **`pos`** définit dans **`Figure`** est le même pour les 2 objets.
3. Le **`main()`** a l'aspect suivant :

```cpp
int main()
{
    Rectangle r1(Point( 1,  2),  4.0, 10.0);
    Rectangle r2(Point( 1,  2),  4.0, 10.0);
    Rectangle r3(Point(10, 20), 10.0, 20.0);
    Circle    c1(Point(1.1, 5.3), 5.0);

    cout << endl << "Comparison of r1 and r2" << endl;
    areTheSame = compareShapes(&r1, &r2);
    cout << endl << "r1 and r2 are the same : " << boolalpha << areTheSame <<endl;

    cout << endl << "Comparison of r1 and r3" << endl;
    areTheSame = compareShapes(&r1, &r3);
    cout << endl << "r1 and r3 are the same : "<< boolalpha << areTheSame <<endl;

    cout << endl << "Comparison of r1 and c1" << endl;
    areTheSame = compareShapes(&r1, &c1);
    cout << endl << "r1 and c1 are the same : "<< boolalpha << areTheSame <<endl;
}
```
Le résultat :
```
Comparison of r1 and r2
     Comparison of an objet 9Rectangle with an objet 9Rectangle
     -  typeid are the same
     -  positions are the same
r1 and r2 are the same: true

Comparison of r1 and r3
     Comparison of an objet 9Rectangle with an objet 9Rectangle    
     - typeid are the same
     - positions are different
r1 and r3 are the same: false

Comparison of r1 and c1
     Comparison of an objet 9Rectangle with an objet 6Circle
     - typeid are different
r1 and c1 are the same: false
```

### Exercice 2 : transtypage dynamique

On aimerait pouvoir accéder à une méthode spécifique à une des classe dérivée, sans connaitre le pointeur sur cette classe, mais uniquement le pointeur sur la classe mère.

1.  reprendre le projet de la série 4.2 concernant les figures.
2.  ajouter la méthode **`getRadius()`** à la classe **`Circle`** 
3.  le code ci-dessous ne fonctionne pas car la méthode n'existe pas dans les classes **`Figure`**, **`Rectangle`** et **`Triangle`**.

```cpp
int main()
{
    Figure *myShapes[3];

    myShapes[0] = new Circle(Point(1.1, 5.3), 5.0);
    myShapes[1] = new Triangle(Point(2, 2), Point(10, 3), Point(-1, -1));
    myShapes[2] = new Rectangle(Point(4, 2), 4.0, 10.0);

    cout << "------- List of shapes -----------" << endl;
    for (auto shape : myShapes)
    {
        shape->show();
        //shape->getRadius();
    }
    return 0;
}
```

Améliorer ce code afin qu'il offre la sortie suivante :
```
Cercle:
   Point : (1.1, 5.3), radius=5
>>>>>>>>>>>>>>> The radius is: 5    (obtenu au moyen de getRadius()

Triangle:
  Point : (2, 2)
  Point : (10, 3)
  Point : (-1, -1)

Rectangle:
  Point : (4, 2), l = 10, h = 4
```

## Serie 5.2
### Exercice 1

Soit un tableau de pointeurs sur des **`Figure`** (cf série 4.2), on aimerait faire une copie de ce tableau.
Pour cela, il faut réallouer la mémoire pour chacun des objets pointés.

```cpp
int main()
{
    Figure *myShapes[3];

    myShapes[0] = new Circle(Point(1.1, 5.3), 5.0);
    myShapes[1] = new Triangle(Point(2, 2), Point(10, 3), Point(-1, -1));
    myShapes[2] = new Rectangle(Point(4, 2), 4.0, 10.0);

    Figure *myShapesCopy[3];

    return 0;
}
```

1. reprendre le projet de la série 4.2 concernant les **`Figure`**
2. utiliser le transtypage dynamique.

Afin de vérifier le bon fonctionnement, désallouer d'abord les **`Figure`** du tableau original puis affichez la copie. 

### Exercice 2

Reprendre le problème précédent, en tirant bénéfice du polymorphime.
Dans la classe **`Figure`**, déclarer une méthode virtuelle pure **`clone()`**.
Chaque classe dérivée l'implémente de manière : 
* à se cloner elle-même
* à allouer dynamiquement de la mémoire 
* à retourner un pointeur. 

Afin de vérifier le bon fonctionnement, désallouer d'abord les **`Figure`** du tableau original puis affichez la copie.
