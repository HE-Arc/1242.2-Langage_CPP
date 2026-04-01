---
title: "Projet Fil Rouge V4 — Solutions"
type: docs
weight: 10
draft: false
---

# Projet Fil Rouge V4 — Solutions

## Classe Hero (inchangée depuis V3)

{{<details "1242.2_Project_V4_FilRouge_Hero" >}}
**`Hero.h`**
<!-- SNIPPET:BEGIN source_file=Hero.h id=1242.2_Project_V4_FilRouge_Hero.h -->
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

    // Pure virtual: every concrete hero must define how it interacts.
    // A body is provided so subclasses can call Hero::interact() as a default greeting.
    virtual void interact(const Hero &other) = 0;

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
<!-- SNIPPET:BEGIN source_file=Hero.cpp id=1242.2_Project_V4_FilRouge_Hero.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  Hero::Hero(int strength, int agility, int intelligence, double hp, std::string name)
    : m_strength(strength), m_agility(agility), m_intelligence(intelligence),
      m_hp(hp), m_name(name) {}

  void Hero::show() const
  {
    std::println("=================");
    std::println("HERO: {}", m_name);
    std::println("=================");
    std::println("strength:     {}", m_strength);
    std::println("agility:      {}", m_agility);
    std::println("intelligence: {}", m_intelligence);
    std::println("HP:           {}", m_hp);
  }

  // Default greeting — subclasses call this via Hero::interact(other)
  void Hero::interact(const Hero &other)
  {
    std::println("Hello valiant {}! I'm {}", other.getName(), m_name);
  }

  std::ostream &operator<<(std::ostream &s, const Hero &p)
  {
    std::print(s, "=================\nHERO: {}\n=================\n"
                  "strength:     {}\nagility:      {}\nintelligence: {}\nHP:           {}\n",
               p.getName(), p.getStrength(), p.getAgility(), p.getIntelligence(), p.getHp());
    return s;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Warrior (inchangée depuis V3)

{{<details "1242.2_Project_V4_FilRouge_Warrior" >}}
**`Warrior.h`**
<!-- SNIPPET:BEGIN source_file=Warrior.h id=1242.2_Project_V4_FilRouge_Warrior.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Hero.h"

namespace He_Arc::RPG
{
  class Warrior : public Hero
  {
  public:
    Warrior(int strength = 10, int agility = 5, int intelligence = 1,
            double hp = 20, std::string name = "no_name_warrior")
        : Hero(strength, agility, intelligence, hp, name) {}

    ~Warrior() override = default;

    void interact(const Hero &other) override;
  };
}
```
<!-- SNIPPET:END -->

**`Warrior.cpp`**
<!-- SNIPPET:BEGIN source_file=Warrior.cpp id=1242.2_Project_V4_FilRouge_Warrior.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  void Warrior::interact(const Hero &other)
  {
    std::println("I will fight you! @{}", other.getName());
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Wizard (inchangée depuis V3)

{{<details "1242.2_Project_V4_FilRouge_Wizard" >}}
**`Wizard.h`**
<!-- SNIPPET:BEGIN source_file=Wizard.h id=1242.2_Project_V4_FilRouge_Wizard.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Hero.h"

namespace He_Arc::RPG
{
  class Wizard : public Hero
  {
  public:
    Wizard(int strength = 2, int agility = 2, int intelligence = 10,
           double hp = 15, std::string name = "no_name_wizard", int mana = 10)
      : Hero(strength, agility, intelligence, hp, name), m_mana(mana) {}

    ~Wizard() override = default;

    void show() const override;
    void interact(const Hero &other) override;
    void castSpell(Hero &other);

  protected:
    int m_mana{0};
  };
}
```
<!-- SNIPPET:END -->

**`Wizard.cpp`**
<!-- SNIPPET:BEGIN source_file=Wizard.cpp id=1242.2_Project_V4_FilRouge_Wizard.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  void Wizard::show() const
  {
    Hero::show();
    std::println("mana:         {}", m_mana);
  }

  void Wizard::interact(const Hero &other)
  {
    Hero::interact(other);
    std::println("Fellow traveler... I'm a bit lost, do you know where the Shire is?");
  }

  void Wizard::castSpell(Hero &other)
  {
    if (m_mana >= 2)
    {
      std::println("FIREBALL!! hahaha! (targeting {})", other.getName());
      m_mana -= 2;
    }
    else
    {
      std::println("Not enough mana!! Run?");
    }
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Necromancer (inchangée depuis V3)

{{<details "1242.2_Project_V4_FilRouge_Necromancer" >}}
**`Necromancer.h`**
<!-- SNIPPET:BEGIN source_file=Necromancer.h id=1242.2_Project_V4_FilRouge_Necromancer.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Wizard.h"

namespace He_Arc::RPG
{
  class Necromancer : public Wizard
  {
  public:
    Necromancer(int strength = 10, int agility = 5, int intelligence = 8,
                double hp = 20, std::string name = "no_name_necromancer", int mana = 10)
        : Wizard(strength, agility, intelligence, hp, name, mana) {}

    ~Necromancer() override = default;

    // Rising undead costs 2 mana
    void riseUndeads();
  };
}
```
<!-- SNIPPET:END -->

**`Necromancer.cpp`**
<!-- SNIPPET:BEGIN source_file=Necromancer.cpp id=1242.2_Project_V4_FilRouge_Necromancer.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  void Necromancer::riseUndeads()
  {
    if (m_mana >= 2)
    {
      std::println("Creating undead... work in progress");
      m_mana -= 2;
    }
    else
    {
      std::println("Not enough mana!!");
    }
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Sword (inchangée depuis V3)

{{<details "1242.2_Project_V4_FilRouge_Sword" >}}
**`Sword.h`**
<!-- SNIPPET:BEGIN source_file=Sword.h id=1242.2_Project_V4_FilRouge_Sword.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Sword
  {
  public:
    Sword() = default;
    explicit Sword(int damage) : m_damage(damage) {}
    virtual ~Sword() = default;

    int getDamage() const { return m_damage; }

  private:
    int m_damage{10};
  };
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Programme principal (étape 10 — polymorphisme avec `std::list<Hero*>`)

{{<details "1242.2_Project_V4_FilRouge_main" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Project_V4_FilRouge_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <list>

#include "Warrior.h"
#include "Wizard.h"
#include "Necromancer.h"

int main()
{
  He_Arc::RPG::Warrior gimli{10, 5, 1, 20, "Gimli"};
  He_Arc::RPG::Wizard gandalf{2, 2, 10, 10, "Gandalf", 10};
  He_Arc::RPG::Necromancer sauron{20, 20, 10, 999.9, "Sauron", 50};

  gimli.show();
  std::println("");
  gandalf.show();
  std::println("");
  sauron.show();
  std::println("");

  gimli.interact(gandalf);
  std::println("");
  gandalf.interact(sauron);
  std::println("");
  sauron.interact(gimli);
  std::println("");

  sauron.castSpell(gandalf);
  sauron.riseUndeads();
  std::println("");

  sauron.show();
  std::println("");

  // V4: polymorphism via std::list<Hero*>
  auto pHero1 = new He_Arc::RPG::Warrior(2, 2, 1, 10, "Twoflower");
  auto pHero2 = new He_Arc::RPG::Warrior(4, 12, 10, 10, "Weasel");
  auto pHero3 = new He_Arc::RPG::Wizard(2, 2, 10, 10, "Rincewind", 3);
  auto pHero4 = new He_Arc::RPG::Necromancer(1, 1, 1, 10, "G.A. Romero", 50);
  auto pHero5 = new He_Arc::RPG::Warrior(10, 7, 3, 20, "Bravd");

  std::list<He_Arc::RPG::Hero *> myParty = {pHero1, pHero2, pHero3, pHero4, pHero5};

  // show() dispatches to the runtime type — polymorphism in action
  for (const auto &hero : myParty)
  {
    hero->show();
    std::println("");
  }

  for (auto &hero : myParty)
  {
    delete hero;
    hero = nullptr;
  }
  myParty.clear();

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
