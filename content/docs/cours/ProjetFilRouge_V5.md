---
title: "Projet Fil Rouge V5"
type: docs
weight: 10
---

# Projet Fil Rouge V5 (~1h30)
Ceci est la dernière étape guidée.
Par la suite, ce sera à vous de décider comment faire évoluer ce RPG (combat, exploration, commerce, mécaniques de jeu, etc.).

## Etape 11 (IObject interface)
Il est temps de différencier les objets que nos héros peuvent manipuler.
On ajoutera des boucliers (classe ```Shield```) et des potions (classe ```Potion```).

- ```Potion```, ```Shield```, ```Sword``` sont tous bien des objets.
Ils vont donc hériter de l'interface ```IObject```.
En C++, une **interface** est une classe abstraite dont **toutes les méthodes sont virtuelles pures**.
Créer l'interface ```IObject``` (voir le diagramme des classes).
- Ajouter la classe ```Shield```. Attention à bien redéfinir les méthodes de ```IObject```.
- Ajouter la classe ```Potion```.
- Adapter la classe ```Sword``` à la nouvelle interface.
- Adapter la classe ```Hero```.
Notre héros pourra utiliser une épée, un bouclier ou une potion.
Pour cela, substituez l'attribut ```Sword sword```, avec un attribut plus générique ```IObject * pObject```.
- Modifier les constructeurs des sous-classes de ```Hero``` pour leur donner un objet/arme par défaut. Par exemple, un guerrier aura une épée ou un bouclier, un magicien une potion, etc.

## Etape 12 (Inventaire / Sac à dos)
Nos héros doivent bien stocker leurs objets quelque part.
Un sac à dos va faire l'affaire.
Notre sac à dos, représenté par la classe ```Backpack```, est bien magique parce qu'il peut contenir un nombre illimité d'objets !
Par contre, cela vient avec une forte limitation : il est organisé comme une *pile* et les objets sont empilés l'un sur l'autre.
Pour récupérer le premier objet il faudra donc tout sortir !

- Ajouter la classe ```Backpack```
   - L'implémentation d'une pile dans la bibliothèque standard sera utilisée (```#include <stack>```).
   Le sac à dos pourra contenir tout objet qui implémente l'interface ```IObject``` : ```std::stack<IObject *> mStack```.
   Le type de l'objet est indiqué entre les symboles ```< Type >```
   - La méthode ```pack()``` ajoute un objet dans le sac à dos
   - La méthode ```unpack()``` enlève un objet du sac a dos
   - La méthode ```isNotEmpty()``` retourne ```true``` si le sac à dos n'est pas vide
- Ajouter un sac à dos (vide à la construction) à chaque héros.
- Dans le ```main```, créer 3 épées, 2 boucliers et 2 potions, et mettre le tout dans le sac à dos (dans l'ordre) d'un guerrier.
- Puis, afficher le contenu du sac à dos en le vidant (ne pas oublier de libérer la mémoire).

Voici un diagramme des classes (les sous-classes de ```Hero``` ont été omises.)

{{< plantuml id="V5_Classes">}}
@startuml
skin rose
skinparam classAttributeIconSize 0

class Sword extends IObject
class Shield extends IObject
class Potion extends IObject

Hero o-- IObject
Hero o-- Backpack

abstract class Hero {
   # strength : int
   # agility : int
   # intelligence : int
   # hp : double
   # name : std::string
   # IObject* : pObject
   + Backpack backpack;
   + Hero()
   + Hero(const Hero &) = delete
   + Hero(int, int, int, double, std::string)
   + ~Hero() {virtual}
   + show() : void
   + {abstract} interact(const Hero &) : void
   + operator=(const Hero &) = delete
}

abstract class IObject {
   + ~IObject() = default;
   + {abstract} getName() : std::string {query}
   + {abstract} getFeature() : int {query}
}
note left: the class IObject is <<abstract>> - the methods getName and getFeature are virtual pure (italic)

class Sword {
   - damage : int
   + Sword(damage: int)
   + getFeature(): int {query}
   + getName() : std::string {query}
}

class Shield {
   - solidity : int
   + Shield(solidity: int)
   + getFeature(): int {query}
   + getName() : std::string {query}
}

class Potion {
   - power : int
   + Potion(power: int)
   + getFeature(): int {query}
   + getName() : std::string {query}
}

class Backpack {
        - std::stack<IObject *> mStack;
        + BackPack() = default
        + ~BackPack() = default {virtual}
        + pack(IObject *pObject) : void
        +  *unPack() : IObject
        + bool isNotEmpty() : bool {query}

}
note left: mStack is the contenair of all the objects

@enduml
{{< /plantuml >}}

## Solutions
[Projet Fil Rouge V5](/zips/FilRouge_V5_SOLUTIONS.zip)
