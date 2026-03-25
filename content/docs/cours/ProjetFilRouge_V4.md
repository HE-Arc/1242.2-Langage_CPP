---
title: "Projet Fil Rouge V4"
type: docs
weight: 10
---

# Projet Fil Rouge V4 (~45 minutes)

## Étape 10 (polymorphisme)
Il est temps de créer une première équipe.
Créez une liste à l'aide de la bibliothèque standard et la classe **`std::list<>`** (contenu dans le header  **`#include <list>`**).

Dans le **`main`**, utiliser **`std::list<Hero*>`** pour créer une équipe de héros.
On veut utiliser le polymorphisme ici.
L'équipe sera donc composée par de **pointeurs** vers des héros.
Il faut donc utiliser le mot-clef **`new`** (sans oublier **`delete`**), pour créer les membres de l'équipe (4-5 héros : au moins un **`Wizard`**, deux **`Warrior`** et un **`Necromancer`**).
Utiliser la méthode **`push_back`** pour ajouter les héros à l'équipe, par exemple **`myParty.push_back(pHero1);`**.

Pour résumer, il faut :
- créer 4-5 pointeurs vers 4-5 héros
- créer une liste vide à l'aide de **`std::list<>`** ( ne pas oublier **`#include <list>`**)
- ajouter les héros dans la liste
- afficher les membres de **`party`** via la méthode **`show()`** et une boucle - les plus avancés peuvent utiliser **`std::for_each`** par exemple (dans le header **`<algorithm>`**) ou une **`range-based for loop`**

{{<attention>}}
Il faut bien vérifier que le polymorphisme fonctionne comme attendu.
{{</attention>}}
