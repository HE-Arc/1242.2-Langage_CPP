---
title: "Projet Fil Rouge V2 — Solutions"
type: docs
weight: 10
draft: false
---

# Projet Fil Rouge V2 — Solutions

## Classe Hero (étape 7 — operator<<)

{{<details "1242.2_Project_V2_FilRouge_Hero" >}}
**`Hero.h`**
<!-- SNIPPET:BEGIN source_file=Hero.h id=1242.2_Project_V2_FilRouge_Hero.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>
#include <ostream>

namespace He_Arc::RPG
{
  class Hero
  {
  public:
    Hero() = default;
    Hero(int strength, int agility, int intelligence, double hp, std::string name);
    virtual ~Hero() = default;

    virtual void show() const;
    void interact(const Hero &other);

    std::string getName() const { return m_name; }
    int getStrength() const { return m_strength; }
    int getAgility() const { return m_agility; }
    int getIntelligence() const { return m_intelligence; }
    double getHp() const { return m_hp; }

    friend std::ostream &operator<<(std::ostream &s, const Hero &p);

  protected:
    int m_strength{0};
    int m_agility{0};
    int m_intelligence{0};
    double m_hp{0};
    std::string m_name{"no name"};
  };

  std::ostream &operator<<(std::ostream &s, const Hero &p);
}
```
<!-- SNIPPET:END -->

**`Hero.cpp`**
<!-- SNIPPET:BEGIN source_file=Hero.cpp id=1242.2_Project_V2_FilRouge_Hero.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  Hero::Hero(int strength, int agility, int intelligence, double hp, std::string name)
      : m_strength(strength), m_agility(agility), m_intelligence(intelligence), m_hp(hp), m_name(name) {}

  void Hero::show() const
  {
    std::println("=================");
    std::println("HERO: {}", m_name);
    std::println("=================");
    std::println("strength: {}", m_strength);
    std::println("agility: {}", m_agility);
    std::println("intelligence: {}", m_intelligence);
    std::println("HP: {}", m_hp);
  }

  void Hero::interact(const Hero &other)
  {
    std::println("Hello valiant {}! I'm {}", other.getName(), m_name);
  }

  // operator<< writes to any ostream (cout, file, stringstream…)
  // std::println(s, …) targets the stream directly — no need for s << endl
  std::ostream &operator<<(std::ostream &s, const Hero &p)
  {
    std::println(s, "=================");
    std::println(s, "HERO: {}", p.m_name);
    std::println(s, "=================");
    std::println(s, "strength: {}", p.m_strength);
    std::println(s, "agility: {}", p.m_agility);
    std::println(s, "intelligence: {}", p.m_intelligence);
    std::println(s, "HP: {}", p.m_hp);

    return s;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Sword (inchangée)

{{<details "1242.2_Project_V2_FilRouge_Sword" >}}
**`Sword.h`**
<!-- SNIPPET:BEGIN source_file=Sword.h id=1242.2_Project_V2_FilRouge_Sword.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>

namespace He_Arc::RPG
{
  class Sword
  {
  public:
    Sword() = default;
    explicit Sword(int damage) : m_damage(damage) {}
    virtual ~Sword() = default;

    std::string getName() const;
    int getPower() const;

  private:
    int m_damage{10};
  };
}
```
<!-- SNIPPET:END -->

**`Sword.cpp`**
<!-- SNIPPET:BEGIN source_file=Sword.cpp id=1242.2_Project_V2_FilRouge_Sword.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  std::string Sword::getName() const
  {
    return "Sword";
  }

  int Sword::getPower() const
  {
    return m_damage;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Programme principal (étape 7)

{{<details "1242.2_Project_V2_FilRouge_main" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Project_V2_FilRouge_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream> // needed for std::cout with operator<<
#include <print>

#include "Hero.h"
#include "Sword.h"

int main()
{
  He_Arc::RPG::Hero aragorn{20, 20, 20, 20,    "Aragorn"};
  He_Arc::RPG::Hero gimli  {10,  5,  1, 20,    "Gimli"};
  He_Arc::RPG::Hero gandalf{ 2,  2, 10, 10,    "Gandalf"};
  He_Arc::RPG::Hero sauron {20, 20, 10, 999.9, "Sauron"};

  gimli.show();         // V1: show()
  std::println("");
  std::cout << gandalf; // V2: operator<<

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
