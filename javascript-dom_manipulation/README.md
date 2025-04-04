# JavaScript DOM Manipulation

## 📚 Description

This project focuses on learning how to manipulate the **DOM (Document Object Model)** using **JavaScript**. Through various interactive tasks, you will practice selecting, modifying, and dynamically updating HTML elements without reloading the page. You will also perform asynchronous data fetching using **Fetch API**.

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- Select HTML elements using JavaScript
- Understand the difference between `id`, `class`, and tag name selectors
- Modify the style and content of HTML elements
- Dynamically change and manipulate the DOM
- Make requests using `XMLHttpRequest` and the modern `Fetch API`
- Bind to DOM events and user actions (e.g. click events)

---

## ✅ Requirements

- Use **any code editor**
- All code must be compatible with **Chrome v57+**
- All files must end with a **newline**
- A **README.md** file must be present at the root
- Use **semistandard** JavaScript syntax (no `var`)
- Page must **not reload** on DOM interaction or data fetching

---

## 📌 Tasks Overview

### 0. Color Me
Change the color of the `<header>` to red using `document.querySelector`.

### 1. Click and Turn Red
On clicking the element with `id="red_header"`, change the `<header>` text color to red.

### 2. Add `.red` Class
Add the `red` class to `<header>` when clicking on `#red_header`.

### 3. Toggle Classes
Toggle class between `red` and `green` on `<header>` when clicking on `#toggle_header`.

### 4. List of Elements
On click of `#add_item`, append a new `<li>Item</li>` to the list with class `.my_list`.

### 5. Change the Text
Update the `<header>` text to `New Header!!!` when clicking on `#update_header`.

### 6. Star Wars Character
Fetch data from [SWAPI](https://swapi-api.hbtn.io/api/people/5/?format=json) and display the character name in `#character`.

### 7. Star Wars Movies
Fetch all movie titles from [SWAPI](https://swapi-api.hbtn.io/api/films/?format=json) and list them in `#list_movies`.

### 8. Say Hello!
Fetch a translation of "hello" from [Hello API](https://hellosalut.stefanbohacek.dev/?lang=fr) and display it in the `#hello` element. Script must be imported in `<head>`.

## 🧪 Testing

Each script is linked to its corresponding HTML file (e.g., `0-main.html`, `1-main.html`, etc.). Open these HTML files in a **Chrome browser** and verify expected behavior.

---