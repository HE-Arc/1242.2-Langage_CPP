---
title: "Projet Fil Rouge Version Libre"
type: docs
weight: 10
---

# Projet Fil Rouge (version libre)

À partir de cette semaine, ce sera à vous de progresser dans le mini-projet.
Ce document fixe les lignes directrices pour ce projet.

L'objectif du mini-projet est de poursuivre le développement de l'exercice "fil rouge" en ajoutant un système de trading, de combat ou un système d'exploration.Vous pouvez venir avec une idée à vous, mais elle **doit impérativement** être validée par le professeur.

Vous **devez** utiliser GitLab.

Le projet devra être avancé chaque semaine dans les périodes du cours et complété avec du travail à la maison.

## Remarques générales
- Le projet doit être fonctionnel, codé selon les meilleures pratiques et les conventions établies.
- Poussez votre solution sur le gitlab, ajoutez des commits (avec des messages significatifs) **chaque semaine**.
- L'exécution du fichier ```main.cpp``` doit fournir un bon aperçu des fonctionnalités implémentées dans votre projet (avec ou sans interaction avec l'utilisateur).

## Livrables du projet
- Code du projet (.hpp, .cpp et fichiers de log)
- Un document texte (.md, .docx ou .pdf) décrivant le code réalisé (1-2 pages)

Le tout doit être dans le GitLab du projet.

## Deadline
Dernier jour du semestre à 23h59.

## Scénarios
Ci-dessous, vous pouvez trouver 3 scénarios possibles à suivre comme ligne directrice pour votre implémentation.
Vous pouvez également proposer votre propre scénario, mais il doit être validé par le professeur.
Dans ce cas, votre projet devra contenir au moins les éléments listés par la suite.

### Minimal requirements

- Une hiérarchie de classes avec à la base une classe abstraite
- L'utilisation d'au moins une surcharge d'opérateurs
- L'utilisation d'au moins une exception
- L'utilisation effective du polymorphisme par la redéfinition de méthodes et l'utilisation de pointeurs ou de références
- L'utilisation de code C++ moderne et de conteneurs de la STL
- La création d'un fichier log qui enregistre les actions importantes du programme durant son utilisation
- Le programme devra être fonctionnel et utiliser les classes développées

## Scénario 1 - Trading System

### Objectifs généraux 
Ajouter la possibilité d'acheter et de vendre des objets et obtenir ou consommer de l'```Or``` :
- de / vers d'autres héros
- de / vers PNJs (classe ```Merchant```)

### Minimal requirements

Vous devrez :
- Ajouter 2 classes (types de marchants : ex. _potion vendors_ ou _weapon vendors_)
- Développer une solution de trading
- Utiliser au moins une _exception_ pour gérer une erreur
- Ajouter un fichier de log pour garder trace de toutes les transactions
- Améliorer la classe "Backpack"
- Utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- Utiliser du code C++ moderne (C++11 ou suivants)

## Scénario 2 - Interaction/Fighting System

### Objectifs généraux
Créer le système de combat pour le jeu de rôle.
Pour cela il sera nécessaire de :
- Ajouter des monstres
- Développer un système de combat (avec un peu d'aléatoire)
- Quand un hitpoints est <= 0 un personnage/monstre est vaincu
- La victoire donne : de l'expérience et un peu d'argent

Obligatoire :
- Hero Vs Monster

Optionnel :
- PVP (Hero Vs Hero)
- Un ou plusieurs ```Hero``` Vs un ou plusieurs ```Monsters```

### Minimal requirements

Vous devrez :
- Ajouter 2 classes (types de monstres : ex. ```Orc``` ou ```Dragon```)
- Utiliser des _Exceptions_ pour gérer les erreurs
- Ajouter un fichier de log pour garder trace de tous les combats
- Ajouter différents types de armes ou différents types d’attaque 
- Utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- Utiliser du code C++ moderne (C++11 ou suivants)

## Scénario 3 - Exploration System

### Objectifs généraux
Créer la possibilité d'explorer une carte avec des villages ou de donjons à explorer.

- Ajouter un système de coordonnées
- Ajouter l'objet ```World``` ou ```Map```
- Ajouter l'interaction avec des objets dans le monde (ex. villages, trésors, PNJ, etc.)

### Minimal requirements

Vous devrez : 
- Ajouter la classe ```World``` (ou ```Map```)
- Ajouter un système de coordonnées et la possibilité de se déplacer dans le monde.
- Ajouter la possibilité pour les héros d'interagir avec des 3 types entités (ex. villages, trésors, PNJ, etc.)
- Ajouter des contraintes pour le déplacement (vitesse maximale, notion du temps, ...)
- Utiliser des _Exceptions_ pour gérer les erreurs
- Ajouter un fichier de log pour garder trace de tous les déplacements
- Utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- Utiliser du code C++ moderne (C++11 ou suivants)

## Un point final
Cherchez à prendre du plaisir dans le développement et la création de votre jeu !
