---
title: "8. Exceptions"
type: docs
weight: 10
---

# Chapitre 8 : exceptions

## Slides

{{<slides "https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/08_Exceptions.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.2-Langage_CPP-SLIDES/08_Exceptions.html?print-pdf)

## Exemples

{{<details "1242.2_08.01_ErrorCodesReturnValue" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.01_ErrorCodesReturnValue_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Error handling using return codes — the traditional approach before exceptions.
// The return value of the function is used both for the result AND for error signaling,
// which makes the code harder to read and maintain.

static int oneOverN(int n, double& result)
{
    if (n == 0)
    {
        return -1;
    }
    else
    {
        result = 1.0 / n;
        return 0;
    }
}

static double compute(int k)
{
    double result;
    if (oneOverN(k, result) == -1)
    {
        return -1;
    }
    else
    {
        return result * result;
    }
}

int main()
{
    // Problem: -1 could be a valid result — ambiguous error signaling
    auto result = compute(0);
    if (result == -1)
    {
        std::println("ERROR");
    }
    else
    {
        std::println("{}", result);
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_08.02_BasicExceptionHandling" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.02_BasicExceptionHandling_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Same logic as 08.01 but using exceptions instead of return codes.
// The exception propagates automatically through the call stack — no need
// for each intermediate function to check and forward error codes.

static double oneOverN(int n)
{
    if (n == 0)
    {
        throw n;
    }
    return 1.0 / n;
}

static double compute(int k)
{
    auto result = oneOverN(k);
    return result * result;
}

int main()
{
    try
    {
        auto result = compute(2);
        std::println("{}", result);
    }
    catch (...)
    {
        std::println("ERROR");
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_08.03_ExceptionTypeMatching" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.03_ExceptionTypeMatching_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Catch handlers with value parameters do NOT perform implicit type conversions.
// A thrown double will NOT be caught by a catch(float) handler.

int main()
{
    int dividend = 10;
    int divisor = 0;

    try
    {
        if (divisor == 0)
        {
            throw 0.0; // throws a double
            // try also: throw "division by zero!";  // const char*
            // try also: throw 0.0f;                 // float
        }
        std::println("Quotient: {}", dividend / divisor);
    }
    catch (float f)
    {
        // Will NOT catch the double — no implicit conversion in catch handlers
        std::println("Caught float: {}", f);
    }
    catch (const char* msg)
    {
        std::println("Caught message: {}", msg);
    }
    catch (...)
    {
        // The double ends up here because no exact-type handler matched
        std::println("Caught unknown exception (catch-all)");
    }

    std::println("Done");

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_08.04_ExceptionRethrowing" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.04_ExceptionRethrowing_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// An exception can be caught, partially handled, and re-thrown with a bare `throw`.
// This allows multiple levels of the call stack to react to the same exception.

void f()
{
    try
    {
        int n = 2;
        throw n;
    }
    catch (int x)
    {
        std::println("Exception caught in f(): {}", x);
        throw; // re-throw the same exception to the caller
    }
}

int main()
{
    try
    {
        f();
    }
    catch (int i)
    {
        std::println("Exception caught in main() (int): {}", i);
    }
    catch (double d)
    {
        std::println("Exception caught in main() (double): {}", d);
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_08.05_NoexceptSpecification" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.05_NoexceptSpecification_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// In C++17, dynamic exception specifications (throw(int, float, ...)) were removed.
// The only remaining specification is `noexcept`, which guarantees that a function
// will not throw. If a noexcept function does throw, std::terminate is called.

// This function promises not to throw
void safeFunction() noexcept
{
    std::println("safeFunction: I promise not to throw");
}

// This function may throw (default behavior, same as noexcept(false))
void riskyFunction()
{
    throw std::runtime_error("something went wrong");
}

// noexcept can also be conditional
template <typename T>
void process(T value) noexcept(std::is_integral_v<T>)
{
    if constexpr (std::is_integral_v<T>)
    {
        std::println("Processing integral value: {} (noexcept)", value);
    }
    else
    {
        std::println("Processing non-integral value: {} (may throw)", value);
        throw std::runtime_error("non-integral error");
    }
}

int main()
{
    // noexcept can be queried at compile time
    std::println("safeFunction is noexcept: {}", noexcept(safeFunction()));
    std::println("riskyFunction is noexcept: {}", noexcept(riskyFunction()));
    std::println("process<int> is noexcept: {}", noexcept(process(42)));
    std::println("process<double> is noexcept: {}", noexcept(process(3.14)));

    safeFunction();

    try
    {
        riskyFunction();
    }
    catch (const std::exception& e)
    {
        std::println("Caught: {}", e.what());
    }

    // Safe: int is integral → noexcept(true)
    process(42);

    // This would throw → catch it
    try
    {
        process(3.14);
    }
    catch (const std::exception& e)
    {
        std::println("Caught from process<double>: {}", e.what());
    }

    // WARNING: calling safeFunction with a throw inside would call std::terminate!
    // Uncomment to test (program will abort):
    // auto dangerous = []() noexcept { throw std::runtime_error("oops"); };
    // dangerous(); // → std::terminate()

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_08.06_VectorBoundsException" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.06_VectorBoundsException_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// A simple Vector class that demonstrates both implicit exceptions (bad_alloc
// from new[]) and explicit exceptions (bounds checking with const char*).

class Vector
{
public:
    explicit Vector(int size) : m_size(size)
    {
        m_data = new double[m_size]; // may throw std::bad_alloc
    }

    ~Vector()
    {
        delete[] m_data;
        m_data = nullptr;
    }

    double& operator[](int i)
    {
        validateIndex(i);
        return m_data[i];
    }

private:
    void validateIndex(int i) const
    {
        if (i < 0 || i >= m_size)
        {
            throw "Index out of bounds!";
        }
    }

    double* m_data{nullptr};
    int m_size{0};
};

int main()
{
    int n = 0;
    int i = 0;
    double x = 0.0;

    std::print("Number of vector components: n = ");
    std::cin >> n;

    try
    {
        Vector v(n); // if n is too large → bad_alloc
        std::print("Index and value of a component: i, v[i] ? ");
        std::cin >> i >> x;
        v[i] = x; // if i is out of [0..n-1] → throws const char*
        std::println("v[{}] = {}", i, x);
    }
    catch (const char* message)
    {
        std::println("{}", message);
    }
    catch (const std::bad_alloc&)
    {
        std::println("Memory allocation failed");
    }
    catch (...)
    {
        std::println("Unknown error");
    }

    std::println("Done");

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_08.07_CatchByReference" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.07_CatchByReference_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// Catching exceptions by reference preserves polymorphism.
// Catching by value causes slicing — the derived part is lost.

class Exception1 : public std::exception
{
public:
    const char* what() const noexcept override
    {
        return "Exception1";
    }
};

class Exception2 : public std::exception
{
public:
    const char* what() const noexcept override
    {
        return "Exception2";
    }
};

int main()
{
    // Catch by REFERENCE: polymorphism works — calls Exception1::what()
    try
    {
        std::println("--- Catch by reference ---");
        throw Exception1();
    }
    catch (const std::exception& e)
    {
        std::println("Caught: {}", e.what()); // prints "Exception1"
    }

    // Catch by VALUE: slicing occurs — calls std::exception::what()
    try
    {
        std::println("--- Catch by value ---");
        throw Exception2();
    }
    catch (const std::exception e) // NOLINT: intentional catch by value
    {
        std::println("Caught: {}", e.what()); // prints "std::exception" (sliced!)
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

{{<details "1242.2_08.08_CustomExceptionClass" >}}
**`main.cpp`**
<!-- SNIPPET:BEGIN source_file=main.cpp id=1242.2_Examples_08.08_CustomExceptionClass_main.cpp -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
```cpp
// A custom exception class that inherits from std::exception.
// Uses __LINE__ to include the source line number in the error message.

class MyException : public std::exception
{
public:
    MyException(const char* message, int line)
        : m_msg(std::format("Error at line {}: {}", line, message))
    {
    }

    const char* what() const noexcept override
    {
        return m_msg.c_str();
    }

private:
    std::string m_msg;
};

int main()
{
    try
    {
        throw MyException("something went wrong", __LINE__);
    }
    catch (const std::exception& e)
    {
        std::println("{}", e.what());
    }

    return 0;
}
```
<!-- SNIPPET:END -->
{{</details>}}

## Serie 8.1
### Exercice 1

Le programme ci-dessous teste la validité d'une valeur saisie au clavier, qui doit être positive, impaire et comprise entre deux valeurs.
Les erreurs sont transmises en levant des exceptions.

{{<a_noter>}}
Pour les besoins des exercices, il est demandé d'utiliser des exceptions pour signaler des erreurs "communes".
Dans la pratique, il est important de faire la distinction entre les erreurs "communes" (ex: valeur saisie par l'utilisateur invalide) et les erreurs "exceptionnelles" (ex: échec d'une allocation mémoire).
- **Les erreurs communes** peuvent être gérées par des mécanismes de contrôle de flux
- **Les erreurs exceptionnelles** doivent être gérées par des exceptions
{{</a_noter>}}

```cpp
int main()
{
  auto minValue = 10;
  auto maxValue = 100;
  auto value = 0;

  std::println("Enter a positive and odd value [{}-{}]: ", minValue, maxValue);
  std::cin >> value;
  
  isPositive(value);
  isOdd(value);
  isLessThan(value, maxValue);
  isGreaterThan(value, minValue);
  
  std::println("Correct value !\n");
  
  return 0;
}
```

Écrire les fonctions suivantes :

**`void isPositive(int value)`**
- si la valeur est positive, afficher " - OK: It's a positive value "
- sinon, lever une exception qui envoie la valeur (`value`).

**`void isOdd(int value)`**
- si la valeur est impaire, afficher " - OK: It's an odd value"
- sinon, lever une exception et envoyer la chaine de caractères: "The value is even".
  
**`void isLessThan(int value, int maxValue)`**
- si la valeur est plus petite que `maxValue`, afficher "- OK: It's a value less than 100"
- sinon, lever une exception qui envoye une instance de la classe `MyException` qui hérite de la classe C++ `exception` (`#include <exception>`)
  - écrire un constructeur de cette classe qui puisse reçevoir le message d'erreur : "The value is too big"
  - redéfinir la méthode `what()` afin qu'elle affiche le message passé au constructeur
  
**`void isGreaterThan(int value, int minValue)`**
- idem que pour le cas précédent

Dans le **`main`**, il s'agit de disposer des **`try`** et **`catch`** aux bons endroits.

#### Exemples
```
Enter a positive and odd value [10, 100] : 11
- OK: It's a positive value
- OK: It's an odd value
- OK: It's a value less than 100
- OK: It's a value greater than 10
Correct value !
```

``` 
Enter a positive and odd value [10, 100] : 12
- OK: It's a positive value
Incorrect value ! ->  The value is even  
```

```
Enter a positive and odd value [10, 100] : 3
- OK: It's a positive value
- OK: It's an odd value
- OK: It's a value less than 100
Incorrect value ! ->  The value is too small
```

## Serie 8.2

### Exercice 1

Reprendre la classe **`Vector`** de la série 3.2 et y ajouter le traitement des exceptions susceptibles d’être levées.

Supposons la fonction **`main()`** suivante :

```cpp
int main()
{
  const int SIZE = 2147483647;
  
  // A) Test de l'allocation dans le constructeur  Vector(int, int)
  Vector v1(SIZE);
  
  // B) Test de l'allocation dans l'opérateur d'assignement 
  for()   ...
  tabV[i] = v1;
    ...
    
    // C) Afficher la taille des vecteurs du tableau
    ...
    
    // D) Test de l'allocation dans le constructeur  Vector(int, int)
    Vector v2(SIZE);

    // E) Test de l'allocation dans le constructeur  par recopie Vector(int, int)
    Vector v3 = v1; 

    // F) Test de l'allocation dans l'opérateur d'affectation
    Vector v5;
    v5 = v1;
 
    // G) Test du constructeur Vector(int, int) avec une taille incorrecte
    Vector v6(-1);

    // H) Test de l'accès  hors limites à un vecteur
    v1[-1] = 5;

    // I) Test de l'accès  hors limites à un std::vector
    cout << tabV.at(-1).getSize() << endl;

    return 0;
}
```

Des exceptions peuvent se produire dans les situations suivantes :

A) Lors de la création d’un objet de type **`Vector(int, int)`**

B) Lors de l'affectation d'un vecteur à un autre vecteur :
   - construire un **`std::vector`** contenant 10 vecteurs de type **`Vector`**, puis copiez le vecteur **`v1`** dans ce tableau afin de voir apparaitre une exception.

C) Afficher la taille des vecteurs du tableau
  
D) Lors de la création d’un objet de type **`Vector(int, int)`**

E) Lors de la création d’un objet de type **`Vector(const Vector&)`**

F) Lors de l'affectation d'un vecteur à un autre vecteur 

H) Lors d'un accès hors limite à un vecteur

I) Lors d'un accès hors limite à un **`std::vector`** avec l'opérateur **`at()`**

Remarque :
- il ne faut pas mettre l'ensemble du programme dans un **`try`**
- en cas d'erreur d'allocation d'un Vecteur, il faut s'assurer celui-ci est remis en ordre et le programme **`main()`** doit continuer.
