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

Le projet final est un projet individuel, mais tout au long du semestre vous êtes encouragés à travailler en binôme en modalité [eXtrem Programming (XP)](https://fr.wikipedia.org/wiki/Extreme_programming).

{{< hint warning >}}
**⚠️ ATTENTION**

Si vous voulez que votre code soit compatible avec la version du corrigée, vous devrez suivre les consignes et les conventions de codage (Noms de variables, méthodes, etc.) à la lettre !
{{< /hint >}}

### Git & GitLab
L'utilisation de GitLab est obligatoire. Pour cela, il faut suivre les étapes détaillées ci-dessous.

#### Première séance
1. Créer un repo nommé **`CPP_FilRouge_ISCX_Nom`** (où X sera remplacé par a, b, c, d, e ou j selon votre groupe).
2. Ajouter le professeur et l'assistant avec le rôle de **`Mantainer`**.
3. Initialiser le git avec un readme
4. Faire un **`git clone ...`**.

#### Chaque semaine
Il faut au minimum faire un push significatif de vos modifications par semaine.

Il faut donc utiliser les commandes :
- **`git add ...`**
- **`git commit ...`**
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
- Poussez votre solution sur le gitlab, ajoutez des commits (avec des messages significatifs) *chaque semaine*
- L'exécution du fichier main.cpp doit fournir un bon aperçu des fonctionnalités implémentées dans votre projet (avec ou sans interaction avec l'utilisateur)

### Livrables du projet
- Code du projet (.hpp, .cpp et fichiers de log)
- Un document texte (.md, .docx ou .pdf) décrivant le code réalisé (1-2 pages)

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
Ajouter la possibilité d'acheter et de vendre des objets et obtenir ou consommer de l'```Or``` :
- de / vers d'autres héros
- de / vers des PNJs (classe ```Merchant```)

#### Minimum requis
Vous devrez :
- Ajouter 2 classes (types de marchants : ex. _potion vendors_ ou _weapon vendors_)
- Développer une solution de trading
- Utiliser au moins une _exception_ pour gérer une erreur
- Ajouter un fichier de log pour garder trace de toutes les transactions
- Améliorer la classe "Backpack"
- Utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- Utiliser du code C++ moderne (C++11 ou suivants)

### Scénario 2 - Interaction/Fighting System

#### Objectifs généraux
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

#### Minimum requis
Vous devrez :
- Ajouter 2 classes (types de monstres : ex. ```Orc``` ou ```Dragon```)
- Utiliser des _Exceptions_ pour gérer les erreurs
- Ajouter un fichier de log pour garder trace de tous les combats
- Ajouter différents types de armes ou différents types d’attaque 
- Utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- Utiliser du code C++ modern (C++11 ou suivants)

### Scénario 3 - Système d'exploration

### Objectifs généraux
Créer la possibilité d'explorer une carte avec des villages ou de donjons.

- Ajouter un système de coordonnées
- Ajouter l'objet ```World``` ou ```Map```
- Ajouter l'interaction avec des objets dans le monde (ex. villages, trésors, PNJ, etc.)

### Minimum requis

Vous devrez : 
- Ajouter la classe ```World``` (ou ```Map```)
- Ajouter un système de coordonnées et la possibilité de se déplacer dans le monde.
- Ajouter la possibilité pour les héros d'interagir avec des 3 types entités (ex. villages, trésors, PNJ, etc.)
- Ajouter des contraintes pour le déplacement (vitesse maximale ou notion du temps ou…)
- Utiliser des _Exceptions_ pour gérer les erreurs
- Ajouter un fichier de log pour garder trace de tous les déplacements
- Utiliser le polymorphisme, la redéfinition et la surcharge des méthodes (y.c. des opérateurs)
- Utiliser du code C++ modern (C++11 ou suivants)

## Formulaire d'évaluation
Le projet sera évalué selon les critères détaillés dans le fichier suivant :

[EvaluationFilRouge_2025.xlsx](/EvaluationFilRouge_2025.xlsx)

## Remarque finale
Cherchez avant tout à prendre du plaisir dans le développement et la création de votre solution/monde/monstres !
