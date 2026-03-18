---
title: "2. Des classes et des objets"
type: docs
weight: 10
---

# Chapitre 2 : des classes et des objets

## Slides
{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/02_Des_classes_et_des_objets.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/02_Des_classes_et_des_objets.html?print-pdf)

## Exemples

{{<details "1242.2_02.01_PointClass" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Examples_02.01_PointClass_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp

#pragma once

// @warning: this class is verbose for educational purposes only.
class Point
{
  public:
  
  // ========== BASIC METHODS ==========

  // Without C++ contructors, we would need to use an init method.
  // This is not needed in C++
  // void init(int px, int py)
  // {
  //     m_x = px;
  //     m_y = py;
  // }
  
  // Implicitly inline methods
  void setX(int x) {m_x = x;}
  void setY(int y) {m_y = y;}
  void setXY(int x, int y){m_x = x; m_y = y;}

  // Inline with definition in header (see end of this file) 
  int getX() const;
  int getY() const;

  void translate(int dx, int dy); 

  // ========== CONSTRUCTORS ==========
  // Default constructor
  Point();

  // Constructor
  Point(int x, int y);

  // Copy constructor
  Point(const Point &p);

  // Conversion constructor from int to Point
  explicit Point(int v);

  // ========== DESTRUCTOR ==========
  virtual ~Point(); // virtual: see chapter on polymorphism

  // ========== COPY ASSIGNMENT ==========
  // Just make it default (compiler-generated)
  Point& operator=(const Point &p) = default;

  // ========== CONST METHODS ==========
  void print() const;

  // ========== 'this' POINTER USAGE ==========
  // Demonstrates: using 'this' pointer
  bool isSameObject(const Point &other) const;

  // Demonstrates: '*this' (dereferencing)
  Point getCopy() const;

  // ========== STATIC MEMBERS ==========
  // Do not belong to a specific instance
  static int getCounts();

  // ========== FRIEND FUNCTION ==========
  friend double distance(const Point &p1, const Point &p2);

  // ========== RETURNING A REFERENCE ==========
  // Allows: p.X() = 5;  or  p.X()++;
  // NOTE: This breaks encapsulation (equivalent to making m_x public).
  //       In practice, prefer getX()/setX() for simple attributes.
  int X() const {return m_x;}
  // Cannot be const
  int &X() {return m_x;}
  int Y() const {return m_y;}
  // Cannot be const
  int &Y() {return m_y;}

private:
  // Attributes
  int m_x{0};
  int m_y{0};

  // Shared attribute for all instances
  static int m_counts;
};

inline int Point::getX() const {return m_x;}
inline int Point::getY() const {return m_y;}

// Non-member function
double distance(const Point &p1, const Point &p2);
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Examples_02.01_PointClass_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp

#include "Point.h"
#include <print>
#include <cmath>

// ========== STATIC MEMBERS INITIALIZATION ==========
int Point::m_counts = 0;

// ========== 1. BASIC METHODS ==========
void Point::translate(int dx, int dy)
{
  m_x += dx;
  m_y += dy;
}

// ========== 2. CONSTRUCTORS ==========
Point::Point() // : m_x(0), m_y(0) -> not needed. See in-class initialization
{
  m_counts++;
  std::println("  ->default ctor (counts={})", m_counts);
}

// member initializer list
Point::Point(int x, int y) : m_x(x), m_y(y)
{
  m_counts++;
  std::println("  ->standard ctor (with initializer list, counts={})", m_counts);
}

Point::Point(int v) : m_x(v), m_y(v)
{
  m_counts++;
  std::println("  ->conversion ctor (counts={})", m_counts);
}

Point::Point(const Point &p) : m_x(p.m_x), m_y(p.m_y)
{
  m_counts++;
  std::println("  ->copy ctor (counts={})", m_counts);
}

// ========== 3. DESTRUCTOR ==========
Point::~Point()
{
  m_counts--;
  std::println("  ~Point() dtor called (counts={})", m_counts);
}

// ========== 4. CONST METHODS ==========
void Point::print() const
{
  // C++23
  std::println("({}, {})", m_x, m_y);
  // Prior to C++23:
  // std::cout << "(" << m_x << "," << m_y << ")" << std::endl;
}

// ========== 5. 'this' POINTER USAGE ==========

bool Point::isSameObject(const Point &otherPoint) const
{  
  return (this == &otherPoint);
}

Point Point::getCopy() const
{
  return *this;
}

// ========== 6. STATIC METHODS ==========
int Point::getCounts()
{
  return m_counts;
}

// ========== 7. FRIEND FUNCTION ==========
double distance(const Point &p1, const Point &p2)
{
  // Friend of Point: can access private members
  int dx = p1.m_x - p2.m_x;
  int dy = p1.m_y - p2.m_y;
  return std::sqrt(dx * dx + dy * dy);
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_02.01_PointClass_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp

#include "Point.h"

#include <print>
#include <vector>

void f1(Point p)
{
  p.print();
}

void f2(const Point &p)
{
  p.print();
}

void f3(Point *p)
{
  p->print();
}

Point f4()
{
  Point p(5, 6);
  p.print();
  return p;
}

void example01_basic()
{
  Point p1;
  p1.print();

  p1.translate(10, 10);
  p1.print();
}

void example02_conversion()
{
  // Explicitly calls CTor
  Point p1 = Point(4);
  p1.print();
  // GCC: error: conversion from 'int' to non-scalar type 'Point' requested
  // Point p2 = 4;
}

void example03_constructors()
{
  Point p1 = Point();
  p1.print();
  p1.setXY(100, 200);
  p1.print();

  Point p2(1, 2);
  p2.print();
  Point p3 = Point(1, 2);
  p3.print();

  Point p4(p1);
  p4.print();

  Point p5 = p1;
  p5.print();

  Point p6(10);
  p6.print();

  // GCC: error: conversion from 'int' to non-scalar type 'Point' requested
  // Point p7 = 11;

  // GCC: error: no match for 'operator=' (operand types are 'Point' and 'int')
  // Point p8;
  // p8 = 4;

  Point *pP1 = new Point();
  pP1->setXY(150, 250);
  pP1->print();
  delete pP1;
  pP1 = nullptr;
}

void example04_copyConstructor()
{
  Point p1(3, 4);

  Point p4(p1);
  p4.print();

  Point p5 = Point(p1);
  p5.print();

  f1(p4);
  f2(p4);
  f3(&p4);
  Point p6 = f4();
}

void example05_destructor()
{
  {
    Point p1(1, 1);
    Point pn[4];
  }

  auto ptrP = new Point(2, 3);
  ptrP->setXY(150, 250);
  ptrP->print();
  delete ptrP;
  ptrP = nullptr;

  auto ptrTabPoint = new Point[5];
  delete[] ptrTabPoint;
  ptrTabPoint = nullptr;
}

void example06_this()
{
  Point pt(5, 7);
  Point p2(pt);
  Point &refPt = pt;
  Point *ptrPt = &pt;
  Point clone = pt.getCopy();

  pt.print();
  p2.print();
  refPt.print();
  ptrPt->print();
  clone.print();

  std::println("pt.isSameObject(p2): {}", pt.isSameObject(p2));
  std::println("pt.isSameObject(refPt): {}", pt.isSameObject(refPt));
  std::println("pt.isSameObject(*ptrPt): {}", pt.isSameObject(*ptrPt));
  std::println("pt.isSameObject(clone): {}", pt.isSameObject(clone));
}

void example07_static()
{
  std::println("Point::getCounts() = {}", Point::getCounts());

  Point p1(2, 3);
  Point p2(4, 5);
  // Both return the same value: counts is shared by all instances
  // Works, but calling a static method on an instance is misleading.
  // Prefer: Point::getCounts()
  std::println("p1.getCounts() = {}", p1.getCounts());
  std::println("p2.getCounts() = {}", p2.getCounts());

  std::println("Point::getCounts() = {}", Point::getCounts());
}

void example08_friend()
{
  Point p1(7, 9);
  p1.print();

  Point p2(3, 4);
  double d = distance(p1, p2);
  std::println("distance(p1, p2) = {}", d);
}

void example09_returnRef()
{
  // X() returns a reference: allows direct modification
  // Convenient, but use with care (see header comment)
  Point p1(1, 1);
  p1.X()++;
  p1.Y() += 10;
  p1.print();
}

void example10_constGet()
{
  // p1 cannot be changed afterwards
  const Point p1(1, 1);
  // GCC: error: passing 'const Point' as 'this' argument discards qualifiers
  // p1.setX(10);
  p1.getX();
}

void example11_pointArray()
{
  // Use default CTor
  Point p3[10];
  // Use Point(int, int), then use default CTor
  Point p4[4] = {Point(5, 3)};

  auto *p5 = new Point(6, 3);
  delete p5;
  p5 = nullptr;

  auto *p6 = new Point[10];
  for (int i = 0; i < 10; i++)
  {
    p6[i] = Point(2, 3);
  }
  delete[] p6;
  p6 = nullptr;

  std::vector<Point> v(10, Point(2, 3));
}

int main()
{
  example01_basic();
  example02_conversion();
  example03_constructors();
  example04_copyConstructor();
  example05_destructor();
  example06_this();
  example07_static();
  example08_friend();
  example09_returnRef();
  example10_constGet();
  example11_pointArray();

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_02.02_CTorsMisc" >}}
**`A.h`**
<!-- SNIPPET:BEGIN source_file=A.h id=1242.2_Examples_02.02_CTorsMisc_A.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp

#pragma once

// GCC: use compiler flag -Wshadow to get shadowing warnings
class A
{
public:
  A() = default;
  // GCC warning: declaration of 'value' shadows a member of 'A'
  explicit A(int value) : value(value) {}
  // Expressions in initializer list are ok
  A(int value1, int value2) : value(add(value1, value2)) {}
  // Members are initialized in the order of their declaration!!!
  // -> value = 10, then angle = 20
  // GCC warning: 'A::angle' will be initialized after
  A(int otherValue, [[maybe_unused]] double otherAngle) : angle(value + 10),
                                                          value(otherValue) {}
  // No copy allowed
  A(const A &other) = delete;
  int add(int a, int b) const { return a + b; }

  int getValue() const { return value; }
  double getAngle() const { return angle; }

private:
  int value{0};
  double angle{0.0};
};
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_02.02_CTorsMisc_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp

#include "A.h"

#include <print>

int main()
{
  A a1; // default constructor
  std::println("a1: value={}, angle={}", a1.getValue(), a1.getAngle());
  A a2(1); // constructor with one parameter
  std::println("a2: value={}, angle={}", a2.getValue(), a2.getAngle());
  A a3(1, 2); // constructor with two parameters
  std::println("a3: value={}, angle={}", a3.getValue(), a3.getAngle());
  A a4(1, 2.0);
  std::println("a4: value={}, angle={}", a4.getValue(), a4.getAngle());
  // GCC: error: use of deleted function 'A::A(const A&)'
  // auto a5 = a4;

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}


## Série 2.1

### Exercice 1 : classe compte bancaire
On veut développer un programme de gestion d’un compte bancaire.
Pour cela, implémenter une classe **`BankAccount`**, avec laquelle on puisse :
- initialiser le montant à zéro
- déposer de l'argent (il faut vérifier que le montant déposé soit positif)
- retirer de l’argent (il faut vérifier que le montant retiré soit positif et pas supérieur au montant disponible sur le compte)

**La classe peut être définie dans le fichier main.cpp**

Avec le programme `main` ci-dessous :

```cpp
int main()
{
  BankAccount myBankAccount;
  myBankAccount.show();
  myBankAccount.withdraw(100);    // ERROR
  myBankAccount.show();
  myBankAccount.deposit(100);
  myBankAccount.show();
  myBankAccount.withdraw(200);    // ERROR
  myBankAccount.show();
  myBankAccount.withdraw(20);
  myBankAccount.show();

  return 0;
}
```

Le résultat sera le suivant:

```
The amount on your bank account is : 0.00
The amount on your bank account is : 0.00
The amount on your bank account is : 100.00
The amount on your bank account is : 100.00
The amount on your bank account is : 80.00
```

### Exercice 2 : classe Time
Créer une classe **`Time`** permettant de manipuler des mesures de temps (heure, minute) selon le diagramme UML suivant :

{{<plantuml id="chap2_exo1_2">}}
@startuml

skin rose
skinparam defaultFontSize 20
skinparam classFontStyle bold
skinparam classAttributeIconSize 0
hide circle

class Time
  {
    - h : int
    - m : int
    + getHour() : int
    + getMinute() : int
    + setHour(int) : void
    + setMinute(int) : void
    + show() : void
    + Time()
    + Time(int h, int m)
    + Time(double realTime)
  }
@enduml
{{</plantuml>}}

Elle disposera donc :
- des attributs privés : **`hour`**, **`minute`**
- des constructeurs : par défaut (-->12H00), standard, et de conversion (5.75 --> 5H45')
- des accesseurs : **`getHour()`**, **`getMinute()`**
- des modificateurs : **`setHour(h)`**, **`setMinute(m)`** qui valideront l'argument avant de modifier l'objet
- de la méthode **`show()`** qui affichera heures et minutes avec 2 digits : ("18H45")

**Suggestion :** utiliser une horloge comptant sur 24 heures. Les valeurs excessives (>23, >59) seront remplacées par la valeur maximum possible. Les valeurs négatives seront considérées comme 0.

{{<a_noter>}}
La classe sera déclarée et définie dans des fichiers distincts : **`Time.h`**, **`Time.cpp`** 
{{</a_noter>}}

Tester cette classe dans un programme qui : 
- appelle les différents constructeurs
- utilise les méthodes pour régler une heure à 16h33, ou à 16h87
- utilise accesseurs et modificateur pour augmenter un objet **`Time`** de 5 minutes
- affiche les objets **`Time`** avec la méthode **`show`**

**Exemple d'utilisation :**
```cpp
Time t1;
Time t2(8,15), t3(11.25);

...
t1.setHour(36);
t1.show();
``` 

{{<notion_avancee>}}
Modifier la logique de contrôle de la validité des arguments aussi bien à la construction qu'à la modification d'un objet pour corriger une valeur excessive en reportant (minutes --> heures, bouclement des heures sur 24).
{{</notion_avancee>}}

### Exercice 3 : classe Point

1) En s’inspirant des exemples du cours, concevoir puis implémenter une classe **`Point`** permettant de manipuler un point dans le plan.
Cette classe est résumé dans le diagramme UML suivant :

{{<plantuml id="chap2_exo3">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
hide circle

class Point
{
  - x : double
  - y : double
  - label : char
  + show() : void
  + translate (double dx, double dy) : void
  + Point (char name, double x = 0, double y = 0)
}

@enduml
{{</plantuml>}}

Un point sera caractérisé par un label et ses coordonnées dans le plan.
La classe **`Point`** disposera des méthodes suivantes :
- un constructeur qui permette de créer un point avec un label et de manière optionnelle spécifier ses coordonnées x,y (0 par défaut)
- une méthode **`show()`** qui affiche le nom du point et ses coordonnées
- une méthode **`translate()`** qui prend en arguments les composantes du vecteur de translation et modifie les attributs du point courant en conséquence.

{{<a_noter>}}
La classe sera déclarée et définie dans des fichiers distincts: **`Point.h`**, **`Point.cpp`**
{{</a_noter>}}

2) Écrire une fonction **`main()`** permettant de tester la classe **`Point`** avec :

- instanciation de points avec chacun des constructeurs : **`Point p1`**, **`Point p2('A', 3, 4)`**
- affichage des points
- translation de l'un des points et nouvel affichage
- instanciation **dynamique** d'un objet point (syntaxe C++), et stockage de son adresse dans un pointeur
- affichage de ce point
- suppression de ce point (récupération de la mémoire)

{{<notion_avancee>}}
Écrire la fonction **`Point** generatePolygon(int n)`** qui instancie dynamiquement autant de points que nécessaire à la réalisation d'un **polygone régulier** à n côtés, dont les points sont à une distance unitaire de l'origine.
Par exemple : triangle(n=3), hexagone(n=6), ...
La fonction renvoie un pointeur sur le tableau de pointeurs alloué dynamiquement qui contient les n pointeurs.
Libérer la mémoire des points créés et du tableau de pointeurs avant la fin du programme.
Note : le premier point sera toujours en (1;0), le second illustré en rouge (à un angle de 120°, 90°, ..., 60° du premier, etc.).
{{</notion_avancee>}}

## Série 2.2

### Exercice 1 : classe Point améliorée
Reprendre la classe **`Point`** de la série 2.1 et la compléter avec les éléments suivants :
- une variable membre _statique_ privée **`counter`** initialisée à 0 qui sera incrémentée dans **tous** les constructeurs et décrémentée dans le destructeur de la classe
- une méthode _statique_ publique **`getCounter()`** qui permettra au programme **`main`** d'afficher la valeur de **`counter`**
- Un destructeur **`~Point()`**

Son diagramme de classe UML sera donc :

{{<plantuml id="chap2_exo2_2">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
hide circle

  class Point
  {
    - x : double
    - y : double
    - {static} counter: int
    - label : char
    + show() : void
    + {static} getCounter() : int
    + translate (double dx, double dy) : void
    + Point (char name, double x, double y)
    + ~Point()
  }
@enduml
{{</plantuml>}}

- Compléter le programme pour créer des objets **`Point`** et afficher la valeur du compteur.
Vérifier en particulier qu'à la fin du programme il n'y ait plus d'objets **`Point`** en mémoire grâce au compteur (encapsuler **`main`** dans une paire de { } supplémentaire). 

Par exemple :

```cpp

...

int main()
{
    Point *ptrPoint = nullptr;
    {
        Point p1('A');
        Point p2('B', 3, 4);
        
        // 1. Afficher le nombre de points avec getCounter() (doit afficher 2)

        // 2. Créer dynamiquement un point et mettre son adresse dans le pointeur

        // 3. Afficher le nombre de points (doit afficher 3)

    }   // fin du bloc --> p1 et p2 sont détruits ici

        // 4. Afficher le nombre de points (doit afficher 1)

    delete ptrPoint;    // destruction du point alloué dynamiquement
    ptrPoint = nullptr;

        // 5. Afficher le nombre de points (doit afficher 0)

    return 0; 
}
```

### Exercice 2 : classe Rectangle (composition de points)
Une **composition** est une relation très forte.
Quand l'objet est détruit, les éléments qui le composent doivent aussi être détruits (si je détruis ma maison, les pièces qui la composaient sont détruites).

En s’appuyant sur la classe **`Point`**, réaliser la classe **`Rectangle`**.

Un **rectangle** sera composé de 2 **points** : son coin inférieur gauche **`cornerLL`** et son coin supérieur droit **`cornerUR`**.

La classe possèdera les méthodes : 
- **`contains(const Point& p)`** : renvoie **`true`** si le point **`p`** est à l’intérieur du rectangle
- **`getPerimeter()`** : retourne le périmètre du rectangle
- **`show()`** : affiche les informations du rectangle (coordonnées des coins et périmètre)
- **`translate(double dx, double dy)`** : translate les deux points du rectangle

ainsi que 2 constructeurs :
- **`Rectangle(double xLL, double yLL, double xUR, double yUR)`**
- **`Rectangle(const Point& cornerLL, const Point& cornerUR)`**

**À faire** :

- Donner le diagramme UML de la classe **`Rectangle`**
- Implémenter la classe **`Rectangle`** en s'appuyant sur la classe **`Point`**
- Ne pas oublier le mot-clef **`const`** pour les méthodes constantes (ex. **`void show() const`**).
- Écrire un programme pour tester la classe **`Rectangle`**.
Le programme construira un objet rectangle avec chacun des constructeurs, les affichera avec **`show()`**, utilisera ses méthodes, puis modifiera les arguments de constructions donnés en paramètre aux constructeurs et les affichera à nouveau.

**Question :** comment donner accès aux coordonnées des points aux fonctions de **`Rectangle`** ?

**Question :** est-il possible de construire un rectangle à partir d'un autre ? Essayer et afficher le nouveau rectangle pour voir si cela fonctionne bien.

**Exemple d´extrait de programme :**

```cpp
Point pt1('A', 5., 5.), pt2('B', 10., 12.), ptX('X', 7., 8.);
Rectangle R(pt1, pt2);
R.show();
std::println("Périmètre : {}", R.getPerimeter()); // 24
std::println("is ptX contained in the area of rectangle R ? {}",  R.contains(ptX));
pt1.translate(3,5);
R.show();
std::println("Périmètre : {}", R.getPerimeter()); // ??
// construire un rectangle R2 à partir de R et l'afficher
```

### Exercice 3 : classe RectangleAgreg (agrégation de points)
Une **agrégation** est une relation moins forte qu'une **composition**.
Quand l'objet est détruit, les éléments qui y étaient associés continuent à exister (si une entreprise disparait, on ne liquide pas ses employés !).

En s’appuyant sur la classe **`Point`**, réaliser la classe **`RectangleAgreg`**.

Un **`RectangleAgreg`** sera associé à 2 points par les pointeurs : **`ptrLLCorner`** et **`ptrURCorner`**.

La classe possèdera les méthodes : **`show()`** , **`getPerimeter()`**, et **`translate(double dx, double dy)`**

La classe **`RectangleAgreg`** offrira un constructeur :
- **`RectangleAgreg(Point* cornerLL, Point* cornerUR)`**

**À faire :**
- implémenter la classe **`RectangleAgreg`** en s'appuyant sur la classe **`Point`**
- écrire un programme qui :
  - crée deux points
  - agrège les deux points pour construire le rectangle **`R`** de classe **`RectangleAgreg`**
  - utilise **`translate(dx, dy)`** sur un des points 
  - affiche le rectangle et les points avec **`show()`**; qu'observez-vous ?
  - crée un second **`RectangleAgreg`** copie du rectangle original avec la déclaration **`RectangleAgreg copyR(Ra1);`**
  - utilise **`translate`** sur un des deux rectangles puis affiche les deux rectangles; qu'observez-vous ?

### Exercice 4 : classe RectangleComp (composition de points avec copie en profondeur)
En vous basant sur la classe **`RectangleAgreg`**, réaliser la classe **`RectangleComp`** qui est une composition de points avec copie en profondeur.
  
**En particulier, il faut :**
- supprimer la dépendance (le lien observé entre les deux rectangles) : implémenter le constructeur par copie **`RectangleComp(const RectangleComp&)`** et le **destructeur** **`~RectangleComp()`** qui utilisent l'allocation dynamique pour faire une **copie en profondeur** des éléments associés au rectangle original (ses points).
Enfin, exécuter à nouveau le programme et vérifier que le problème soit résolu (les rectangles peuvent être translatés **indépendamment**).

