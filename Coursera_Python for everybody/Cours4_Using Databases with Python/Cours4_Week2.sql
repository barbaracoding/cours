
## Examples of SQL commands

## CRUD

# Create
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')

# Read
SELECT * FROM Users # Browse all columns
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name

# Delete
DELETE FROM Users WHERE email='fred@umich.edu'

# Update 
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

