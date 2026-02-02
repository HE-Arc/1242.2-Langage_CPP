---
title: "Projet Fil Rouge V2"
type: docs
weight: 10
---

# Projet Fil Rouge V2 (~20 minutes)

## Étape 7 (surcharges des opérateurs)
Dans cette étape, nous nous limitons à remplacer la méthode ```show()``` par la surcharge de ```operator<<```.
(Gardez la méthode ```show()```, il n'est pas besoin de la supprimer).

- Surcharger l'```operator<<``` pour avoir le même comportement que ```show()```.

## Étape 7.b (optionelle - pas dans le corrigé)
Chaque héros a bien une arme. 
- Changer l'attribut ```Sword``` en pointeur (cela va nous aider plus tard quand on parlera d'héritage).

```cpp
Sword *sword = nullptr;
```

- Adapter le constructeur de ```Hero``` en y ajoutant l'épée.

À cause de ce pointeur, il faut désormais implémenter un constructeur par copie, un destructeur et surcharger l'opérateur d'affectation (```operator=```).

- Implémenter ces 3 méthodes.

## Solutions
[Projet Fil Rouge V2](/zips/FilRouge_V2_SOLUTIONS.zip)
