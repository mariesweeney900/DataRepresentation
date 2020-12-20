# -*- coding: utf-8 -*-
"""BuildProductsDatabase.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fh-EgcswDjOCN-3lxEMcie0PMWMUp5_W
"""

#https://docs.python.org/3/library/sqlite3.html
#Imports the sqllite module and connects to a database created by python anywhere
import sqlite3
conn = sqlite3.connect('products.db')

#https://docs.python.org/3/library/sqlite3.html
#Cursors are created by the connection. cursor() method: the commands are executed by the connection.

c = conn.cursor()

# Create table products
c.execute('''CREATE TABLE products
             (Type, Barcode, Make, Price)''')

# Insert a row of data
c.execute("INSERT INTO products VALUES ('Butter','45678','erin', 3)")

# Save and commit the changes
conn.commit()

# Can close the connection if complete.
#Changes that have been committed will be lost.
conn.close()

#https://docs.python.org/3/library/sqlite3.html

import sqlite3
conn = sqlite3.connect('products.db')
c = conn.cursor()

#https://docs.python.org/3/library/sqlite3.html
#Put ? as a placeholder where =one wants to use a value, and then give a tuple of values as the second argument to the cursor’s execute() method.

m = ('erin',)
c.execute('SELECT * FROM products WHERE Make=?', m)
print(c.fetchone())

# Can insert many records in the one instance
purchases = [('Cookies', '32451', 'Nestle', 2),
             ('Crackers', '26789', 'Goodwins', 2),
             ('Apples', '65789', 'Sams', 2),
            ]
c.executemany('INSERT INTO products VALUES (?,?,?,?)', purchases)