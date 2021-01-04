# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:00:41 2021

@author: pauls
"""
#https://enterprise-docs.anaconda.com/en/latest/data-science-workflows/data/mysql.html

import mysql.connector as mysql
import json


# Get credentials from Kubernetes. The credentials were setup as a dictionary.
credentials = None
with open('/var/run/secrets/user_credentials/mysql_credentials') as f:
    credentials = json.load(f)

# Ensure your credentials were setup
if credentials:
    # Connect to the DB
    connection = mysql.connect(
        user=credentials.get('username'),
        password=credentials.get('password'),
        database='employees',
        host='support-mysql.dev.anaconda.com'
    )
    cursor = connection.cursor()

    # Execute the query
    cursor.execute("SELECT first_name, last_name FROM employees LIMIT 20")

    # Loop through the results
    for first_name, last_name in cursor:
        print(f'First name: {first_name}, Last name: {last_name}')


 # Close the connection
    connection.close()