# Everything is Object in Python: What I Learned

Understanding how Python handles objects, memory, mutability, and function arguments is crucial to mastering the language. In the project "Everything is Object," I dug into the internals of Python's behavior and uncovered how things really work under the hood. Here’s a breakdown of what I learned.

---

## Introduction

When writing Python, it might seem like you're just assigning variables and manipulating data. But behind the scenes, Python treats **everything as an object**. This includes integers, strings, lists, and even functions themselves. By understanding object identity, mutability, and how variables interact with memory, we gain a powerful toolset for debugging, optimizing, and writing cleaner code.

---

## `id()` and `type()`

In Python, each object has:
- A **type**: which tells what kind of object it is (`int`, `str`, `list`, etc.)
- An **id**: which is its **memory address** (in CPython)

```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # e.g., 140008871395472
```

Knowing the type helps identify how the object behaves. The `id()` function helps determine whether two variables refer to the **same** object in memory.

---

## Mutable Objects

**Mutable** objects can be changed **in place**. Lists are a great example:

```python
my_list = [1, 2, 3]
print(id(my_list))
my_list.append(4)
print(id(my_list))  # Same id as before
```

The same object is modified directly. This can lead to unexpected behaviors when lists are shared across variables or passed into functions.

---

## Immutable Objects

**Immutable** objects cannot be changed after they are created. Any operation that appears to modify them will actually return a **new object**.

```python
a = "hello"
print(id(a))
a += " world"
print(id(a))  # Different id
```

Common immutable types include `int`, `float`, `str`, and `tuple`. Understanding this is key to avoiding confusion when working with these objects.

---

## Memory Optimization: NSMALLPOSINTS and NSMALLNEGINTS

Python (specifically CPython) implements clever memory optimizations using internal constants:

- **`NSMALLPOSINTS` = 257** (caches integers from 0 to 256)
- **`NSMALLNEGINTS` = 5** (caches integers from -5 to -1)

These values are preallocated, so the same object is reused:

```python
a = 100
b = 100
print(a is b)  # True

x = 1000
y = 1000
print(x is y)  # False (usually)
```

This improves performance but can cause surprising behavior when using the `is` operator with numbers.

---

## Why It Matters

Understanding the difference between mutable and immutable objects helps prevent subtle bugs:

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] - both a and b refer to the same list
```

If `a` was a tuple, such behavior wouldn't occur. This difference is crucial when working in collaborative environments or passing data between functions.

---

## Argument Passing in Functions

Python passes variables by **object reference** (not by value or by reference like in other languages). What this means:

- **Immutable objects**: changes inside the function do **not** affect the original
- **Mutable objects**: changes inside the function **do** affect the original

Examples:

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1 - unchanged
```

```python
def add_element(lst):
    lst.append(5)

my_list = [1, 2]
add_element(my_list)
print(my_list)  # [1, 2, 5] - list is modified
```

This behavior must be kept in mind when designing functions that modify their arguments.

---

```python
def copy_list(a_list):
    return a_list[:]
```

- Observe how Python handles identity even when values are equal:

```python
a = (1, 2)
b = (1, 2)
print(a is b)  # True, due to internal optimization (interning)
```

These details reveal the true elegance (and complexity) of how Python treats memory.

---

## Conclusion

This project gave me deep insight into Python’s internals. Understanding object identity, mutability, memory optimization, and function behavior makes me a more confident and capable Python developer. From here, I can write more predictable, efficient, and clean code.

---
