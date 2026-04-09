---
title: "7. Modèles — Solutions"
type: docs
weight: 10
draft: false
---

# Chapitre 7 : modèles — Solutions

## Série 7.1

### Exercice 1 : modèle de fonction **`exchange`**

{{<details "1242.2_07.01_FunctionTemplateExchange" >}}
**`Time.h`**
<!-- SNIPPET:BEGIN source_file=Time.h id=1242.2_Exercises_07.01_FunctionTemplateExchange_Time.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <iomanip>

constexpr int HOURS_PER_DAY = 24;
constexpr int MINUTES_PER_HOUR = 60;

class Time
{
public:
    Time() = default;
    Time(const Time& other) = default;
    virtual ~Time() = default;
    
    Time(int h, int m);
    Time(double realTime);

    int getHour() const { return m_hour; }
    int getMinute() const { return m_minute; }

    void setHour(int h);
    void setMinute(int m);

    Time& operator=(const Time& other);

    friend Time operator+(const Time& t1, const Time& t2);
    Time operator-(const Time& other) const;

    bool operator==(const Time& other) const { return m_hour == other.m_hour && m_minute == other.m_minute; }
    bool operator<(const Time& other) const { return evaluate() < other.evaluate(); }
    bool operator>=(const Time& other) const { return !(*this < other); }
    bool operator<=(const Time& other) const { return !(other < *this); }
    bool operator!=(const Time& other) const { return !(*this == other); }

    Time& operator++();
    Time operator++(int);

    friend std::istream& operator>>(std::istream& in, Time& t);
    friend std::ostream& operator<<(std::ostream& out, const Time& t);

private:
    int m_hour{12};
    int m_minute{0};

    int evaluate() const;
};
```
<!-- SNIPPET:END -->

**`Time.cpp`**
<!-- SNIPPET:BEGIN source_file=Time.cpp id=1242.2_Exercises_07.01_FunctionTemplateExchange_Time.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
Time::Time(int h, int m) : m_hour(0), m_minute(0)
{
    setHour(h);
    setMinute(m);
}

Time::Time(double realTime) : m_hour(0), m_minute(0)
{
    if (realTime >= 0 && realTime < HOURS_PER_DAY) {
        setHour(static_cast<int>(realTime));
        setMinute(static_cast<int>(MINUTES_PER_HOUR * (realTime - static_cast<int>(realTime))));
    }
}

void Time::setHour(int h)
{
    if (h >= 0) {
        m_hour = h % HOURS_PER_DAY;
    }
}

void Time::setMinute(int m)
{
    if (m >= 0) {
        m_minute = m % MINUTES_PER_HOUR;
        m_hour += m / MINUTES_PER_HOUR;
        setHour(m_hour);
    } else {
        m_minute = 0;
    }
}

Time& Time::operator=(const Time& other)
{
    if (this != &other) {
        m_hour = other.m_hour;
        m_minute = other.m_minute;
    }
    return *this;
}

Time Time::operator-(const Time& other) const
{
    Time result;
    result.setMinute(m_minute - other.m_minute);
    result.setHour(m_hour - other.m_hour);
    return result;
}

Time operator+(const Time& t1, const Time& t2)
{
    Time result;
    result.setMinute(t1.m_minute + t2.m_minute);
    result.setHour(t1.m_hour + t2.m_hour);
    return result;
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

int Time::evaluate() const
{
    return m_hour * MINUTES_PER_HOUR + m_minute;
}

std::ostream& operator<<(std::ostream& out, const Time& t)
{
    return out << std::setfill('0') << std::setw(2) << t.m_hour
               << ':' << std::setw(2) << t.m_minute;
}

std::istream& operator>>(std::istream& in, Time& t)
{
    char c;
    int hour, minute;

    in >> hour >> c >> minute;
    if (c == ':') {
        t.setMinute(minute);
        t.setHour(hour);
        return in;
    }

    std::println(stderr, "Read error: expected format HH:MM");
    in.setstate(std::ios::failbit);
    return in;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_07.01_FunctionTemplateExchange_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
template <typename T>
void exchange(T& first, T& second)
{
    T temp = first;
    first = second;
    second = temp;
}

int main()
{
    int n1 = 3, n2 = 5;
    auto f1 = 1.76, f2 = -5.87;
    Time t1(10, 17), t2(11, 12);

    std::println("n1:{} n2:{}", n1, n2);
    exchange(n1, n2);
    std::println("exchange(n1, n2)");
    std::println("n1:{} n2:{}", n1, n2);

    std::println("f1:{} f2:{}", f1, f2);
    exchange(f1, f2);
    std::println("exchange(f1, f2)");
    std::println("f1:{} f2:{}", f1, f2);

    // Time has operator<< but no std::formatter
    std::cout << "t1:" << t1 << " t2:" << t2 << '\n';
    exchange(t1, t2);
    std::println("exchange(t1, t2)");
    std::cout << "t1:" << t1 << " t2:" << t2 << '\n';

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

### Exercice 2 : modèle de fonction **`sum`**

{{<details "1242.2_07.02_FunctionTemplateSum" >}}
**`Time.h`**
<!-- SNIPPET:BEGIN source_file=Time.h id=1242.2_Exercises_07.02_FunctionTemplateSum_Time.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <iomanip>

constexpr int HOURS_PER_DAY = 24;
constexpr int MINUTES_PER_HOUR = 60;

class Time
{
public:
    Time() = default;
    Time(const Time& other) = default;
    virtual ~Time() = default;
    
    Time(int h, int m);
    Time(double realTime);

    int getHour() const { return m_hour; }
    int getMinute() const { return m_minute; }

    void setHour(int h);
    void setMinute(int m);

    Time& operator=(const Time& other);

    friend Time operator+(const Time& t1, const Time& t2);
    Time operator-(const Time& other) const;
    Time& operator+=(const Time& other);

    bool operator==(const Time& other) const { return m_hour == other.m_hour && m_minute == other.m_minute; }
    bool operator<(const Time& other) const { return evaluate() < other.evaluate(); }
    bool operator>=(const Time& other) const { return !(*this < other); }
    bool operator<=(const Time& other) const { return !(other < *this); }
    bool operator!=(const Time& other) const { return !(*this == other); }

    Time& operator++();
    Time operator++(int);

    friend std::istream& operator>>(std::istream& in, Time& t);
    friend std::ostream& operator<<(std::ostream& out, const Time& t);

private:
    int m_hour{12};
    int m_minute{0};

    int evaluate() const;
};
```
<!-- SNIPPET:END -->

**`Time.cpp`**
<!-- SNIPPET:BEGIN source_file=Time.cpp id=1242.2_Exercises_07.02_FunctionTemplateSum_Time.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
Time::Time(int h, int m) : m_hour(0), m_minute(0)
{
    setHour(h);
    setMinute(m);
}

Time::Time(double realTime) : m_hour(0), m_minute(0)
{
    if (realTime >= 0 && realTime < HOURS_PER_DAY) {
        setHour(static_cast<int>(realTime));
        setMinute(static_cast<int>(MINUTES_PER_HOUR * (realTime - static_cast<int>(realTime))));
    }
}

void Time::setHour(int h)
{
    if (h >= 0) {
        m_hour = h % HOURS_PER_DAY;
    }
}

void Time::setMinute(int m)
{
    if (m >= 0) {
        m_minute = m % MINUTES_PER_HOUR;
        m_hour += m / MINUTES_PER_HOUR;
        setHour(m_hour);
    } else {
        m_minute = 0;
    }
}

Time& Time::operator=(const Time& other)
{
    if (this != &other) {
        m_hour = other.m_hour;
        m_minute = other.m_minute;
    }
    return *this;
}

Time Time::operator-(const Time& other) const
{
    Time result;
    result.setMinute(m_minute - other.m_minute);
    result.setHour(m_hour - other.m_hour);
    return result;
}

Time operator+(const Time& t1, const Time& t2)
{
    Time result;
    result.setMinute(t1.m_minute + t2.m_minute);
    result.setHour(t1.m_hour + t2.m_hour);
    return result;
}

Time& Time::operator+=(const Time& other)
{
    *this = *this + other;
    return *this;
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

int Time::evaluate() const
{
    return m_hour * MINUTES_PER_HOUR + m_minute;
}

std::ostream& operator<<(std::ostream& out, const Time& t)
{
    return out << std::setfill('0') << std::setw(2) << t.m_hour
               << ':' << std::setw(2) << t.m_minute;
}

std::istream& operator>>(std::istream& in, Time& t)
{
    char c;
    int hour, minute;

    in >> hour >> c >> minute;
    if (c == ':') {
        t.setMinute(minute);
        t.setHour(hour);
        return in;
    }

    std::println(stderr, "Read error: expected format HH:MM");
    in.setstate(std::ios::failbit);
    return in;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_07.02_FunctionTemplateSum_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
template <typename T>
T sum(T tab[], int length)
{
    T result{0};
    for (int i = 0; i < length; ++i) {
        result += tab[i];
    }
    return result;
}

int main()
{
    int intTable[] = {3, 5, 2, 1};
    double doubleTable[] = {2.5, 3.2, 1.8};
    char charTable[] = {'A', '0', 'i', 'o', 'u'};
    Time timeTable[] = {{5, 10}, {3, 22}};

    std::println("{}", sum(intTable, 4));
    std::println("{}", sum(doubleTable, 3));
    // char sum produces an ASCII value (int promotion)
    std::println("{}", sum(charTable, 5));
    // Time has operator<< but no std::formatter
    std::cout << sum(timeTable, 2) << '\n';

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Série 7.2

### Exercice 1 : modèle de classe **`Vector`**

{{<details "1242.2_07.03_ClassTemplateVector" >}}
**`Point.h`**
<!-- SNIPPET:BEGIN source_file=Point.h id=1242.2_Exercises_07.03_ClassTemplateVector_Point.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <string>

class Point
{
public:
    Point(double x = 0.0, double y = 0.0, std::string name = "Point");
    Point(const Point& other);
    Point(Point&& other);
    virtual ~Point();

    Point& operator=(const Point& other);

    void show() const;
    void translate(double dx, double dy);
    void translate(const Point& other);

    friend std::ostream& operator<<(std::ostream& os, const Point& p);

    static int counter;

private:
    double m_x{0.0};
    double m_y{0.0};
    std::string m_name;
};
```
<!-- SNIPPET:END -->

**`Point.cpp`**
<!-- SNIPPET:BEGIN source_file=Point.cpp id=1242.2_Exercises_07.03_ClassTemplateVector_Point.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int Point::counter = 0;

Point::Point(double x, double y, std::string name)
    : m_x(x), m_y(y), m_name(std::move(name))
{
    counter++;
    std::print("[Cstd:{}]", counter);
}

Point::Point(const Point& other)
    : m_x(other.m_x), m_y(other.m_y), m_name(other.m_name)
{
    counter++;
    std::print("[Ccop:{}]", counter);
}

Point::Point(Point&& other)
    : m_x(other.m_x), m_y(other.m_y), m_name(std::move(other.m_name))
{
    counter++;
    std::print("[Cmov:{}]", counter);
}

Point& Point::operator=(const Point& other)
{
    if (this != &other) {
        m_x = other.m_x;
        m_y = other.m_y;
        m_name = other.m_name;
    }
    return *this;
}

Point::~Point()
{
    std::print("[Dstr:{}]", counter);
    counter--;
}

void Point::show() const
{
    std::println("{}: ({}, {})", m_name, m_x, m_y);
}

void Point::translate(double dx, double dy)
{
    m_x += dx;
    m_y += dy;
}

void Point::translate(const Point& other)
{
    translate(other.m_x, other.m_y);
}

std::ostream& operator<<(std::ostream& os, const Point& p)
{
    os << '\n' << p.m_name << ": (" << p.m_x << ", " << p.m_y << ')';
    return os;
}
```
<!-- SNIPPET:END -->

**`Vector.h`**
<!-- SNIPPET:BEGIN source_file=Vector.h id=1242.2_Exercises_07.03_ClassTemplateVector_Vector.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <algorithm>

// Class template with type parameter T and non-type parameter dim (default: 3)
template <typename T, int dim = 3>
class Vector
{
public:
  Vector() = default;
  Vector(const T &initElem);
  Vector(const Vector &src);
  virtual ~Vector() = default;

  T &operator[](int index);
  Vector &operator=(const Vector &src);
  Vector &operator=(const T &src);

  // Inline friend to avoid template friendship complexity
  friend std::ostream &operator<<(std::ostream &os, const Vector &v)
  {
    os << "(";
    for (const auto &comp : v.m_data)
    {
      os << " " << comp;
    }
    os << " )";
    return os;
  }

private:
  T m_data[dim];
};

template <typename T, int dim>
Vector<T, dim>::Vector(const T &initElem)
{
  for (auto &comp : m_data)
  {
    comp = initElem;
  }
}

template <typename T, int dim>
Vector<T, dim>::Vector(const Vector &src)
{
  std::copy(std::begin(src.m_data), std::end(src.m_data), std::begin(m_data));
}

// Clamps index to valid range [0, dim-1]
template <typename T, int dim>
T &Vector<T, dim>::operator[](int index)
{
  return m_data[std::clamp(index, 0, dim - 1)];
}

template <typename T, int dim>
Vector<T, dim> &Vector<T, dim>::operator=(const Vector &src)
{
  if (this != &src)
  {
    std::copy(std::begin(src.m_data), std::end(src.m_data), std::begin(m_data));
  }
  return *this;
}

// Fills all components with a single value
template <typename T, int dim>
Vector<T, dim> &Vector<T, dim>::operator=(const T &src)
{
  for (auto &comp : m_data)
  {
    comp = src;
  }
  return *this;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_07.03_ClassTemplateVector_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
int main()
{
    Vector<int, 4> vi = {37};
    vi[3] = 5;
    vi[2] = 2;
    std::cout << vi;

    Vector<double> vd; // 3 elements by default
    vd[0] = 0.0;
    vd[1] = 0.1;
    vd[2] = 0.2;
    std::cout << vd;
    std::println("\nvd[-8] --> out of range: {}", vd[-8]); // clamped to first element
    std::println("\nvd[12] --> out of range: {}", vd[12]); // clamped to last element
    std::println("vd[12] = 99.99");
    vd[12] = 99.99; // clamped to last element
    std::println("vd[2]: {}", vd[2]);

    Vector<double> vd3;
    std::cout << vd;
    vd3 = vd;
    std::cout << vd3;

    Vector<Point, 2> vpt = {Point(0.0, 0.0, "default")};
    Vector<Point, 2> vpt2 = {Point(1.0, 2.0, "other")};
    std::cout << vpt;
    vpt = vpt2;
    std::cout << vpt;

    // Class Template Argument Deduction (C++17)
    // No need to specify template arguments if deducible
    Vector vpt3(vpt2);
    std::cout << vpt3;

    std::println("");

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
