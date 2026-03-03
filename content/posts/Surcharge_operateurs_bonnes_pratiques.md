---
title: "Surcharge des opérateurs : bonnes pratiques"
author: "Benoit Le Callennec"
date: 2026-03-03
tags : ["C++", "Opérateurs", "Bonnes pratiques"]
draft: false
---

## **`operator=`**

**Membre obligatoire**

Le standard C++ exige que l'**`operator=`** soit défini comme une fonction membre de la classe.

Il doit **retourner `*this`** pour permettre le chaînage (**`a = b = c`**).

Il doit aussi empêcher l'**auto-affectation**.
Sans cette condition, alors on a un UB (Undefined Behavior).

```cpp
NamedPoint& NamedPoint::operator=(const NamedPoint& p)
{
    if (this == &p)
    {
      return *this;
    }

    ...

    return *this;
}
```

{{<a_noter>}}
Cet opérateur est obligatoire pour les classes qui gèrent des ressources dynamiques (pointeurs bruts, allocations).
Dans le cas contraire, alors **`operator= = default`** est suffisant.
{{</a_noter>}}

## **`operator<<`** et **`operator>>`**

**Non-membres obligatoires**

L'opérande de gauche est un **`std::ostream`** ou un **`std::istream`** qui appartient à la bibliothèque standard.
Il est impossible d'ajouter une méthode à ces types.
On les déclare aussi **`friend`** pour leur donner accès aux membres privés.

Ils doivent enfin **retourner le flux** pour permettre le chaînage (**`std::cout << p1 << p2`**) :

```cpp
friend std::ostream& operator<<(std::ostream& s, const Point& p);
friend std::istream& operator>>(std::istream& in, Point& p);
```

En cas d'erreur de lecture dans **`operator>>`**, on le signale avec **`setstate(failbit)`** :

```cpp
std::istream& operator>>(std::istream& in, Point& p)
{
    char c;
    in >> c;
    if (c == '(')
    {
        in >> p.m_x >> c;
        if (c == ',') { in >> p.m_y >> c; if (c == ')') return in; }
    }
    in.setstate(std::ios::failbit);
    return in;
}
```

## **`operator++`** et **`operator--`**

**Membres recommandés**

Ces opérateurs modifient l'état interne de l'objet.

La signature distingue les deux formes par un **paramètre `int` fictif** pour la forme postfixée :

```cpp
Counter& Counter::operator++()
{
    ++m_x;
    return *this;             
}

Counter Counter::operator++(int)
{
    Counter temp(*this);        
    ++m_x;
    return temp;                
}
```

{{<a_noter>}}
On voit qu'il faut préférer utiliser **`++x`** dans les boucles car elle retourne une référence, alors que **`x++`** crée systématiquement un objet temporaire.
{{</a_noter>}}

## Opérateurs arithmétiques : **`+`**, **`-`**, **`*`**, **`/`**

**Non-membres recommandés**

Ces opérateurs doivent supporter la **symétrie des conversions implicites**.
Un opérateur membre ne peut convertir implicitement que l'opérande de ***droite***.
Un opérateur non-membre peut convertir les deux :

```cpp
Complex operator+(const Complex& rhs) const; 
// VS
friend Complex operator+(const Complex& lhs, const Complex& rhs);
```

Ils retournent un **objet par valeur**.
La bonne pratique est de les implémenter en termes de `operator+=` pour éviter la duplication de code :

```cpp
Complex& Complex::operator+=(const Complex& rhs)
{
    m_r += rhs.m_r;
    m_i += rhs.m_i;

    return *this;
}

// Non-membre
Complex operator+(Complex lhs, const Complex& rhs)
{
    return lhs += rhs;
}
```

## Opérateurs de comparaison : **`==`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**

**Non-membres recommandés** 

Pour respecter la symétrie.
Si **`a == b`** fonctionne, alors **`b == a`** doit aussi fonctionner, en particulier lorsque l'un des opérandes doit être implicitement converti.

```cpp
bool operator==(const Time& tm) const { return m_hour == tm.m_hour && m_minute == tm.m_minute; }
bool operator< (const Time& tm) const { return eval() < tm.eval(); }

bool operator!=(const Time& tm) const { return !(*this == tm); }
bool operator>=(const Time& tm) const { return !(*this < tm); }
bool operator<=(const Time& tm) const { return !(tm < *this); }
bool operator> (const Time& tm) const { return tm < *this; }
```

## **`operator[]`**

**Membre obligatoire** 

C'est imposé par le standard C++.
Il faut fournir 2 versions — `const` et non-`const` — pour que l'opérateur fonctionne aussi bien sur des objets modifiables que constants :

```cpp
int& Vector::operator[](int i)
{
    if (i >= 0 && i < m_size) return m_pData[i];
    return m_pData[0]; 
}

const int& Vector::operator[](int i) const
{
    if (i >= 0 && i < m_size) return m_pData[i];
    return m_pData[0];
}
```

## **`operator()`**

**Membre obligatoire**

C'est imposé par le standard C++.
Un objet dont la classe surcharge l'**`operator()`** s'appelle un **foncteur** (*function object*).
Contrairement à une fonction libre, il peut conserver un **état** entre les appels via ses attributs membres :

```cpp
class Linear
{
public:
    Linear(double a, double b) : m_a(a), m_b(b) {}

    double operator()(double x) const { return m_a * x + m_b; }

private:
    double m_a{0};
    double m_b{0};
};

Linear f(2, 1);
std::println("{}", f(4));
```

Les foncteurs sont utilisés par les algorithmes de la STL (**`std::sort`**, **`std::transform`**, etc.) et ont été en grande partie remplacés par les **lambdas** depuis C++11.

## **`operator T()`**

**Membres obligatoires** 

La conversion part de l'objet lui-même (**`this`**) vers un autre type.

```cpp
class Point
{
public:
    operator int()    const { return std::abs(m_x) + std::abs(m_y); }
    operator double() const { return std::abs(m_x) + std::abs(m_y) + 0.01; }
private:
    int m_x{0};
    int m_y{0};
};
```

{{<attention>}}
Depuis C++11, marquer les opérateurs de conversion comme **`explicit`** force l'usage d'un **`static_cast`** et prévient les erreurs silencieuses.
{{</attention>}}

## Références

- [Operator overloading (cppreference)](https://en.cppreference.com/w/cpp/language/operators)
