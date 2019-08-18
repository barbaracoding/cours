# Many-to-Many Relationships and Python

### 1.Question 1
### How do we model a many-to-many relationship between two database tables?

`We add a table with two foreign keys`

### 2.Question 2
### In Python, what is a database "cursor" most like?

`A file handle

### 3.Question 3
### What method do you call in an SQLIte cursor object in Python to run an SQL command?

`execute()`

### 4.Question 4
### In the following SQL, what is the purpose of the "?"?

`It is a placeholder for the contents of the "org" variable`

### 5.Question 5
### In the following Python code sequence (assuming cur is a SQLite cursor object), what is the value in row if no rows match the WHERE clause?

`None`

### 6.Question 6
### What does the LIMIT clause in the following SQL accomplish?

`It only retrieves the first 10 rows from the table`

### 7.Question 7
### What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?

`It allows multiple SQL statements separated by semicolons

https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.executescript

### 8.Question 8
### What is the purpose of "OR IGNORE" in the following SQL:

`It makes sure that if a particular title is already in the table, there are no duplicate rows inserted`

### 9.Question 9
### For the following Python code to work, what must be added to the title column in the CREATE TABLE statement for the Course table:

`A UNIQUE constraint`


### 9.Question 9
### What do we generally avoid in a many-to-many junction table?

A logical key
or
Two foreign keys
or
Data items specific to the many-to-many relationship