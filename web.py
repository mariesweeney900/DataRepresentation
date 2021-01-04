# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:22:00 2021

@author: pauls
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'