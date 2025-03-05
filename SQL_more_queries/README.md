# Holberton School - SQL: More Queries

## Description
This project delves deeper into SQL by exploring advanced concepts such as:
- Managing users and privileges in MySQL
- Working with relational databases and foreign keys
- Advanced joins (INNER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN)
- Subqueries and nested queries
- Indexing to optimize query performance
- Using PRIMARY KEY and FOREIGN KEY constraints
- Implementing NOT NULL and UNIQUE constraints
- Retrieving data from multiple tables in one request
- Understanding JOIN and UNION operations

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0 (version 8.0.25)**
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start with a comment describing the task
- All SQL keywords should be in **uppercase** (e.g., `SELECT`, `WHERE`, `JOIN`)
- A `README.md` file at the root of the project is mandatory
- The length of files will be tested using `wc`

## Prerequisites
- MySQL 8.0 or later
- A Unix/Linux terminal
- A text editor (Vim, Emacs, VS Code...)

## Files
This project contains multiple SQL files, each corresponding to a specific task:
- `0-privileges.sql` : Create a user and manage privileges
- `1-create_database_if_missing.sql` : Conditionally create a database
- `2-create_table.sql` : Create a table with a primary key
- `3-create_table_with_fk.sql` : Create a table with a foreign key
- `4-combined_queries.sql` : Execute joins between multiple tables
- `5-full_queries.sql` : Advanced queries with aggregates and groupings

## Task List
- **0. My privileges!** – Write a script that lists all privileges of the MySQL user `user_0d_1` and `user_0d_2`.
- **1. Root user** – Write a script that creates the MySQL server user `user_0d_1` and grants them specific privileges.
- **2. Read user** – Create the MySQL server user `user_0d_2` with SELECT privilege only.
- **3. Always a name** – Create a table `force_name` that does not accept NULL values in the `name` column.
- **4. ID can't be null** – Create a table `id_not_null` with an `id` column that must always have a value.
- **5. Unique ID** – Create a table `unique_id` with an `id` column that must be unique.
- **6. States table** – Create a database `hbtn_0d_usa` and a table `states` with `id` and `name` columns.
- **7. Cities table** – Create a table `cities` linked to `states` via a foreign key.
- **8. Cities of California** – List all cities of California using a join query.
- **9. Cities by States** – List all cities and their corresponding states.
- **10. Genre ID by show** – List all TV shows and their genre IDs.
- **11. Genre ID for all shows** – List all TV shows and their corresponding genres.
- **12. No genre** – List TV shows that do not belong to any genre.
- **13. Number of shows by genre** – Display the number of TV shows per genre.
- **14. My genres** – List genres of the show `Dexter`.
- **15. Only Comedy** – List TV shows that belong only to the genre `Comedy`.
- **16. List shows and genres** – List all shows and genres in a formatted way.
