---
title: "3. Surcharge des opérateurs"
type: docs
weight: 10
---

# Chapitre 3 : surcharge des opérateurs

## Slides

{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/03_Surcharge_des_operateurs.html">}}


[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/03_Surcharge_des_operateurs.html?print-pdf)

## Série 3.1

### Exercice 1 : classe **`Time`** surcharge 
Reprendre la classe **`Time`** de l'exercice 2 de la série 2.1, et :

1. surcharger l'opérateur d'insertion de flux **`operator<<()`** afin de pouvoir afficher un temps  **`cout << t << endl;`**
2. surcharger l'opérateur d'affectation **`operator=()`**
3. surcharger les opérateurs arithmétiques :
   1. l’opérateur **`+`** doit être implémenté par une fonction non membre de la classe et amie
   2. l’opérateur **`-`** doit être implémenté par une fonction membre de la classe
   Est-ce que toutes les utilisations proposées dans le `main()` sont possibles ? 
   Laquelle de ces deux opération est commutative ?
4. surcharger les opérateurs relationnels
   1. de manière explicite, implémenter :
      1.  l' **`operator==()`** avec des opérateurs logiques
      2.  l' **`operator<()`** en comparant la valeur renvoyée par une méthode privée **`evaluate()`** qui retourne heure*60+minute
   2. en se basant sur ces deux opérateurs, implémenter :
      1. **`operator>=()`**
      2. **`operator<=()`** 
      3. **`operator!=()`**

5. surchargez les méthodes d'incrémentation préfixée et postfixée   
6. implémentez l'opérateur d'insertion de flux, capable de lire un temps sous la forme : 4:45

{{< plantuml id="chap3_exo1.1">}}
@startuml
skin rose
skinparam classAttributeIconSize 0

class Time {
    - hour : short
    - minute : short

+ Time()
+ Time(Int, Int)
+ Time(Int)

+ operator = ( const Time& ) : Time& 

<<friend>> operator + (const Time&, const Time&) : Time
+ operator + (const Time&): Time

- evaluate() : Short

+ operator == ( const Time& ) : Boolean {query}
+ operator <  ( const Time& ) : Boolean {query}
+ operator >= ( const Time& ) : Boolean {query}
+ operator <= ( const Time& ) : Boolean {query}
+ operator != ( const Time& ) : Boolean {query}

+ operator ++ ()    : Time& 
+ operator ++ (Int) : Time 

<<friend>> operator<<(ostream&,  const Time&): ostream& 
<<friend>> operator>>(istream&,  Time&) : istream& 

} 
@enduml
{{< /plantuml >}}

**Exemple de `main()`**
```cpp
#include <iostream>
#include "Time.h"

using namespace std;

int main()
{
     // INSTANTIATION DES OBJETS t1, t2, t3
     //================================================================
     cout << "TEST DES CONSTRUCTEURS :" << endl << endl;

     cout << "Time t1; ";
     Time t1;   // Appel du constructeur par défaut
     t1.show(); //-> t1: 12H00
     cout << "Time t2(10,9); ";
     Time t2(10, 9); // Appel du constructeur standard
     t2.show();      //-> t2: 10H09
     cout << "Time t3(17.75); ";
     Time t3(17.75); // Appel du constructeur de conversion
     t3.show();      //-> t3: 17:45

     // TEST DES MODIFICATEURS
     //================================================================
     cout << endl << "TEST DES MODIFICATEURS :\n\n";
     cout << "t2.setHour(7); ";
     t2.setHour(7);
     t2.show(); //-> t2: 07:09

     cout << "t2.setMinute(-40); ";
     t2.setMinute(-40); // -40 < 0 --> 0
     t2.show();         //-> t2: 07:00

     cout << "t2.setMinute(86); ";
     t2.setMinute(86); // 86 %60 --> 26  et h+1
     t2.show();        //-> t2: 08:26

     cout <<"operateur <<" << endl;
     cout <<"================================================================" <<endl;
     cout << "cout << \"t1: \" << t1 << \" t2: \" << t2 << \" t3 \" << t3 << endl;" << endl;;
     cout << "t1: " << t1 << " t2: " << t2 << " t3 " << t3 << endl << endl;

     cout <<"operateur =" << endl;
     cout <<"================================================================" <<endl;
     cout << "t1: " << t1 << " t2: " << t2 << endl;
     cout << "t1 =t2" << endl;
     t1=t2;
     cout << "t1: " << t1 << " t2: " << t2 << endl << endl;

     cout <<"operateur + (fonction non membre amie)" << endl;
     cout <<"================================================================" <<endl;
     t1.setMinute(0);
     cout << "t1: " << t1 << " t3: " << t3 << endl;
     cout << "t1 = t1 + t3" << endl;
     t1 = t1 + t3;
     cout << "t1: " << t1 << " t3: " << t3 << endl << endl;

     cout << "t3: " << t3  << endl;
     cout << "t3 = t3 + 4" << endl;
     t3 = t3 + 4;
     cout << "t3: " << t3  << endl << endl;

     cout << "t3: " << t3  << endl;
     cout << "t3 = 4 + t3" << endl;
     t3 = 4 + t3;
     cout << "t3: " << t3  << endl << endl;

     cout <<"operateur - (fonction membre)" <<endl;
     cout <<"================================================================" <<endl;

     cout << "t1: " << t1 << " t3: " << t3 << endl;
     cout << "t1 = t1 - t3" << endl;
     t1 = t1 - t3;
     cout << "t1: " << t1 << " t3: " << t3 << endl << endl;

     cout << "t3: " << t3 << endl;
     cout << "t3 = t3 - 1" << endl;
     t3 = t3 - 1;
     cout << "t3: " << t3 << endl<< endl;

     cout << "t3: " << t3 << endl;
     cout << "t3 = 1 - t3 " << endl;
     t3 = 1 - t3; not allowed
     cout << "t3: " << t3 << endl << endl;

    cout <<" == operator overloading" << endl;
    cout <<"================================================================" <<endl;
    std::cout << t1 << " == " << t1 << boolalpha << " : " << (t1==t1) << std::endl;
    std::cout << t1 << " == " << t2 << boolalpha << " : " << (t1==t2) << std::endl;
    // < operator overloading
    std::cout << t1 << " <  " << t1 << boolalpha << " : " << (t1<t1)  << std::endl;
    std::cout << t1 << " <  " << t2 << boolalpha << " : " << (t1<t2)  << std::endl;
    // >= operator overloading
    std::cout << t1 << " >= " << t1 << boolalpha << " : " << (t1>=t1)  << std::endl;
    std::cout << t1 << " >= " << t2 << boolalpha << " : " << (t1>=t2)  << std::endl;
    // != operator overloading
    std::cout << t1 << " != " << t1 << boolalpha << " : " << (t1!=t1)  << std::endl;
    std::cout << t1 << " != " << t2 << boolalpha << " : " << (t1!=t2)  << std::endl << std::endl;


    std::cout << "\n ++ Increment operator \n";
    cout <<"================================================================" <<endl;

    std::cout << "t2: " << t2 << " t3: " << t3 << std::endl;
    std::cout << "t2 = t3++;" << std::endl;
    t2 = t3++;
    std::cout << "t2: " << t2 << " t3: " << t3 << std::endl;
    std::cout << "t2 =  ++t3;" << std::endl;
    t2 =  ++t3;
    std::cout << "t2: " << t2 << " t3: " << t3 << std::endl;


    cout << "Entrez un temps au format hh:mm :";
    cin >> t2;
    std::cout << "t2: " << t2 << std::endl;

     cout << "\n\nPlease hit ENTER to continue... ";
     cin.get();

     return 0;
}
```

#### Cours de C++, 1ère année, HE-Arc
## Serie 3.2: Surcharge des opérateurs


### Exercice 1: Classe Vecteur. Surcharge de << = et []
Implémentez une classe de vecteurs dynamique, dans le sens où les constructeurs doivent allouer dynamiquement la mémoire nécessaire. Les éléments sont de type `double`.
1. Implémentez les constructeurs 
   1. par défaut (pas d'allocation),
   2. standard (le premier argument définit la taille et le second le contenu; par défaut le contenu est nul),
   3. par recopie. 
2. Surchargez les opérateurs suivants:
   1. insertion de flux  `operator << ()`,
   2. affectation  `operator = ()`. Il faut faire une copie en profondeur,
   3. addition `operator + ()`. A déclarer comme fonction amie
   4. accès  `operator [] ()`. Il doit permettre:
      * de lire un élément du vecteur `x=v[4];`
      * de modifier un élément. `v[4]=4;`
  
      Si l'indice est hors du vecteur, l'operateur utilise la première case du vecteur `v[0]`.


``` C++
int main()
{
    Vector v1;
    Vector v2(3);
    Vector v3= Vector(3,10);
    cout << "v1: " << v1 << " v2: " << v2 << " v3: " << v3 << endl << endl;
    
    cout << "v1: " << v1 << " v3: " << v3 << endl;
    cout << "v1=v3;" << endl;
    v1=v3;
    cout << "v1: " << v1 << " v3: " << v3 << endl<< endl;

    cout << "v1: " << v1 << endl;
    cout << "v1[2]=100;" << endl;
    v1[2]=100;
    cout << "v1: " << v1 << endl<< endl;

    cout << "v1[2] " << v1[2] << endl;
    cout << "v3[2] " << v3[2] << endl << endl;
 
    cout << "v1: " << v1 << endl;
    cout << "v1[1000]=200; " << endl;
    v1[1000]=200;
    cout << "v1: " << v1 << endl << endl;

    Vector v4(5,5);
    cout << "v1: " << v1 << " v3: " << v3 << " v4: " << v4 << endl;
    cout << "v1=v3+v4; " << endl;
    v1=v3+v4;
    cout << "v1: " << v1 << " v3: " << v3 << " v4: " << v4 << endl << endl;

    cout << "v1: " << v1 << " v2: " << v2 << " v3: " << v3 << endl;
    cout << "v1=v3+v3; " << endl;
    v1=v3+v3;
    cout << "v1: " << v1 << " v2: " << v2 << " v3: " << v3 << endl << endl;

    return 0;
}
```

## Serie 3.2: surcharge des opérateurs

### Exercice 1 : classe Vecteur, surcharge de <<, =, et []
Implémenter une classe de vecteurs dynamique, dans le sens où les constructeurs doivent allouer dynamiquement la mémoire nécessaire.
Les éléments sont de type **`double`**. En particulier, il faut :
1. implémenter les constructeurs :
   1. par défaut (pas d'allocation)
   2. standard (le premier argument définit la taille et le second le contenu; par défaut le contenu est nul)
   3. par recopie 
2. surcharger les opérateurs suivants :
   1. insertion de flux  **`operator<<()`**
   2. affectation  **`operator=()`**. Il faut faire une copie en profondeur
   3. addition **`operator+()`**. À déclarer comme fonction amie
   4. accès  **`operator[]()`**. Il doit permettre :
      * de lire un élément du vecteur **`x=v[4];`**
      * de modifier un élément. **`v[4]=4;`**
  
      Si l'indice est hors du vecteur, l'operateur utilise la première case du vecteur **`v[0]`**.

**Exemple de `main()`**

```cpp
int main()
{
    Vector v1;
    Vector v2(3);
    Vector v3= Vector(3,10);
    cout << "v1: " << v1 << " v2: " << v2 << " v3: " << v3 << endl << endl;
    
    cout << "v1: " << v1 << " v3: " << v3 << endl;
    cout << "v1=v3;" << endl;
    v1=v3;
    cout << "v1: " << v1 << " v3: " << v3 << endl<< endl;

    cout << "v1: " << v1 << endl;
    cout << "v1[2]=100;" << endl;
    v1[2]=100;
    cout << "v1: " << v1 << endl<< endl;

    cout << "v1[2] " << v1[2] << endl;
    cout << "v3[2] " << v3[2] << endl << endl;
 
    cout << "v1: " << v1 << endl;
    cout << "v1[1000]=200; " << endl;
    v1[1000]=200;
    cout << "v1: " << v1 << endl << endl;

    Vector v4(5,5);
    cout << "v1: " << v1 << " v3: " << v3 << " v4: " << v4 << endl;
    cout << "v1=v3+v4; " << endl;
    v1=v3+v4;
    cout << "v1: " << v1 << " v3: " << v3 << " v4: " << v4 << endl << endl;

    cout << "v1: " << v1 << " v2: " << v2 << " v3: " << v3 << endl;
    cout << "v1=v3+v3; " << endl;
    v1=v3+v3;
    cout << "v1: " << v1 << " v2: " << v2 << " v3: " << v3 << endl << endl;

    return 0;
}
``` 

## Solutions
<!-- [Serie3_1_SOLUTIONS](/zips/Serie3_1_SOLUTIONS.zip) -->

