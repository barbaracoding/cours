
# create a SQLITE database or use an existing database and create a table in the database called "Ages":

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Barbara', 25);
INSERT INTO Ages (name, age) VALUES ('Elysse', 33);
INSERT INTO Ages (name, age) VALUES ('Mayeul', 32);
INSERT INTO Ages (name, age) VALUES ('Payton', 27);


First row : 426172626172613235