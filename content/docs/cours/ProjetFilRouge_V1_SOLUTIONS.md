---
title: "Projet Fil Rouge V1 — Solutions"
type: docs
weight: 10
draft: false
---

# Projet Fil Rouge V1 — Solutions

## Classe Hero (étapes 1–4, 6)

### Hero.h

<!-- SNIPPET:BEGIN source_file=Hero.h id=1242.2_Project_V1_FilRouge_Hero.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <string>

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

  protected:
    int m_strength{0};
    int m_agility{0};
    int m_intelligence{0};
    double m_hp{0};
    std::string m_name{"no name"};
  };
}
```
<!-- SNIPPET:END -->

### Hero.cpp

<!-- SNIPPET:BEGIN source_file=Hero.cpp id=1242.2_Project_V1_FilRouge_Hero.cpp -->
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
}
```
<!-- SNIPPET:END -->

## Classe Sword (étape 5)

### Sword.h

<!-- SNIPPET:BEGIN source_file=Sword.h id=1242.2_Project_V1_FilRouge_Sword.h -->
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

### Sword.cpp

<!-- SNIPPET:BEGIN source_file=Sword.cpp id=1242.2_Project_V1_FilRouge_Sword.cpp -->
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

## Programme principal (étape 4)

### main.cpp

<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Project_V1_FilRouge_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>

#include "Hero.h"
#include "Sword.h"

int main()
{
  He_Arc::RPG::Hero aragorn{20, 20, 20, 20, "Aragorn"};
  He_Arc::RPG::Hero gimli{10, 5, 1, 20, "Gimli"};
  He_Arc::RPG::Hero gandalf{2, 2, 10, 10, "Gandalf"};
  He_Arc::RPG::Hero sauron{20, 20, 10, 999.9, "Sauron"};

  gimli.show();
  std::println("");
  gandalf.show();
  std::println("");

  gandalf.interact(aragorn);

  return 0;
}
```
<!-- SNIPPET:END -->
