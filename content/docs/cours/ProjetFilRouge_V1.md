---
title: "Projet Fil Rouge V1"
type: docs
weight: 10
---

# Projet Fil Rouge V1 (~60 minutes)
Vous voici au début de l'aventure !
Le coeur de ce projet est la notion de **héros**. 
```Hero``` (en anglais selon les conventions de codage) sera donc une **classe**.
Cette classe permettra donc de créer plusieurs héros avec des caractéristiques différentes.

Pour commencer, un héros sera défini pas les caractéristiques (attributs) suivantes :

- ```strength```: entier (représente la force de notre personnage)
- ```agility```: entier (représente l'habileté physique du personnage)
- ```intelligence```: entier (capacité à utiliser la magie, et pas uniquement à avoir de bonnes notes en maths)
- ```hp```: double (_hit points_, ou la vie, énergie qui reste à notre personnage)
- ```name```: ```std::string``` (il faut un nom pour appeler le personnage)

Au début, un héros ne pourra faire que 2 actions (méthodes) :
- ```void show()``` : permettra de se décrire (concrètement, d'afficher à la console les attributs ci-dessus)
- ```void interact(const Hero&)``` : pour interagir avec un autre héros

Voici le diagramme de la classe ```Hero```:

{{< plantuml id="hero_1">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
class Hero {
   - strength : int
   - agility : int
   - intelligence : int
   - hp : double
   - name : std::string

   + show() : void
   + interact(const Hero &) : void
   + getAgility(): int
}
@enduml
{{< /plantuml >}}

## Étape 1
- Créer la classe ```Hero``` (fichiers Hero.cpp et Hero.h)
- Implémenter les attributs (en ```private```)
- Ajouter le namespace ```He_Arc::RPG```

## Étape 2
Implémenter les méthodes :
- ```void interact(const Hero &other)``` : pour le moment, que de courtoises présentations. Les deux noms sont affichés.
- ```void show()``` : afficher à la console les attributs d'un héros.

## Étape 3 (constructeurs par défaut/standard)
- Ajouter le constructeur par défaut (sans paramètre) ```Hero()```
- Tous les attributs seront initialisés à zero et le nom sera '_no\_name_'
- Ajouter le constructeur qui permet d'initialiser les différents attributs :
   - ```Hero(int _strength, int _agility, int _intelligence, double _hp, std::string _name)```
   - Dans le fichier _Hero.cpp_, utiliser une liste d'initialisation pour initialiser les attributs de la classe
- Dans le __main__, créer un héro

{{<hint info >}}
**🔍 NOTE**

N'oubliez pas d'utiliser le mot-clé ```const``` quand nécessaire.
{{</hint >}}

La classe ```Hero``` devrait au final ressembler à ceci :

{{< plantuml id="hero_2">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
class Hero {
   - strength : int
   - agility : int
   - intelligence : int
   - hp : double
   - name : std::string
   + show() : void
   + interact(const Hero &) : void
   + getAgility(): int
   + Hero()
   + Hero(const Hero &)
   + Hero(int, int, int, double, std::string)
}
@enduml
{{< /plantuml >}}

## Étape 4
- Instancier 2 héros
- Appeler la méthode ```show()``` pour chaque héros
- Faites interagir les 2 héros

Voici une sortie possible à la console :
 
```
=================
HERO: Gimli
=================
strength: 10
agility: 5
intelligence: 1
HP: 20

=================
HERO: Gandalf
=================
strength: 2
agility: 2
intelligence: 10
HP: 10

Hello valiant Gimli! I'm Gandalf
```

{{<hint warning >}}
**⚠️ ATTENTION**

Pour la V2 ce code doit être fonctionnel ! Toutes les méthodes et attributs sont nécessaires.
{{</hint >}}

## Étape 5
Notre héros devra bien pouvoir se défendre s'il venait à être attaqué.
Pour cela, il faudra l'équiper d'une arme, comme une épée par exemple.
- Créer une épée (classe ```Sword```).
- Une épée est caractérisée par l'attribut ```int damage```.
- Sa valeur est fixée par le constructeur et lue grâce à un getteur. Utiliser les bonnes conventions de codage et ne pas oublier d'utiliser le mot clé ```const``` quand nécessaire (hint: getter).
- Enfin, ajouter l'épée comme attribut à la classe ```Hero``` (pour le moment pas besoin de modifier le constructeur de ```Hero```)

La classe ```Sword``` devrait ressembler à ceci :

{{< plantuml id="sword">}}
@startuml
skin rose
skinparam classAttributeIconSize 0
class Sword {
   - damage : int
   + Sword(damage: int)
   + getDamage(): int {query}
}
@enduml
{{< /plantuml >}}

## Étape 6 (constructeur par copie)
- Dans _hero.h_, écrire la signature du constructeur par copie
- Est-ce qu'un constructeur par copie est nécessaire ?
   - Si votre réponse est "Oui", allez regarder le cours :P
   - Si "Non", mettez en commentaire la ligne de code que vous venez de créer (ou utilisez _=default_ comme vu en cours)
   
## Solutions
[Projet Fil Rouge V1](/zips/FilRouge_V1_SOLUTIONS.zip)
