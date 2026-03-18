---
title: "3. Surcharge des opérateurs — Solutions"
type: docs
weight: 10
draft: false
---

# Chapitre 3 : surcharge des opérateurs — Solutions

## Série 3.1

### Exercice 1 : classe Time avec surcharge d'opérateurs

{{<details "1242.2_03.01_OverloadingTime" >}}
**`Time.h`**
<!-- SNIPPET:BEGIN source_file=Time.h id=1242.2_Exercises_03.01_OverloadingTime_Time.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iosfwd>

class Time
{
public:
    Time();
    explicit Time(int h, int m);
    Time(double realTime); // Implicit conversion intentional: enables expressions like t + 4

    virtual ~Time() = default;

    int getHour() const;
    int getMinute() const;

    void setHour(int h);
    void setMinute(int m);

    Time &operator=(const Time &) = default; // Default memberwise copy is sufficient here

    friend Time operator+(const Time &tm1, const Time &tm2);
    Time operator-(const Time &tm) const;

    bool operator==(const Time &tm) const { return m_hour == tm.m_hour && m_minute == tm.m_minute; }
    bool operator<(const Time &tm) const { return evaluate() < tm.evaluate(); }
    bool operator>=(const Time &tm) const { return !(*this < tm); }
    bool operator<=(const Time &tm) const { return !(tm < *this); }
    bool operator!=(const Time &tm) const { return !(*this == tm); }

    Time &operator++();
    Time operator++(int);

    friend std::istream &operator>>(std::istream &in, Time &tm);
    friend std::ostream &operator<<(std::ostream &out, const Time &tm);

private:
    int m_hour{12};
    int m_minute{0};

    int evaluate() const;

    static constexpr int m_hours_per_day{24};
    static constexpr int m_minutes_per_hour{60};
};
```
<!-- SNIPPET:END -->

**`Time.cpp`**
<!-- SNIPPET:BEGIN source_file=Time.cpp id=1242.2_Exercises_03.01_OverloadingTime_Time.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
Time::Time() = default;

Time::Time(int h, int m)
{
    setHour(h);
    setMinute(m);
}

Time::Time(double realTime)
{
    setHour(static_cast<int>(realTime));
    setMinute(static_cast<int>(60.0 * (realTime - static_cast<int>(realTime))));
}

int Time::getHour()   const { return m_hour; }
int Time::getMinute() const { return m_minute; }

void Time::setHour(int h)
{
    m_hour = (h >= 0) ? (h % m_hours_per_day) : 0;
}

void Time::setMinute(int m)
{
    if (m >= 0)
    {
        m_minute = m % m_minutes_per_hour;
        m_hour   = m_hour + m / m_minutes_per_hour;
        setHour(m_hour);
    }
    else
    {
        m_minute = 0;
    }
}

Time Time::operator-(const Time& tm) const
{
    Time result;
    result.setMinute(m_minute - tm.m_minute);
    result.setHour(m_hour - tm.m_hour);
    return result;
}

Time operator+(const Time& tm1, const Time& tm2)
{
    Time result;
    result.setMinute(tm1.m_minute + tm2.m_minute);
    result.setHour(tm1.m_hour + tm2.m_hour);
    return result;
}

int Time::evaluate() const
{
    return m_hour * 60 + m_minute;
}

Time& Time::operator++()
{
    *this = *this + Time(0, 1);
    return *this;
}

Time Time::operator++(int)
{
    Time tmp = *this;
    *this = *this + Time(0, 1);
    return tmp;
}

std::ostream& operator<<(std::ostream& out, const Time& tm)
{
    return out << std::format("{:02d}:{:02d}", tm.m_hour, tm.m_minute);
}

std::istream& operator>>(std::istream& in, Time& tm)
{
    char c;
    int hour, minute;
    in >> hour >> c >> minute;
    if (c == ':')
    {
        tm.setMinute(minute);
        tm.setHour(hour);
        return in;
    }
    in.setstate(std::ios::failbit);
    return in;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_03.01_OverloadingTime_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Time.h"

#include <iostream>

int main()
{
  // Constructors
  std::cout << "Time t1 (default): ";
  Time t1;
  std::cout << t1 << '\n';

  std::cout << "Time t2(10, 9):    ";
  Time t2(10, 9);
  std::cout << t2 << '\n';

  std::cout << "Time t3(17.75):    ";
  Time t3(17.75);
  std::cout << t3 << '\n';

  // Setters
  std::cout << "\nt2.setHour(7):      ";
  t2.setHour(7);
  std::cout << t2 << '\n';

  std::cout << "t2.setMinute(-40):  ";
  t2.setMinute(-40); // negative -> clamped to 0
  std::cout << t2 << '\n';

  std::cout << "t2.setMinute(86):   ";
  t2.setMinute(86); // 86 % 60 = 26 min, +1 hour
  std::cout << t2 << '\n';

  // operator=
  std::cout << "\nt1 = t2:  ";
  t1 = t2;
  std::cout << "t1=" << t1 << "  t2=" << t2 << '\n';

  // operator+ (non-member friend)
  t1.setMinute(0);
  std::cout << "\nt1=" << t1 << "  t3=" << t3 << '\n';
  std::cout << "t1 = t1 + t3: ";
  t1 = t1 + t3;
  std::cout << t1 << '\n';

  std::cout << "t3 = t3 + 4:  ";
  t3 = t3 + 4; // implicit conversion: 4 -> Time(4.0)
  std::cout << t3 << '\n';

  std::cout << "t3 = 4 + t3:  ";
  t3 = 4 + t3;
  std::cout << t3 << '\n';

  // operator- (member)
  std::cout << "\nt1=" << t1 << "  t3=" << t3 << '\n';
  std::cout << "t1 = t1 - t3: ";
  t1 = t1 - t3;
  std::cout << t1 << '\n';

  std::cout << "t3 = t3 - 1:  ";
  t3 = t3 - 1;
  std::cout << t3 << '\n';

  // t3 = 1 - t3 // ???

  // Comparison operators
  std::cout << '\n';
  std::cout << t1 << " == " << t1 << std::boolalpha << " : " << (t1 == t1) << '\n';
  std::cout << t1 << " == " << t2 << std::boolalpha << " : " << (t1 == t2) << '\n';
  std::cout << t1 << " <  " << t1 << std::boolalpha << " : " << (t1 < t1) << '\n';
  std::cout << t1 << " <  " << t2 << std::boolalpha << " : " << (t1 < t2) << '\n';
  std::cout << t1 << " >= " << t1 << std::boolalpha << " : " << (t1 >= t1) << '\n';
  std::cout << t1 << " >= " << t2 << std::boolalpha << " : " << (t1 >= t2) << '\n';
  std::cout << t1 << " != " << t1 << std::boolalpha << " : " << (t1 != t1) << '\n';
  std::cout << t1 << " != " << t2 << std::boolalpha << " : " << (t1 != t2) << '\n';

  // Increment operators
  std::cout << "\nt2=" << t2 << "  t3=" << t3 << '\n';
  std::cout << "t2 = t3++: ";
  t2 = t3++;
  std::cout << "t2=" << t2 << "  t3=" << t3 << '\n';

  std::cout << "t2 = ++t3: ";
  t2 = ++t3;
  std::cout << "t2=" << t2 << "  t3=" << t3 << '\n';

  // operator>>
  std::cout << "\nEnter a time (hh:mm): ";
  std::cin >> t2;
  std::cout << "t2: " << t2 << '\n';

  return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 3.2

### Exercice 1 : classe Vector avec surcharge d'opérateurs

{{<details "1242.2_03.02_OverloadingVector" >}}
**`Vector.h`**
<!-- SNIPPET:BEGIN source_file=Vector.h id=1242.2_Exercises_03.02_OverloadingVector_Vector.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iosfwd>

class Vector
{
public:
    Vector() = default;
    explicit Vector(int n, double val = 0);
    Vector(const Vector& v);
    virtual ~Vector();

    Vector& operator=(const Vector& v);
    double& operator[](int i);
    const double& operator[](int i) const;

    friend Vector operator+(const Vector& v1, const Vector& v2);
    friend std::ostream& operator<<(std::ostream& out, const Vector& v);

private:
    double* m_pData{nullptr};
    int  m_size{0};
};
```
<!-- SNIPPET:END -->

**`Vector.cpp`**
<!-- SNIPPET:BEGIN source_file=Vector.cpp id=1242.2_Exercises_03.02_OverloadingVector_Vector.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
Vector::Vector(int n, double val)
    : m_pData(new double[n]), m_size(n)
{
  for (int i = 0; i < m_size; ++i)
  {
    m_pData[i] = val;
  }
}

Vector::Vector(const Vector &v)
    : m_pData(new double[v.m_size]), m_size(v.m_size)
{
  for (int i = 0; i < m_size; ++i)
  {
    m_pData[i] = v.m_pData[i];
  }
}

Vector::~Vector()
{
  delete[] m_pData;
  m_pData = nullptr;
  m_size = 0;
}

Vector &Vector::operator=(const Vector &vec)
{
  if (this != &vec)
  {
    delete[] m_pData;
    m_pData = nullptr;
    m_size = vec.m_size;
    m_pData = new double[m_size];
    for (int i = 0; i < m_size; ++i)
    {
      m_pData[i] = vec.m_pData[i];
    }
  }
  return *this;
}

double &Vector::operator[](int i)
{
  if (i >= 0 && i < m_size)
  {
    return m_pData[i];
  }
  // Out-of-bounds: fall back to first element
  return m_pData[0];
}

const double &Vector::operator[](int i) const
{
  if (i >= 0 && i < m_size)
  {
    return m_pData[i];
  }
  // Out-of-bounds: fall back to first element
  return m_pData[0];
}

std::ostream &operator<<(std::ostream &out, const Vector &v)
{
  out << "[ ";
  for (int i = 0; i < v.m_size; ++i)
  {
    out << v.m_pData[i] << ' ';
  }
  return out << ']';
}

Vector operator+(const Vector &v1, const Vector &v2)
{
  if (v1.m_size != v2.m_size)
  {
    return v1; // sizes differ: return left operand unchanged
  }
  Vector result(v1.m_size);
  for (int i = 0; i < v1.m_size; ++i)
  {
    result.m_pData[i] = v1.m_pData[i] + v2.m_pData[i];
  }
  return result;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_03.02_OverloadingVector_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Vector.h"

#include <iostream>

int main()
{
    Vector v1;
    Vector v2(3);
    Vector v3 = Vector(3, 10);
    std::cout << "v1: " << v1 << "  v2: " << v2 << "  v3: " << v3 << "\n\n";

    // operator=
    std::cout << "v1: " << v1 << "  v3: " << v3 << '\n';
    std::cout << "v1 = v3;\n";
    v1 = v3;
    std::cout << "v1: " << v1 << "  v3: " << v3 << "\n\n";

    // operator[] — write
    std::cout << "v1: " << v1 << '\n';
    std::cout << "v1[2] = 100;\n";
    v1[2] = 100;
    std::cout << "v1: " << v1 << "\n\n";

    // operator[] — read
    std::cout << "v1[2] = " << v1[2] << '\n';
    std::cout << "v3[2] = " << v3[2] << "\n\n";

    // operator[] — out of bounds falls back to v[0]
    std::cout << "v1: " << v1 << '\n';
    std::cout << "v1[1000] = 200;\n";
    v1[1000] = 200;
    std::cout << "v1: " << v1 << "\n\n";

    // operator+ (non-member friend)
    Vector v4(5, 5);
    std::cout << "v1: " << v1 << "  v3: " << v3 << "  v4: " << v4 << '\n';
    std::cout << "v1 = v3 + v4;\n";
    v1 = v3 + v4;
    std::cout << "v1: " << v1 << "  v3: " << v3 << "  v4: " << v4 << "\n\n";

    std::cout << "v1: " << v1 << "  v2: " << v2 << "  v3: " << v3 << '\n';
    std::cout << "v1 = v3 + v3;\n";
    v1 = v3 + v3;
    std::cout << "v1: " << v1 << "  v2: " << v2 << "  v3: " << v3 << '\n';

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
