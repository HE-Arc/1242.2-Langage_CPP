---
title: "8. Exceptions — Solutions"
type: docs
weight: 10
draft: true
---

# Chapitre 8 : exceptions — Solutions

## Serie 8.1

### Exercice 1 : validation avec exceptions

{{<details "1242.2_08.01_ExceptionValidation" >}}
**`MyException.h`**
<!-- SNIPPET:BEGIN source_file=MyException.h id=1242.2_Exercises_08.01_ExceptionValidation_MyException.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#pragma once

#include <exception>
#include <string>

class MyException : public std::exception
{
public:
    MyException() noexcept = default;
    explicit MyException(std::string msg) noexcept;
    virtual ~MyException() = default;

    const char* what() const noexcept override;

private:
    std::string m_errorMessage{"Undefined error!"};
};
```
<!-- SNIPPET:END -->

**`MyException.cpp`**
<!-- SNIPPET:BEGIN source_file=MyException.cpp id=1242.2_Exercises_08.01_ExceptionValidation_MyException.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "MyException.h"

MyException::MyException(std::string msg) noexcept
    : m_errorMessage(std::move(msg))
{
}

const char* MyException::what() const noexcept
{
    return m_errorMessage.c_str();
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_08.01_ExceptionValidation_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <iostream>
#include <print>

#include "MyException.h"

void isPositive(int value);
void isOdd(int value);
void isLessThan(int value, int maxValue);
void isGreaterThan(int value, int minValue);

int main()
{
    auto minValue = 10;
    auto maxValue = 100;

    try
    {
        int value;
        std::print("Enter a positive and odd value [{}, {}] : ", minValue, maxValue);
        std::cin >> value;

        isPositive(value);
        isOdd(value);
        isLessThan(value, maxValue);
        isGreaterThan(value, minValue);

        std::println("Correct value !");
    }
    catch (int val)
    {
        std::println("Incorrect value ! ->  {}", val);
    }
    catch (const char* str)
    {
        std::println("Incorrect value ! ->  {}", str);
    }
    catch (const MyException& err)
    {
        std::println("Incorrect value ! ->  {}", err.what());
    }
    catch (...)
    {
        std::println("Unknown error !");
    }

    return 0;
}

void isPositive(int value)
{
    if (value < 0)
    {
        throw value;
    }
    std::println("- OK: It's a positive value");
}

void isOdd(int value)
{
    if (value % 2 == 0)
    {
        throw "The value is even";
    }
    std::println("- OK: It's an odd value");
}

void isLessThan(int value, int maxValue)
{
    if (value > maxValue)
    {
        throw MyException("The value is too large");
    }
    std::println("- OK: It's a value less than {}", maxValue);
}

void isGreaterThan(int value, int minValue)
{
    if (value < minValue)
    {
        throw MyException("The value is too small");
    }
    std::println("- OK: It's a value greater than {}", minValue);
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Serie 8.2

### Exercice 1 : classe Vector avec exceptions

{{<details "1242.2_08.02_ExceptionVector" >}}
**`Vector.h`**
<!-- SNIPPET:BEGIN source_file=Vector.h id=1242.2_Exercises_08.02_ExceptionVector_Vector.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#pragma once

#include <iosfwd>

class Vector
{
public:
    Vector() = default;
    Vector(int size, int value = 0);
    Vector(const Vector& v);
    virtual ~Vector();

    Vector& operator=(const Vector& v);
    friend Vector operator+(const Vector& v1, const Vector& v2);
    int& operator[](int i);

    long long getSizeInBytes() const
    {
        return static_cast<long long>(m_size) * sizeof(*m_data);
    }

    friend std::ostream& operator<<(std::ostream& out, const Vector& v);

private:

    int *m_data{nullptr};
    int m_size{0};

    void cleanup();
};
```
<!-- SNIPPET:END -->

**`Vector.cpp`**
<!-- SNIPPET:BEGIN source_file=Vector.cpp id=1242.2_Exercises_08.02_ExceptionVector_Vector.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include "Vector.h"

#include <iostream>
#include <print>
#include <new>
#include <stdexcept>

Vector::Vector(int size, int value)
{
  try
  {
    m_size = size;
    m_data = new int[m_size];
    for (int i = 0; i < m_size; i++)
    {
      m_data[i] = value;
    }
  }
  catch (const std::bad_alloc &e)
  {
    std::println("  caught in Vector(int, int) >>> {}", e.what());
    cleanup();
  }
}

Vector::Vector(const Vector &v)
{
  try
  {
    m_size = v.m_size;
    m_data = new int[m_size];
    for (int i = 0; i < m_size; i++)
    {
      m_data[i] = v.m_data[i];
    }
  }
  catch (const std::bad_alloc &e)
  {
    std::println("  caught in Vector(const Vector&) >>> {}", e.what());
    cleanup();
  }
}

Vector::~Vector()
{
  cleanup();
}

Vector &Vector::operator=(const Vector &vec)
{
  if (this != &vec)
  {
    cleanup();
    try
    {
      m_size = vec.m_size;
      m_data = new int[m_size];
      for (int i = 0; i < m_size; i++)
      {
        m_data[i] = vec.m_data[i];
      }
    }
    catch (const std::bad_alloc &e)
    {
      std::println("  caught in operator= >>> {}", e.what());
      cleanup();
    }
  }
  return *this;
}

int &Vector::operator[](int i)
{
  if (m_data != nullptr && i >= 0 && i < m_size)
  {
    return m_data[i];
  }
  throw std::out_of_range("  thrown from operator[] :: Out of range");
}

void Vector::cleanup()
{
  delete[] m_data;
  m_data = nullptr;
  m_size = 0;
}

std::ostream &operator<<(std::ostream &out, const Vector &v)
{
  out << "[ ";
  for (int i = 0; i < v.m_size; i++)
  {
    out << v.m_data[i] << ' ';
  }
  out << "]";
  return out;
}

Vector operator+(const Vector &v1, const Vector &v2)
{
  if (v1.m_size == v2.m_size)
  {
    Vector result(v1.m_size);
    for (int i = 0; i < v1.m_size; i++)
    {
      result.m_data[i] = v1.m_data[i] + v2.m_data[i];
    }
    return result;
  }
  return v1;
}
```
<!-- SNIPPET:END -->

**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Exercises_08.02_ExceptionVector_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
#include <print>
#include <vector>
#include <cmath>
#include <limits>

#include "Vector.h"

int main()
{
    const int SIZE = INT_MAX;

    // A) Allocation test in constructor Vector(int, int)
    std::println("Vector v1({});", SIZE);
    Vector v1(SIZE);

    // B) Allocation test in assignment operator
    auto nbOfTry = 10;
    std::vector<Vector> tabV(nbOfTry);
    for (int i = 0; i < nbOfTry; i++)
    {
        std::println("Allocation of the {}th vector of {} elements", i + 1, SIZE);
        tabV[i] = v1;
    }

    // C) Size of allocated memory
    long long sumInBytes = 0;
    for (auto &v : tabV)
    {
        sumInBytes += v.getSizeInBytes();
    }
    std::println("Memory allocated : {} Bytes", sumInBytes);
    std::println("Memory allocated : {} GB (1000)", sumInBytes / std::pow(1000, 3));
    std::println("Memory allocated : {} GB (1024)", sumInBytes / std::pow(1024, 3));

    // D) Allocation test in constructor Vector(int, int)
    std::println("Vector v2({});", SIZE);
    Vector v2(SIZE);

    // E) Allocation test in copy constructor Vector(const Vector&)
    std::println("Vector v3 = v1;");
    Vector v3 = v1;

    // F) Allocation test in assignment operator
    std::println("Vector v5;");
    Vector v5;
    std::println("v5 = v1;");
    v5 = v1;

    // G) Allocation test with wrong value
    std::println("Vector v6(-1);");
    Vector v6(-1);

    // H) Out-of-range access in Vector
    try
    {
        std::println("v1[-1] = 5;");
        v1[-1] = 5;
    }
    catch (const std::out_of_range& e)
    {
        std::println("  caught in main() >>>> {}", e.what());
    }

    // I) Out-of-range access in std::vector
    try
    {
        std::println("tabV.at(-1).getSizeInBytes()");
        std::println("{}", tabV.at(-1).getSizeInBytes());
    }
    catch (const std::exception& e)
    {
        std::println("  caught in main() >>>> {}", e.what());
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}
