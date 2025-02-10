# Python File Manipulation and JSON Handling

## Description
This project focuses on learning essential Python programming concepts such as file manipulation, JSON serialization/deserialization, and using Python data structures effectively. By completing the tasks, you will gain a deeper understanding of how to work with files, process data, and handle command-line arguments in Python.

## Learning Objectives
By the end of this project, you will understand:
- Why Python programming is awesome
- How to open a file
- How to write text to a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to ensure a file is closed after usage
- What the `with` statement is and how to use it
- What JSON is
- The concepts of serialization and deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string back to a Python data structure
- How to access command-line parameters in a Python script

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.8.5**
- All files should end with a new line
- The first line of all files must be: `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should comply with **pycodestyle** (version 2.7.*)
- All files must be executable
- File length will be tested using `wc`

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All test files should end with a new line
- Test files should be inside a `tests` folder
- Test files should have a `.txt` extension
- Tests will be executed with the command: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("module_name").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("module_name").ClassName.__doc__)'`)
- All functions (inside and outside classes) should have documentation:
  - `python3 -c 'print(__import__("module_name").function_name.__doc__)'`
  - `python3 -c 'print(__import__("module_name").ClassName.function_name.__doc__)'`
- Documentation should be a meaningful sentence explaining the purpose of the module, class, or function.

## Project Tasks

### 0. **Read file**
- Implement a function to read the content of a file.

### 1. **Write to a file**
- Create a function to write text to a file and return the number of characters written.

### 2. **Append to a file**
- Write a function to append text to a file and return the number of characters added.

### 3. **To JSON string**
- Implement a function to convert a Python data structure to a JSON string.

### 4. **From JSON string to Object**
- Write a function to deserialize a JSON string back to a Python object.

### 5. **Save Object to a file**
- Create a function that serializes a Python object and saves it to a file.

### 6. **Create object from a JSON file**
- Write a function to deserialize a JSON file into a Python object.

### 7. **Load, add, save**
- Build a script that loads a JSON file, adds new data, and saves the updated object back to the file.

### 8. **Class to JSON**
- Create a function that returns the dictionary representation of a simple class instance.

### 9. **Student to JSON**
- Write a class `Student` and implement a method that serializes its attributes into a dictionary.

### 10. **Student to JSON with filter**
- Extend the `Student` class to serialize specific attributes only, based on a filter.

### 11. **Student to disk and reload**
- Implement methods in the `Student` class to save its attributes to a file and reload them.

### 12. **Pascal's Triangle**
- Create a function to generate Pascal’s Triangle up to a given number of rows.
