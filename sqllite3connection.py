# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:09:14 2021

@author: pauls
"""
#https://www.sqlservertutorial.net/sql-server-sample-database/
#https://www.quora.com/How-do-I-connect-to-SQLite-database-using-Anaconda-Python

import sqlite3 as sql 
  
conn  = sql.connect("mysqlsampledatabase") 
cur = conn.cursor() 
 
ensure_schema = ''' 
CREATE TABLE IF NOT EXISTS atable ( 
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	some_key VARCHAR UNIQUE NOT NULL, 
  some_value VARCHAR 
	)''' 
 
cur.execute(ensure_schema) 
 
 
insert_data = ''' 
INSERT INTO table (some_key, some_value) VALUES (?,?)''' 
 
cur.execute(insert_data, ('foo', 'bar')) 
some_data = ( 
	('fob','baz'), 
	('zoo','bee') 
	) 
cur.executemany(insert_data, some_data) 
 
cur.execute(‘insert into table (some_key) VALUES (?)’, (‘noval’,)) 
 
query = ''' 
SELECT id, some_key, some_value FROM atable''' 
 
sth = cur.execute(query) 
results = sth.fetchall() 
for i, key, val in results: 
	print(i, key, val) 