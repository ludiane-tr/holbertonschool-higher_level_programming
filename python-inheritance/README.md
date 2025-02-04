# Python - Inheritance

## Description
This project is an introduction to inheritance in Python, focusing on object-oriented programming concepts. By the end of this project, you should be able to explain the fundamentals of inheritance, including its purpose, how to create subclasses, and how to use built-in functions like `isinstance`, `issubclass`, `type`, and `super`.

## Learning Objectives
At the end of this project, you will be able to:

- Explain what a superclass, base class, or parent class is.
- Define and recognize subclasses.
- List all attributes and methods of a class or instance.
- Understand when an instance can have new attributes.
- Inherit a class from another.
- Define a class with multiple base classes.
- Explain the default class that every class inherits from.
- Override methods or attributes inherited from a base class.
- Identify which attributes or methods are available by inheritance to subclasses.
- Explain the purpose of inheritance in object-oriented programming.
- Use the built-in functions `isinstance`, `issubclass`, `type`, and `super` effectively.

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- All files should end with a new line.
- The first line of all files should be exactly:
  ```python
  #!/usr/bin/python3
  ```
- A `README.md` file at the root of the project folder is mandatory.
- Your code should follow the `pycodestyle` (version 2.7.*).
- All files must be executable.
- File length will be tested using `wc`.

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All test files should end with a new line.
- All test files should be inside a folder named `tests`.
- All test files should be text files with the `.txt` extension.
- All tests should be executed using the command:
  ```bash
  python3 -m doctest ./tests/*
  ```
- All modules should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  ```
- All classes should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  ```
- All functions (inside and outside a class) should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
  ```
- Documentation must be meaningful and explain the purpose of the module, class, or method. 

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object.

### 1. My list
Write a class `MyList` that inherits from `list` and has a method to print the list in sorted order.

### 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class.

### 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or inherits from, the specified class.

### 4. Only subclass of
Write a function that returns `True` if the object is strictly a subclass of the specified class.

### 5. Geometry module
Create an empty class `BaseGeometry`.

### 6. Improve Geometry
Add a public instance method `area` that raises an Exception with the message `area() is not implemented`.

### 7. Integer validator
Write a method `integer_validator` that validates if a value is an integer and greater than 0.

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` and implements width and height validation.

## Usage
To run the tasks, ensure your scripts are executable and follow the requirements outlined above. Use the following command to execute a script:
```bash
./<script_name>.py
```

For testing, place your test cases inside the `tests` folder and run:
```bash
python3 -m doctest ./tests/*
```

## Author
- [Your Name]

Feel free to update this README as you progress through the project!
