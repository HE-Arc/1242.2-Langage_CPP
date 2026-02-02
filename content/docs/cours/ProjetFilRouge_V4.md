---
title: "Projet Fil Rouge V4"
type: docs
weight: 10
---

# Projet Fil Rouge V4 (~45 minutes)

## Étape 10 (polymorphisme)
Il est temps de créer une première équipe.
Créez une liste à l'aide de la bibliothèque standard et la classe ```std::list<>``` (contenu dans le header  ```#include <list>```).

Dans le ```main```, utilisez ```std::list<Hero*>``` pour créer votre équipe.
On veut utiliser le polymorphisme ici.
Votre équipe sera donc composée par des **pointeurs** vers des héros.
Utilisez donc le mot clé ```new``` (sans oublier le ```delete```), pour créer les membres de votre équipe (4-5 héros : au moins un ```Wizard```, deux ```Warrior```et un ```Necromancer```).
Utilisez la méthode ```push_back``` pour ajouter les héros à l'équipe, par exemple ```myParty.push_back(pHero1);```.

Pour résumer, il faut :
- créer 4-5 pointeurs vers 4-5 héros
- créer une liste vide à l'aide de ```std::list<>``` ( ne pas oublier ```#include <list> ```)
- ajouter les héros dans votre liste
- afficher les membres de votre _party_ via la méthode ```show() ``` et une boucle - les plus avancés peuvent utiliser ```std::for_each``` par exemple (dans le header ```<algorithm>```) ou le _range-based for loop_

{{<hint warning >}}
**⚠️ ATTENTION**

Il faut bien vérifier que le polymorphisme fonctionne comme attendu.
{{</hint >}}

## Solutions
[Projet Fil Rouge V4](/zips/FilRouge_V4_SOLUTIONS.zip)
