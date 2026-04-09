---
title: "Projet Fil Rouge V5 — Solutions"
type: docs
weight: 10
draft: false
---

# Projet Fil Rouge V5 — Solutions

## Interface IObject (nouveau en V5)

{{<details "1242.2_Project_V5_FilRouge_IObject" >}}
**`IObject.h`**
<!-- SNIPPET:BEGIN source_file=IObject.h id=1242.2_Project_V5_FilRouge_IObject.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class IObject
  {
  public:
    virtual ~IObject() = default;
    virtual std::string getName() const = 0;
    virtual int getFeature() const = 0;
  };
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Sword (adaptée pour IObject)

{{<details "1242.2_Project_V5_FilRouge_Sword" >}}
**`Sword.h`**
<!-- SNIPPET:BEGIN source_file=Sword.h id=1242.2_Project_V5_FilRouge_Sword.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Sword : public IObject
  {
  public:
    Sword() = default;
    explicit Sword(int damage) : m_damage(damage) {}
    virtual ~Sword() override = default;

    std::string getName() const override;
    int getFeature() const override;

  private:
    int m_damage{10};
  };
}
```
<!-- SNIPPET:END -->

**`Sword.cpp`**
<!-- SNIPPET:BEGIN source_file=Sword.cpp id=1242.2_Project_V5_FilRouge_Sword.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Sword.h"

namespace He_Arc::RPG
{
  std::string Sword::getName() const
  {
    return "Sword";
  }

  int Sword::getFeature() const
  {
    return m_damage;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Shield (nouveau en V5)

{{<details "1242.2_Project_V5_FilRouge_Shield" >}}
**`Shield.h`**
<!-- SNIPPET:BEGIN source_file=Shield.h id=1242.2_Project_V5_FilRouge_Shield.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Shield : public IObject
  {
  public:
    Shield() = default;
    explicit Shield(int solidity) : m_solidity(solidity) {}
    virtual ~Shield() override = default;

    std::string getName() const override;
    int getFeature() const override;

  private:
    int m_solidity{5};
  };
}
```
<!-- SNIPPET:END -->

**`Shield.cpp`**
<!-- SNIPPET:BEGIN source_file=Shield.cpp id=1242.2_Project_V5_FilRouge_Shield.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Shield.h"

namespace He_Arc::RPG
{
  std::string Shield::getName() const
  {
    return "Shield";
  }

  int Shield::getFeature() const
  {
    return m_solidity;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Potion (nouveau en V5)

{{<details "1242.2_Project_V5_FilRouge_Potion" >}}
**`Potion.h`**
<!-- SNIPPET:BEGIN source_file=Potion.h id=1242.2_Project_V5_FilRouge_Potion.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Potion : public IObject
  {
  public:
    Potion() = default;
    explicit Potion(int power) : m_power(power) {}
    virtual ~Potion() override = default;

    std::string getName() const override;
    int getFeature() const override;

  private:
    int m_power{10};
  };
}
```
<!-- SNIPPET:END -->

**`Potion.cpp`**
<!-- SNIPPET:BEGIN source_file=Potion.cpp id=1242.2_Project_V5_FilRouge_Potion.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Potion.h"

namespace He_Arc::RPG
{
  std::string Potion::getName() const
  {
    return "Potion";
  }

  int Potion::getFeature() const
  {
    return m_power;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Backpack (nouveau en V5)

{{<details "1242.2_Project_V5_FilRouge_Backpack" >}}
**`Backpack.h`**
<!-- SNIPPET:BEGIN source_file=Backpack.h id=1242.2_Project_V5_FilRouge_Backpack.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Backpack
  {
  public:
    Backpack() = default;
    virtual ~Backpack() = default;

    void pack(IObject* pObject);
    IObject* unPack();
    bool isNotEmpty() const;

  private:
    std::stack<IObject*> m_stack;
  };
}
```
<!-- SNIPPET:END -->

**`Backpack.cpp`**
<!-- SNIPPET:BEGIN source_file=Backpack.cpp id=1242.2_Project_V5_FilRouge_Backpack.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  void Backpack::pack(IObject* pObject)
  {
    m_stack.push(pObject);
  }

  IObject* Backpack::unPack()
  {
    auto pObject = m_stack.top();
    m_stack.pop();
    return pObject;
  }

  bool Backpack::isNotEmpty() const
  {
    return !m_stack.empty();
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Hero (modifiée en V5 — IObject + Backpack)

{{<details "1242.2_Project_V5_FilRouge_Hero" >}}
**`Hero.h`**
<!-- SNIPPET:BEGIN source_file=Hero.h id=1242.2_Project_V5_FilRouge_Hero.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Hero
  {
  public:
    Hero() = default;
    Hero(const Hero&) = delete;
    Hero& operator=(const Hero&) = delete;

    Hero(int strength, int agility, int intelligence, double hp, std::string name, IObject* pObject);
    virtual ~Hero();

    virtual void show() const;
    virtual void interact(const Hero& other) = 0;

    std::string getName() const { return m_name; }
    int getStrength() const { return m_strength; }
    int getAgility() const { return m_agility; }
    int getIntelligence() const { return m_intelligence; }
    double getHp() const { return m_hp; }

    Backpack& getBackpack() { return m_backpack; }

    friend std::ostream& operator<<(std::ostream& s, const Hero& p);

  protected:
    int m_strength{0};
    int m_agility{0};
    int m_intelligence{0};
    double m_hp{0};
    std::string m_name{"no name"};
    IObject* m_pObject{nullptr};

  private:
    Backpack m_backpack;
  };

  std::ostream& operator<<(std::ostream& s, const Hero& p);
}
```
<!-- SNIPPET:END -->

**`Hero.cpp`**
<!-- SNIPPET:BEGIN source_file=Hero.cpp id=1242.2_Project_V5_FilRouge_Hero.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  Hero::Hero(int strength, int agility, int intelligence, double hp, std::string name, IObject* pObject)
      : m_strength(strength), m_agility(agility), m_intelligence(intelligence),
        m_hp(hp), m_name(std::move(name)), m_pObject(pObject) {}

  Hero::~Hero()
  {
    delete m_pObject;
    m_pObject = nullptr;
  }

  void Hero::show() const
  {
    std::println("=================");
    std::println("HERO: {}", m_name);
    std::println("=================");
    std::println("strength: {}", m_strength);
    std::println("agility: {}", m_agility);
    std::println("intelligence: {}", m_intelligence);
    std::println("HP: {}", m_hp);
    std::println("{}: {}", m_pObject->getName(), m_pObject->getFeature());
  }

  void Hero::interact(const Hero& other)
  {
    std::println("Hello valiant {}! I'm {}", other.getName(), m_name);
  }

  std::ostream& operator<<(std::ostream& s, const Hero& p)
  {
    s << "=================\n"
      << "HERO: " << p.getName() << '\n'
      << "=================\n"
      << "strength: " << p.getStrength() << '\n'
      << "agility: " << p.getAgility() << '\n'
      << "intelligence: " << p.getIntelligence() << '\n'
      << "HP: " << p.getHp() << '\n';
    return s;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Warrior (modifiée en V5 — arme par défaut)

{{<details "1242.2_Project_V5_FilRouge_Warrior" >}}
**`Warrior.h`**
<!-- SNIPPET:BEGIN source_file=Warrior.h id=1242.2_Project_V5_FilRouge_Warrior.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Warrior : public Hero
  {
  public:
    Warrior(int strength = 10, int agility = 5, int intelligence = 1,
            double hp = 20, std::string name = "no_name_warrior")
        : Hero(strength, agility, intelligence, hp, std::move(name), new Sword()) {}

    virtual ~Warrior() override = default;

    void interact(const Hero& other) override;
  };
}
```
<!-- SNIPPET:END -->

**`Warrior.cpp`**
<!-- SNIPPET:BEGIN source_file=Warrior.cpp id=1242.2_Project_V5_FilRouge_Warrior.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Warrior.h"

#include <print>

namespace He_Arc::RPG
{
  void Warrior::interact(const Hero& other)
  {
    std::println("I will fight you! @{}", other.getName());
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Classe Wizard (modifiée en V5 — objet par défaut)

{{<details "1242.2_Project_V5_FilRouge_Wizard" >}}
**`Wizard.h`**
<!-- SNIPPET:BEGIN source_file=Wizard.h id=1242.2_Project_V5_FilRouge_Wizard.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Wizard : public Hero
  {
  public:
    Wizard(int strength = 10, int agility = 5, int intelligence = 1,
           double hp = 20, std::string name = "no_name_wizard", int mana = 10)
        : Hero(strength, agility, intelligence, hp, std::move(name), new Potion()),
          m_mana(mana) {}

    virtual ~Wizard() override = default;

    void show() const override;
    void interact(const Hero& other) override;
    void castSpell(Hero& other);

  protected:
    int m_mana{0};
  };
}
```
<!-- SNIPPET:END -->

**`Wizard.cpp`**
<!-- SNIPPET:BEGIN source_file=Wizard.cpp id=1242.2_Project_V5_FilRouge_Wizard.cpp -->
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
    std::println("Mana: {}", m_mana);
  }

  void Wizard::interact([[maybe_unused]] const Hero& other)
  {
    std::println("Hello fellow traveler! I'm a bit lost, do you know where the Shire is?");
  }

  void Wizard::castSpell([[maybe_unused]] Hero& other)
  {
    if (m_mana > 2)
    {
      std::println("FIREBALL!! hahaha!");
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

{{<details "1242.2_Project_V5_FilRouge_Necromancer" >}}
**`Necromancer.h`**
<!-- SNIPPET:BEGIN source_file=Necromancer.h id=1242.2_Project_V5_FilRouge_Necromancer.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
namespace He_Arc::RPG
{
  class Necromancer : public Wizard
  {
  public:
    Necromancer(int strength = 10, int agility = 5, int intelligence = 1,
                double hp = 20, std::string name = "no_name_necromancer", int mana = 10)
        : Wizard(strength, agility, intelligence, hp, std::move(name), mana) {}

    virtual ~Necromancer() override = default;

    void riseUndeads();
  };
}
```
<!-- SNIPPET:END -->

**`Necromancer.cpp`**
<!-- SNIPPET:BEGIN source_file=Necromancer.cpp id=1242.2_Project_V5_FilRouge_Necromancer.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Necromancer.h"

#include <print>

namespace He_Arc::RPG
{
  void Necromancer::riseUndeads()
  {
    if (m_mana > 2)
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

## Utilitaire

{{<details "1242.2_Project_V5_FilRouge_Utility" >}}
**`Utility.h`**
<!-- SNIPPET:BEGIN source_file=Utility.h id=1242.2_Project_V5_FilRouge_Utility.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#pragma once

namespace He_Arc::RPG::Utility
{
  template <typename T>
  inline void deletePtr(T*& rPtr)
  {
    delete rPtr;
    rPtr = nullptr;
  }
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Programme principal (étape 12 — Backpack)

{{<details "1242.2_Project_V5_FilRouge_main" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Project_V5_FilRouge_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int main()
{
    Warrior gimli = {10, 5, 1, 20, "Gimli"};
    Wizard gandalf = {2, 2, 10, 10, "Gandalf", 10};
    Necromancer sauron = {20, 20, 10, 999.9, "Sauron", 50};

    gimli.show();
    std::println("");
    gandalf.show();
    std::println("");
    sauron.show();
    std::println("");

    gimli.interact(gandalf);
    gandalf.interact(sauron);
    sauron.interact(gimli);

    sauron.castSpell(gandalf);
    sauron.riseUndeads();

    sauron.show();
    std::println("");

    // V4: Polymorphism with std::list
    auto pHero1 = new Warrior(2, 2, 1, 10, "Twoflower");
    auto pHero2 = new Warrior(4, 12, 10, 10, "Weasel");
    auto pHero3 = new Wizard(2, 2, 10, 10, "Rincewind", 3);
    auto pHero4 = new Necromancer(1, 1, 1, 10, "G.A. Romero", 50);
    auto pHero5 = new Warrior(10, 7, 3, 20, "Bravd");

    std::list<Hero*> myParty = {pHero1, pHero2, pHero3, pHero4, pHero5};

    for (const auto& hero : myParty)
    {
        hero->show();
    }

    for (auto& hero : myParty)
    {
        delete hero;
        hero = nullptr;
    }

    // V5: Backpack (LIFO inventory)
    std::println("BackPack test");

    gimli.getBackpack().pack(new Sword());
    gimli.getBackpack().pack(new Sword());
    gimli.getBackpack().pack(new Sword());
    gimli.getBackpack().pack(new Shield());
    gimli.getBackpack().pack(new Shield());
    gimli.getBackpack().pack(new Potion());

    std::println("\nThe backpack of {} contains:", gimli.getName());

    while (gimli.getBackpack().isNotEmpty())
    {
        auto pObject = gimli.getBackpack().unPack();
        std::println(" - {} ({})", pObject->getName(), pObject->getFeature());
        delete pObject;
        pObject = nullptr;
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
