---
title: "Surcharge des opérateurs : bonnes pratiques"
author: "Benoit Le Callennec"
date: 2025-03-14
tags : ["C++", "Opérateurs", "Bonnes pratiques"]
draft: true
---

## ```operator=``` : l'opérateur d'affectation
- Défini comme membre de la classe
- Retourne une référence vers l'objet courant



The assignment (=), subscript ([]), call (()), and member access arrow (->) operators must be defined as members. • The compound-assignment operators ordinarily ought to be members. However, unlike assignment, they are not required to be members. • Operators that change the state of their object or that are closely tied to their given type—such as increment, decrement, and dereference—usually should be members. • Symmetric operators—those that might convert either operand, such as the arithmetic, equality, relational, and bitwise operators—usually should be defined as ordinary nonmember functions.

