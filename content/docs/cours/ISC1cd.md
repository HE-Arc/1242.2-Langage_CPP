---
title: "ISC1cd"
weight: 20
---

# ISC1cd
## Oral
L'oral durera 30 minutes.

### Avant l'oral
Avant de passer, il faut absolument :
- Préparer VS Code : être capable de coder, compiler et exécuter du code rapidement.
- Vérifier que l'ordinateur peut être branché au projecteur. Il faut prévoir un adaptateur USB-C → HDMI si nécessaire.
- Ouvrir le code source de ses auto-évaluations dans VS Code.
- Bien relire son code et être capable de l'expliquer (auto-évaluations et exercices).

{{< hint danger >}}
**ATTENTION :** tout le temps perdu au début de l'oral pénalisera la note finale.
{{< /hint >}}

### Pendant l'oral
0) (Optionnel) Discussions sur le coded de votr projet.
1) **[Très simple]** Afficher un entier + compiler + exécuter ⇒ max. 1 minute.
2) Exercice complet ressemblant à celui donné ci-dessous, à coder en direct ⇒ max. 20 minutes.

### Exemple

Écrire un programme qui gère les formes cercle et rectangle. 

#### Classe **`Shape`**
Il faut implémenter la classe **`Shape`** qui contient en particulier la méthode décrite ci-dessous.
- Une méthode **`area()`** qui retourne l’aire de la forme.

#### Classe **`Rectangle`** 
Il faut implémenter la classe **`Rectangle`** qui hérite de la classe **`Shape`**, et qui contient en particulier les éléments décrits ci-dessous.
- Un attribut **`m_length`** de type **`double`**,
- Un attribut **`m_width`** de type **`double`**,
- Une méthode **`area()`** qui retourne l’aire du rectangle. 

#### Classe **`Circle`**
Il faut implémenter la classe **`Circle`** qui hérite de la classe **`Shape`**, et qui contient en particulier les éléments décrits ci-dessous.
- Un attribut **`m_radius`** de type **`double`**,
- Une méthode **`area()`** qui retourne l’aire du cercle.

#### Main
Dans le **`main()`**, il faut les éléments ci-dessous.
- Une liste de **`Shape`** implémentée utilisant le container **`std::vector`**.
Elle doit contenir au moins 2 **`Rectangle`** et 2 **`Circle`**, avec des dimensions différentes.
- Une boucle qui parcourt la liste de **`Shape`** et qui affiche l’aire de chaque forme.
- Une seconde liste de **`Shape`** implémentée utilisant le container **`std::vector`**.
- Les valeurs de la première liste sont copiées dans la seconde liste.
- Une boucle qui parcourt la seconde liste de **`Shape`** et qui affiche l’aire de chaque forme.

### Ce qui est évalué

#### Général
- Éviter les copier-coller
- Ne pas dupliquer du code dans les classes dérivées

#### Création de classe
- Déclarer une classe avec ses attributs et méthodes
- Choisir le bon niveau d'accès : **`private`** par défaut (ou **`protected`**)
- Initialiser les attributs en classe : **`double m_x{0.0};`**
- Marquer les méthodes **`const`** quand elles ne modifient pas l'objet
- Préférer **`#pragma once`** (pas besoin d'**`#ifndef`** / **`#define`** en plus)

#### Constructeurs
- Utiliser la **liste d'initialisation** (`: m_x(x), m_y(y)`), pas le corps du constructeur
- Faire les vérifications nécessaires dans le constructeur (ex. vérifier que les dimensions sont positives)
- Savoir appeler le constructeur de la classe de base depuis la classe dérivée
- Passer les **`std::string`** par **`const std::string&`**

#### Héritage
- Savoir la syntaxe de l'héritage
- Inclure le header de la classe de base dans la classe dérivée
- Appeler une méthode de la classe parente

#### Méthodes virtuelles et polymorphisme
- **Destructeur virtuel obligatoire** dans une classe de base
- Mot-clé **`virtual`** dans la classe de base ; mot-clé **`override`** (sans **`virtual`**) dans la classe dérivée
- Comprendre et savoir expliquer : **méthode virtuelle pure** (`= 0`) et **classe abstraite**
- Savoir stocker des objets polymorphes dans un conteneur (**`std::vector<Shape*>`**)
- Appeler une méthode à partir d'un pointeur sur un objet

#### Conteneurs et boucles
- **`std::vector`** : **`push_back()`**, **`at()`**
- Boucle range-based : **`for (const auto &e : elems) { ... }`**
- Connaître au moins une syntaxe de parcours qui fonctionne (range-for, itérateur ou index)

#### Comportement à l'oral
- **Préparer VS Code en amont** : tout le temps perdu au début pénalise la note
- Pouvoir **expliquer son code** clairement (notamment les concepts : héritage, polymorphisme, virtuelle pure)
- Quand on bloque : essayer, montrer son raisonnement — l'enseignant peut aider, et savoir rebondir avec un indice est valorisé
- Repérer ses propres erreurs (oubli de **`virtual`**, mauvais type de retour, etc.) est très valorisé
- Comprendre les erreurs de compilation et les corriger est très valorisé
