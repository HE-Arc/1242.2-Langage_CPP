---
title: "Projet Fil Rouge V0"
type: docs
weight: 10
---

# Projet Fil Rouge V0
**Auteur original**<br>
Prof. Stefano Carino, HE-Arc, mars 2021.

> Un "Fil rouge" est un projet de développement, réalisé sur la durée par les collaborateurs d'une entreprise en parallèle de leur mission principale.
>
> Source : [Wikipedia](https://fr.wikipedia.org/wiki/Fil_rouge)

Le but de cet exercice "Fil Rouge" est de mettre en pratique plusieurs concepts vus dans le cours dans un projet unificateur, cohérent et, surtout, concret.
Le développement se fera par étapes tout le long du semestre (V1, V2, etc.) et il sera poursuivi par un développement personnel (qui sera évalué !).

## Le contexte : Role Playing Game (RPG)

Le but de ce travail est d'utiliser les différentes notions vues en cours pour réaliser le noyau d'un jeu de rôle (personnages, interactions, armes, etc.) qui pourra être continué selon vos envies (à valider avec le professeur).

## Modalités
Chaque semaine, une partie des exercices sera dédiée au developpement de l'exercice "Fil Rouge".
Il faudra de plus atteindre l'objectif donné pour la semaine suivante.

{{< hint info >}}
**🔍 INFORMATION**

Chaque semaine, une correction sera founie.
Vous pouvez l'utiliser pour améliorer/valider votre code (mais vous n'avez pas l'obligation de le suivre à la lettre).
{{< /hint >}}

Le projet final est un projet individuel, mais vous êtes encouragés à collaborer avec les autres.
{{< hint warning >}}
**⚠️ ATTENTION**

Si vous voulez que votre code soit compatible avec la version du corrigée, vous devrez suivre les consignes et les conventions de codage (Noms de variables, méthodes, etc.) à la lettre !
{{< /hint >}}

### Git & GitLab
L'utilisation de GitLab est obligatoire. Pour cela, il faut suivre les étapes détaillées ci-dessous.

#### Première séance
1. Accéder à votre répertoire personnel, dans le groupe de votre classe, sur le GitLab du cours : [1242.2 LanguageCPP](https://gitlab-etu.ing.he-arc.ch/groups/isc/2025-26/niveau-1/1242.2-langagecpp). 
2. Faire un **`git clone ...`**.
3. Si absent, initialiser votre répertoire git avec un README.md

#### Chaque semaine
Il faut au minimum faire un push significatif de vos modifications par semaine.

Il faut donc utiliser les commandes :
- **`git add ...`**
- **`git commit -m ...`**
- **`git push ...`**

{{< hint warning >}}
**⚠️ ATTENTION**

Il faut utiliser des messages de commit pertinents !
Il faut donc éviter les messages du type "update" ou "correction d'un bug" mais plutôt **`DONE Add new spells`** ou encore **`FIXED Bug in monster movements`**.
{{< /hint >}}

{{< hint info >}}
**🔍 À NOTER**

1. L'utilisation régulière de git et de GitLab aura un effect positif sur votre note finale !
2. Il faut suivre les conventions de codage données. On code donc en anglais !
{{< /hint >}}

## Travail libre évalué
L'objectif de ce projet est de poursuivre le développement de l'exercice "fil rouge" en ajoutant un système de trading, de combat ou un système d'exploration.
Vous pouvez venir avec une idée à vous, mais elle **doit impérativement** être validée par le professeur.

Vous **devez** utiliser GitLab.

Le projet devra être avancé chaque semaine dans les périodes du cours et complété avec du travail à la maison.

### Remarques générales
- Le projet doit être fonctionnel, codé selon les meilleures pratiques et les conventions établies.
- Poussez votre solution sur GitLab, ajoutez des commits (avec des messages pertinents) **chaque semaine**
- L'exécution du fichier main.cpp doit fournir un bon aperçu des fonctionnalités implémentées dans votre projet (avec ou sans interaction avec l'utilisateur)

### Livrables du projet
- Code du projet (.h, .cpp et fichiers de log)
- Un document texte (.md, .docx ou .pdf) décrivant le code réalisé (1-2 pages). Le README de votre projet GitLab peut aussi servir de document de description du projet.

Le tout doit être dans le GitLab du projet, sur la branch `main`.

### Deadline
Dernier jour du semestre à 23h59.

## Scénarios
Il y a 3 scénarios possibles pour votre implémentation.
Vous pouvez également proposer votre propre scénario, mais il doit être validé par le professeur.
Dans ce cas, votre projet devra contenir au moins les éléments suivants.

### Minimum requis
- Une hiérarchie de classes avec à la base une classe abstraite
- L'utilisation d'au moins une surcharge d'opérateurs
- L'utilisation d'au moins une exception
- L'utilisation effective du polymorphisme par la redéfinition de méthodes et l'utilisation de pointeurs ou de références
- L'utilisation de code C++ moderne et de conteneurs de la STL
- La création d'un fichier log qui enregistre les actions importantes du programme durant son utilisation
- Le programme devra être fonctionnel et utiliser les classes développées

### Scénario 1 - Trading System

#### Objectifs généraux
Ajouter la possibilité d'acheter et de vendre des objets et obtenir ou consommer des **`Gold`** :
- de / vers d'autres héros
- de / vers des PNJs (classe **`Merchant`**)

#### Minimum requis
Vous devez :
- ajouter 2 classes (types de marchants : ex. _potion vendors_ ou _weapon vendors_)
- développer une solution de trading
- ajouter un fichier de log pour garder trace de toutes les transactions
- utiliser au moins une _exception_ pour gérer une erreur. Par exemple, une exception pour gérer l'impossibilité d'ouvrir le fichier de log.
- améliorer la classe **`Backpack`**
- utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- utiliser du code C++ moderne (C++11 ou suivants)

### Scénario 2 - Interaction/Fighting System

#### Objectifs généraux
Créer le système de combat pour le jeu de rôle.
Pour cela il sera nécessaire de :
- ajouter des monstres
- développer un système de combat (avec un peu d'aléatoire)
- quand un hitpoints est <= 0 un personnage/monstre est vaincu
- la victoire donne de l'expérience et un peu d'argent

Obligatoire :
- **`Hero`** Vs **`Monster`**

Optionnel :
- PVP (**`Hero`** Vs **`Hero`**)
- un ou plusieurs **`Hero`** Vs un ou plusieurs **`Monsters`**

#### Minimum requis
Vous devrez :
- ajouter 2 classes (types de monstres : ex. **`Orc`** ou **`Dragon`**)
- utiliser des _Exceptions_ pour gérer les erreurs
- ajouter un fichier de log pour garder trace de tous les combats
- ajouter différents types de armes ou différents types d’attaque 
- utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- utiliser du code C++ modern (C++11 ou suivants)

### Scénario 3 - Système d'exploration

### Objectifs généraux
Créer la possibilité d'explorer une carte avec des villages ou de donjons.

- ajouter un système de coordonnées
- ajouter l'objet **`World`** ou **`Map`**
- ajouter l'interaction avec des objets dans le monde (ex. villages, trésors, PNJ, etc.)

### Minimum requis

Vous devrez : 
- ajouter la classe **`World`** (ou **`Map`**)
- ajouter un système de coordonnées et la possibilité de se déplacer dans le monde
- ajouter la possibilité pour les héros d'interagir avec des 3 types entités (ex. villages, trésors, PNJ, etc.)
- ajouter des contraintes pour le déplacement (vitesse maximale, notion du temps, etc.)
- ajouter un fichier de log pour garder trace de tous les déplacements
- utiliser des _Exceptions_ pour gérer les erreurs
- utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- utiliser du code C++ modern (C++11 ou suivants)

## Formulaire d'évaluation
Le projet sera évalué selon les critères détaillés dans le fichier suivant :

[EvaluationFilRouge_2025-2026.xlsx]({{<static "EvaluationFilRouge_2025-2026.xlsx">}})


## Remarque finale
Cherchez avant tout à prendre du plaisir dans le développement et la création de votre solution/monde/monstres !
