#!/usr/bin/python3
import sys, os
import sqlite3 as db

####################################################################################
# This script creates or refreshes a database to demonstrate SQL injection attacks
####################################################################################

DB_NAME = "database.db"

try:
    os.remove(os.path.join(sys.path[0], DB_NAME))
    print("Reseting {}...".format(DB_NAME))
except FileNotFoundError:
    print("Initializing {}...".format(DB_NAME))

# Connect to database
connection = db.connect(DB_NAME)

# Create cursor object
cursor = connection.cursor()

# Create sample tables
cursor.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR(32),"
                                                 "firstName VARCHAR(32),"
                                                 "lastName VARCHAR(32),"
                                                 "password VARCHAR(32))")

# Add users to tables
cursor.execute("INSERT INTO users VALUES ('dman27', 'David', 'Madison', 'monkey123')")
cursor.execute("INSERT INTO users VALUES ('agnwl390', 'Allen', 'Mackinzie', 'password1234')")
cursor.execute("INSERT INTO users VALUES ('stwe5528', 'Steven', 'West', 'password!')")
cursor.execute("INSERT INTO users VALUES ('rabl4950', 'Raquel', 'Black', 'tellmeyourname')")
cursor.execute("INSERT INTO users VALUES ('juja1425', 'Juliette', 'Jabroni', 'secret')")
cursor.execute("INSERT INTO users VALUES ('jodo3849', 'John', 'Doe', 'joejoemonkeybo')")
cursor.execute("INSERT INTO users VALUES ('bsmith1424', 'Becky', 'Smith', 'qwerty1234')")

# Save changes and close connection
connection.commit()
connection.close()
