---
title: "4. Héritage et polymorphisme"
type: docs
weight: 10
---

# Chapitre 4 : héritage et polymorphisme

## Slides

{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/04_Heritage_et_polymorphisme.html">}}


[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/04_Heritage_et_polymorphisme.html?print-pdf)

## Série 4.1
### Exercice 1 : héritage simple

Écrire une classe **`Pixel`** permettant de manipuler des points colorés.
Une couleur sera représentée par 3 entiers (voir schéma UML), chacun compris entre 0 et 255.
Cette classe disposera de la méthode **`show()`** qui affichera les coordonnées et la couleur d’un point.
Cette classe devra mettre en œuvre la notion d’héritage, en utilisant la classe **`Point`** définie dans la série 2.3.

On donne aussi le diagramme de classe des classes suivant :

{{< plantuml id="chap4_exo1.1">}}
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

Quel sera l’affichage à l’exécution du programme ci-dessous :

```cpp
#include <iostream>

// Just to save some space
using namespace std;

class A
{
protected:
  int na = 0;
public:
  A(int _na)
  {
    na = _na;
    cout << "A constructor " << na << "\n";
  }
};

class B : public A
{
protected:
  int nb = 1;
public:
  B() : A(1)
  {
    cout << "B constructor " << nb << "\n";
  }
};

class C : public A
{
protected:
  int nc = 2;
public:
  C() : A(2) 
  {
    cout << "C constructor " << nc << "\n";
  }
};
```

<div style="page-break-after: always;"></div>

```cpp
class D : public C, public B
{
  int nd = 3;
public:
  D() : C(), B()
  {
    cout << "D constructor " << nd << "\n";
  }
};

int main()
{
  D d;

  cout << "\nPress any key to continue...";
  cin.get();
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

## Solutions
[Serie4_1_SOLUTIONS](/zips/Serie4_1_SOLUTIONS.zip)

[Serie4_2_SOLUTIONS](/zips/Serie4_2_SOLUTIONS.zip)
