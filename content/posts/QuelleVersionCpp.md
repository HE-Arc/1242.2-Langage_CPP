---
title: "Quelle version de C++ pour le cours ?"
author: "Benoit Le Callennec"
date: 2026-02-19
tags : ["C++", "Visual Studio", "Compilateurs"]
draft: false
---

Durant le cours, nous utiliserons le C++23.
Dans certains cas, si la version du compilateur utilisé est trop ancienne, alors certaines fonctionnalités de C++23 ne seront pas disponibles.
À l'inverse, il est aussi possible que certaines "possibilités" aient été enlevées dans les versions les plus récentes du C++.
Par exemple, la possibilité de lire, depuis `std::cin` dans un `char*` a été supprimée depuis C++20, pour des raisons de sécurité (risque de dépassement de buffer).

{{< figure src="images/CPP17VsCPP20.png#center" width="100%">}}
(Source : Compiler Explorer. See full code [here](https://godbolt.org/z/9d3qfx1bK))

Si on considère le code suivant :
```cpp
#include <iostream>

int main()
{
    auto str = new char[100];
    // Removed in C++20
    std::cin >> str;
    delete[] str;
}
```

Avec C++17, ce code compile et fonctionne (même s'il est dangereux).
Avec C++20, ce code ne compile plus, et génère l'erreur suivante :

**MSVC :**
```
error C2679: binary '>>': no operator found which takes a right-hand operand of type 'char *' (or there is no acceptable conversion)
```

**GCC :**
```
error: no match for 'operator>>' (operand types are 'std::istream' {aka 'std::basic_istream<char>'} and 'char*')
```

Avec Visual Studio, il faut donc s'assurer d'utiliser la version C++23, et pas une version plus ancienne.
Pour cela, il faut faire un clic droit sur le projet dans l'explorateur de solutions, puis dans **`Properties`** -> **`General`**, choisir **`Preview - ISO C++23 Standard (/std:c++23preview)`** :

{{< figure src="images/VSProperties.png#center" width="100%">}}
