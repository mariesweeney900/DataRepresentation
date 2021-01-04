# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:57:41 2021

@author: pauls
"""

import mysql.connector
import static.dbconfig as cfg
import json
from flask import jsonify

# -------------------------------------
# # create a class
# -------------------------------------


class EquipmentDAO:

    db = ""

    # the below lines have become obscolete due to implemetation of the connection pooling
    # def connectToDB(self):  # in case the line below does not work
    #     self.db = mysql.connector.connect(
    #         host=cfg.mysql['host'],
    #         user=cfg.mysql['user'],
    #         password=cfg.mysql['password'],
    #         database=cfg.mysql['database']
    #     )

    def __init__(self):
        # self.connectToDB() # obsolete
        db = self.initConnectToDB()
        db.close()

    # Connection pooling
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database'],
            pool_name="my_connection_pool",
            pool_size=3
        )
        return db

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name="my_connection_pool"
        )
        return db

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    def create(self, values):
        db = self.getConnection()
        # cursor = self.db.cursor() # obsolete
        cursor = db.cursor()
        sql = "INSERT INTO equipment (category, name, supplier, price_eur) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
        db.commit()
        db.close()
        cursor.close()
        return cursor.lastrowid

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()  # was cursor=self.db.cursor()
        sql = "SELECT * FROM equipment"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            # print(result)
            # convert data type from tuple to dictionary
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        db.close()
        return returnArray

    def findByID(self, id):
        db = self.getConnection()
        cursor = db.cursor()  # was cursor=self.db.cursor()
        sql = "SELECT * FROM equipment WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        db.close()
        # convert result to dictionary and return
        return self.convertToDictionary(result)

    def update(self, values):
        db = self.getConnection()
        cursor = db.cursor()  # was cursor=self.db.cursor()
        sql = "UPDATE equipment SET category= %s, name= %s, supplier= %s, price_eur= %s  WHERE id = %s"
        cursor.execute(sql, values)
        db.commit()
        cursor.close()
        db.close()

    def delete(self, id):
        db = self.getConnection()
        cursor = db.cursor()  # was cursor=self.db.cursor()
        sql = "DELETE FROM equipment WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        db.commit()
        cursor.close()
        db.close()
        print("Delete done")

    # Converting tuple returned from DB into dictionary
    def convertToDictionary(self, result):
        # List of attributes - match html with colnames
        colnames = ['id', 'category', 'name', 'supplier', 'price_eur']
        # Empty dict
        item = {}
        # if result exist, enumerate through
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item

# -------------------------------------
# create instance of the class
# -------------------------------------


equipmentDAO = EquipmentDAO()