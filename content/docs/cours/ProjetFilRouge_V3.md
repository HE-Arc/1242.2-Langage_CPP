---
title: "Projet Fil Rouge V3"
type: docs
weight: 10
---

# Projet Fil Rouge V3 (~1h30 minutes)

## Etape 8 (héritage)
- Créer les classes **`Warrior`**, **`Wizard`** et **`Necromancer`** selon le diagramme des classes ci-dessous.
{{<attention>}}
Il faut respecter les noms utilisés ainsi que l'accessibilité des attributs et méthodes (**`private`**, **`protected`** et **`public`**)
{{</attention>}}
Pour le moment, les méthodes **`castSpell`** et **`riseUndead`** affichent du texte ("Fire Ball !!!", par exemple).
Cependant, pour être utilisées, le héros doit avoir assez de point magie (**`mana`** >=2)

- Donner des valeurs par défaut pour les différentes classes (ex. un guerrier aura de la force, un magicien de l'intelligence, etc.)
{{<attention>}}
Il ne faut pas oublier les mots clés ```virtual``` et ```override``` !
{{</attention>}}

## Etape 9 (classe abstraite)
Un héros qui ne soit ni un **`Warrior`**, un **`Wizard`** ou un **`Necromancer`** n'a pas de raison d'être.
Ceci est un bon exemple de classe abstraite.

- Passer la classe **`Hero`** en abstrait (utiliser/modifier la méthode **`interact`**).

Voici le diagramme de classes finale (en omettant les getters et les setters) :

{{< plantuml id="V3_Classes">}}
@startuml
skin rose
skinparam classAttributeIconSize 0

class Warrior extends Hero
class Wizard extends Hero
class Necromancer extends Wizard
Hero o-- Sword

abstract class Hero {
   # strength : int
   # agility : int
   # intelligence : int
   # hp : double
   # name : std::string
   # Sword : sword
   + Hero()   
   + Hero(int, int, int, double, std::string)
   + ~Hero() {virtual}
   + show() : void
   + {abstract} interact(const Hero &) : void
}
note left: Hero is now <<abstract>> and the attributes #protected

class Warrior {
   + Warrior(int, int, int, double, std::string)
   + interact(const Hero &) : void 
}

class Wizard {
   # mana : int
   + Wizard(int, int, int, double, std::string, int)
   + castSpell() : void
   + interact(const Hero &) : void
   + show() : void
}

class Necromancer {
   + Necromancer(int, int, int, double, std::string, int)
   + riseUndeads() : void
}

class Sword {
   - damage : int
   + Sword(damage: int)
   + getDamage(): int
}

@enduml
{{< /plantuml >}}

