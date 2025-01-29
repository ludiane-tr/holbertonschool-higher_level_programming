# More Classes - Python OOP

## Overview
This project covers fundamental Object-Oriented Programming (OOP) concepts in Python, exploring class functionalities and best practices.

## Key Concepts

### Object-Oriented Programming (OOP)
- Python treats everything as an object ("first-class everything").
- A class is a blueprint for creating objects.
- An object is an instance of a class.
- Difference between a class and an instance.

### Attributes & Methods
- Public, protected, and private attributes.
- Using `self` to reference the instance.
- Special methods like `__init__`, `__str__`, and `__repr__`:
  ```python
  class MyClass:
      def __init__(self, name):
          self.name = name
      
      def __str__(self):
          return f"Instance of MyClass: {self.name}"
## Tasks
- [x] Simple rectangle
- [x] Real definition of a rectangle
- [x] Area and Perimeter
- [x] String representation
- [x] Eval is magic
- [x] Detect instance deletion
- [x] How many instances
- [x] Change representation
- [x] Compare rectangles
- [x] A square is a rectangle