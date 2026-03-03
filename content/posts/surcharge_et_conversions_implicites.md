---
title: "Surcharge et conversions implicites"
author: "Benoit Le Callennec"
date: 2026-02-19
tags: ["C++", "Avancé"]
draft: false
---

Lorsqu'un appel de fonction ne correspond pas exactement à une signature, le compilateur C++ effectue des **conversions implicites** pour tenter de trouver une correspondance.
Ce mécanisme est au coeur de la résolution de surcharge (*overload resolution*).

### Les 3 rangs de conversion

Le compilateur C++ classe les conversions implicites en 3 rangs, du plus prioritaire au moins prioritaire :

| Rang | Nom | Exemples |
|------|-----|----------|
| 1 | **Exact match** | Aucune conversion, ajout de `const`, lvalue-to-rvalue |
| 2 | **Promotion** | `float` &rarr; `double`, `short` &rarr; `int`, `char` &rarr; `int` |
| 3 | **Conversion** | `double` &rarr; `int`, `double` &rarr; `float`, `int` &rarr; `float` |

### Exemple concret
Considérons deux surcharges :

```cpp
int minimum(int val1, int val2);
float minimum(float val1, float val2);
```

**Avec `minimum(7, 3)`**

Le compilateur trouve un **exact match** (rang 1) pour la version **`int`**, et une conversion de rang 3 pour la version **`float`** (promotion de **`int`** à **`float`**), donc il choisit la version **`int`**.

**Avec `minimum(7.0f, 3.0f)`**
{{<a_noter>}}
Un littéral décimal comme `7.0` est de type **`double`**, pas **`float`**. Pour un littéral **`float`**, il faut écrire `7.0f`.
{{</a_noter>}}

Le compilateur trouve un **exact match** (rang 1) pour la version **`float`**, et une conversion de rang 3 pour la version **`int`** (conversion de **`float`** à **`int`**), donc il choisit la version **`float`**.

{{<attention>}}
**Asymétrie float / double**

La conversion entre **`float`** et **`double`** n'est **pas symétrique**.

- **`float`** &rarr; **`double`** est une **promotion** (rang 2)
- **`double`** &rarr; **`float`** est une **conversion** (rang 3)
{{</attention>}}

**Avec `minimum(7.0, 3.0)`**

Le compilateur trouve une conversion de rang 3 pour la version **`int`** (conversion de **`double`** à **`int`**), et une conversion de rang 3 pour la version **`float`** (conversion de **`double`** à **`float`**), donc il ne peut pas choisir entre les deux &rarr; **erreur d'ambiguïté**.

**Avec `minimum(7.0, 3)`**

Le compilateur trouve une conversion de rang 3 pour la version **`int`** (conversion de **`double`** à **`int`**), et une conversion de rang 3 pour la version **`float`** (conversion de **`double`** à **`float`** + promotion de **`int`** à **`float`**), donc il ne peut pas choisir entre les deux &rarr; **erreur d'ambiguïté**.

## Références

- [Overload resolution (cppreference)](https://en.cppreference.com/w/cpp/language/overload_resolution)
- [Numeric promotions (cppreference)](https://en.cppreference.com/w/cpp/language/implicit_conversion#Numeric_promotions)
- [Numeric conversions (cppreference)](https://en.cppreference.com/w/cpp/language/implicit_conversion#Numeric_conversions)
