# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 00:26:28 2021

@author: pauls
"""

from flask import Flask, url_for, request, redirect, abort, jsonify, abort, send_from_directory
import logging
from flask_cors import CORS
from plant_dao import plantdao

app = Flask(__name__,
            static_url_path = "", 
            static_folder = "staticpages")
# Requests were blocked by CORS policy until this was added
CORS(app)

# Keep json objects sorted as in dictionary
app.config['JSON_SORT_KEYS'] = False

# Send logs to file
logging.basicConfig(filename="serverlog.log", 
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

# Index
@app.route('/')
def index():
    content = send_from_directory('staticpages', "login.html")
    return content

# Get all
@app.route('/plants')
def getAll():
    return jsonify(plantdao.getAll())

# Get all types
@app.route('/types')
def getAllTypes():
    return jsonify(plantdao.getAllTypes())

# Find by name/type
@app.route('/plants/<string:name>')
def findByNameOrType(name):
    return jsonify(plantdao.findByNameOrType(name))

# Find by need
@app.route('/plants/<light>/<water>')
def findByNeed(light, water):
    return jsonify(plantdao.findByNeed(light, water))

# Create plant
@app.route('/plants', methods=['POST'])         
def createPlant():
    if not request.json:
        abort(400)

    plant = {
        "name": request.json["name"],
        "scientific_name": request.json["scientific_name"],
        "light_needs": request.json["light_needs"],
        "water_needs": request.json["water_needs"],
        "plant_type": request.json["plant_type"],
        "stock": request.json["stock"]
    }

    return jsonify(plantdao.createPlant(plant))

# Update 
@app.route('/plants/<string:name>', methods=['PUT'])
def update(name):
    foundplants = plantdao.findByNameOrType(name)
    if foundplants == []:
        abort(404, "Page not found")

    if "price" in request.json:
        plantdao.updatePrice(foundplants[0]["plant_type"], request.json["price"])
    if "name" in request.json:
        foundplants[0]["name"] = request.json["name"]
    if "scientific_name" in request.json:
        foundplants[0]["scientific_name"] = request.json["scientific_name"]
    if "light_needs" in request.json:
        foundplants[0]["light_needs"] = request.json["light_needs"]
    if "water_needs" in request.json:
        foundplants[0]["water_needs"] = request.json["water_needs"]
    if "plant_type" in request.json:
        foundplants[0]["plant_type"] = request.json["plant_type"]
    if "stock" in request.json:
        foundplants[0]["stock"] = request.json["stock"]    
    
    plantdao.updatePlant(foundplants[0]["name"], foundplants[0])

    return jsonify(plantdao.findByNameOrType(name))

# Delete
@app.route('/plants/<string:name>', methods=['DELETE'])
def delete(name):
        plantdao.deletePlant(name)
        return jsonify({"done": True})

# Run main
if __name__ == "__main__":
   app.run(debug=True)