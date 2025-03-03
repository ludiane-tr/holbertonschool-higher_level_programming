# SQL Project

## Description
This project aims to familiarize you with the basics of SQL, MySQL, and PostgreSQL. Through a series of exercises, you will learn to manipulate relational databases, execute queries, and understand the fundamental concepts of SQL.

## Learning Objectives
### General
- What a database is
- What a relational database is
- The meaning of SQL
- What MySQL and PostgreSQL are
- How to create a MySQL/PostgreSQL database
- The difference between DDL and DML
- How to create or modify a table
- How to select data from a table
- How to insert, update, or delete data
- What subqueries are
- How to use SQL functions

## Prerequisites and Setup
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be executed on Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25) and PostgreSQL 14
- All files must end with a new line
- Each SQL query must be preceded by an explanatory comment
- All files must start with a comment describing the task
- SQL keywords must be in uppercase (`SELECT`, `WHERE`, etc.)
- A `README.md` file is mandatory at the root of the project
- File lengths will be checked using the `wc` command

## Installation Instructions for MySQL and PostgreSQL
### MySQL on Ubuntu 22.04
1. Request an Ubuntu 22.04 container
2. Update the package list:
   ```sh
   apt update
   ```
3. Install MySQL:
   ```sh
   apt install -y mysql-server
   ```
4. Verify the installation:
   ```sh
   mysql --version
   ```
5. Start the MySQL service:
   ```sh
   service mysql start
   ```
6. Connect to the MySQL server:
   ```sh
   mysql -uroot
   ```

### PostgreSQL on Ubuntu 22.04
1. Update the package list:
   ```sh
   apt update
   ```
2. Install PostgreSQL:
   ```sh
   apt install -y postgresql postgresql-contrib
   ```
3. Verify the installation:
   ```sh
   psql --version
   ```
4. Start the PostgreSQL service:
   ```sh
   service postgresql start
   ```
5. Connect to the PostgreSQL server:
   ```sh
   sudo -i -u postgres psql
   ```

## List of Exercises
```markdown
1. `0-list_databases.sql` - List databases
2. `1-create_database.sql` - Create a database
3. `2-delete_database.sql` - Delete a database
4. `3-list_tables.sql` - List tables in a database
5. `4-first_table.sql` - Create a first table
6. `5-full_description.sql` - Display the full description of a table
7. `6-list_all_in_table.sql` - Show all content in a table
8. `7-first_add.sql` - Add a first entry to a table
9. `8-count_89.sql` - Count entries with a specific value
10. `9-full_creation.sql` - Create a table with constraints
11. `10-list_by_best.sql` - List entries by performance order
12. `11-select_the_best.sql` - Select the best entries
13. `12-cheating_is_bad.sql` - Delete a specific entry
14. `13-score_too_low.sql` - Delete entries with low scores
15. `14-average.sql` - Compute an average
16. `15-number_by_score.sql` - Count entries by score
17. `16-say_my_name.sql` - Execute a custom query
```

## Author
Project completed as part of the Holberton School curricul