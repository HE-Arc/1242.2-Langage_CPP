---
title: "2. Des classes et des objets"
type: docs
weight: 10
---

# Chapitre 2 : des classes et des objets

## Série 2.1

### Exercice 1 : CLASSE Compte bancaire
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
  myBankAccount.init();
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

{{< plantuml id="chap2_exo1_2">}}
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
    + setHour() : void
    + setMinute(int) : void
    + show() : void
    + Time()
    + Time (int h, int m)
    + Time (double realTime)
  }
@enduml
{{< /plantuml >}}

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

{{< plantuml id="chap2_exo3">}}
@startuml
skin rose
skinparam classAttributeIconSize 0

class Point
{
  - x : double
  - y : double
  + label : char
  + show() : void
  + translate (double dx, double dy) : void
  + Point (char name, double x, double y)
}

@enduml
{{< /plantuml >}}

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

{{< plantuml id="chap2_exo2_2">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
  class Point
  {
    - x : double
    - y : double
    - {static} counter: int
    + label : char
    + show() : void
    + {static} getCounter() : int
    + translate (double dx, double dy) : void
    + Point (char name, double x, double y)
    + ~Point()
  }
@enduml
{{< /plantuml >}}

- Compléter le programme pour créer des objets **`Point`** et afficher la valeur du compteur.
Vérifier en particulier qu'à la fin du programme il n'y ait plus d'objets **`Point`** en mémoire grâce au compteur (encapsuler **`main`** dans une paire de { } supplémentaire). 

Par exemple :

```cpp
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

    cout << "\n\nPlease hit ENTER to continue... ";
    cin.get();

    return 0; 
}
```

### Exercice 2 : classe Rectangle (composition de points)
Une **composition** est une relation très forte.
Quand l'objet est détruit, les éléments qui le composent doivent aussi être détruits (si je détruis ma maison, les pièces qui la composaient sont détruites).

En s’appuyant sur la classe **`Point`**, réaliser la classe **`Rectangle`**.

Un **rectangle** sera composé de 2 **points** : son coin supérieur gauche **`cornerUL`** et son coin inférieur droit **`cornerBR`**.

La classe possèdera les méthodes : 
- **`contains(const Point& p)`** : renvoie **`true`** si le point **`p`** est à l’intérieur du rectangle
- **`getPerimeter()`** : retourne le périmètre du rectangle
- **`show()`** : affiche les informations du rectangle (coordonnées des coins et périmètre)
- **`translate(int, int)`** : translate les deux points du rectangle

ainsi que 2 constructeurs :
- **`Rectangle(int xUL, int yUL, int xBR, int yBR)`**
- **`Rectangle(const Point& cornerUL, const Point& cornerBR)`**

**À faire** :

- Donner le diagramme UML de la classe **`Rectangle`**
- Implémenter la classe **`Rectangle`** en s'appuyant sur la classe **`Point`**
- Ne pas oublier le mot clé **`const`** pour les méthodes constantes (ex. **`void show() const`**).
- Écrire un programme pour tester la classe **`Rectangle`**.
Le programme construira un objet rectangle avec chacun des constructeurs, les affichera avec **`show()`**, utilisera ses méthodes, puis modifiera les arguments de constructions donnés en paramètre aux constructeurs et les affichera à nouveau.

**Question :** comment donner accès aux coordonnées des points aux fonctions de **`Rectangle`** ?

**Question :** est-il possible de contruire un rectangle à partir d'un autre ? Essayer et afficher le nouveau rectangle pour voir si cela fonctionne bien.

**Exemple d´extrait de programme :**

```cpp
Point pt1('A', 5., 5.), pt2('B', 10., 12.), ptX('X', 7., 8.);
Rectangle R(pt1, pt2);
R.show();
cout << "Périmètre : " << R.getPerimeter() << endl; // 24
cout << "is ptX contained in the area of rectangle R ? " <<  R.Contains(ptX) << endl;
pt1.translate(3,5);
R.show();
cout << "Périmètre : " << R.getPerimeter() << endl; // ??
// construire un rectangle R2 à partir de R et l'afficher
```

### Exercice 3 : classe RectangleAssoc (association de points)
Une **association** est une relation moins forte qu'une **composition**.
Quand l'objet est détruit, les éléments qui y étaient associés continuent à exister (si une entreprise disparait, on ne liquide pas ses employés !).

En s’appuyant sur la classe **`Point`**, réaliser la classe **`RectangleAssoc`**.

Un **`RectangleAssoc`** sera associé à 2 points par les pointeurs : **`ptrULCorner`** et **`ptrBRCorner`**.

La classe possèdera les méthodes : **`show()`** , **`getPerimeter()`**, et **`translate(int, int)`**

La classe **`RectangleAssoc`** offrira un constructeur :
- **`RectangleAssoc(Point* cornerUL, Point* cornerBR)`**

**À faire :**
- implémenter la classe **`RectangleAssoc`** en s'appuyant sur la classe **`Point`**
- écrire un programme qui :
  - crée deux points
  - associe les deux points pour construire le rectangle **`R`** de classe **`RectangleAssoc`**
  - utilise **`translate(dx, dy)`** sur un des points 
  - affiche le rectangle et les points avec **`show()`**; qu'observez-vous ?
  - crée un second **`RectangleAssoc`** copie du rectangle original avec la déclaration **`RectangleAssoc copyR(Ra1);`**
  - utilise **`translate`** sur un des deux rectangles puis affiche les deux rectangles; qu'observez-vous ?
  
**Puis :**
- supprimer la dépendance (le lien observé entre les deux rectangles) : implémenter le constructeur par copie **`RectangleAssoc(const RectangleAssoc&)`** et le **destructeur** **`~RectangleAssoc()`** qui utilisent l'allocation dynamique pour faire une **copie en profondeur** des éléments associés au rectangle original (ses points).
Enfin, exécuter à nouveau le programme et vérifier que le problème soit résolu (les rectangles peuvent être translatés **indépendamment**).

**Exemple :**

```cpp
Point pt1('A', 5, 5), pt2('B', 10, 12);

// partie 1
RectangleAssoc R( &pt1, &pt2);
R.show();   // OK
pt1.translate(3,5);
R.show();   // ?!? grmph

// partie 2
RectangleAssoc copyR(R);
R.translate(-5,-5);
R.show();       // OK
copyR.show();   // ?!? grmph    --> :) après complétion de l'exercice
```



## Solutions
<!-- [Serie2_1_1_SOLUTIONS](/zips/Serie2_1_1_SOLUTIONS.zip)

[Serie2_1_2_SOLUTIONS](/zips/Serie2_1_2_SOLUTIONS.zip)

[Serie2_1_3_SOLUTIONS](/zips/Serie2_1_3_SOLUTIONS.zip)

[Serie2_2_1_SOLUTIONS](/zips/Serie2_2_1_SOLUTIONS.zip)

[Serie2_2_2_SOLUTIONS](/zips/Serie2_2_2_SOLUTIONS.zip)

[Serie2_2_3_SOLUTIONS](/zips/Serie2_2_3_SOLUTIONS.zip) -->

## Slides
{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/02_Des_classes_et_des_objets.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/02_Des_classes_et_des_objets.html?print-pdf)
