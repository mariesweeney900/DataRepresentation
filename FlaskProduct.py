# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 00:31:14 2021

@author: pauls
"""

#Code adapted from https://github.com/andrewbeattycourseware/dataRepresenation2020/blob/master/code/week05-lecture/servers/restserver.py
#!flask/bin/python
#create products
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

products = [
    {
        "type":"Ketchup",
        "barcode":"56789",
        "make":"Heinz",
        "price":3
    },
    {
        "type":"Potatoes",
        "barcode":"23456",
        "make":"Ardfert",
        "price":9
    },
    {
        "type":"Tomatoes",
        "barcode":"56687",
        "make":"OnTheVine",
        "price":5
    }
]

#https://www.google.com/search?q=app+route+in+flask&oq=app+route+in+flask&aqs=chrome..69i57j0i22i30l7.5908j0j7&sourceid=chrome&ie=UTF-8
#map the specific URL with the associated function
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify( {'products':products})
# curl -i http://localhost:5000/products

@app.route('/products/<string:reg>', methods =['GET'])
def get_products(products):
    foundProducts = list(filter(lambda t : t['type'] == type , products))
    if len(foundProducts) == 0:
        return jsonify( { 'products' : '' }),204
    return jsonify( { 'products' : foundProducts[0] })
#curl -i http://localhost:5000/products/test

@app.route('/products', methods=['POST'])
def create_products():
    if not request.json:
        abort(400)
    if not 'type' in request.json:
        abort(400)
    products={
        "type":  request.json['type'],
        "barcode": request.json['barcode'],
        "make":request.json['make'],
        "price":request.json['price']
    }
    products.append(products)
    return jsonify( {'products':products }),201
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"type":"Ketchup","barcode":"56789","make":"Heinz","price":3}' http://localhost:5000/products
# curl -i -H "Content-Type:application/json" -X POST -d "{\"type\":\"Ketchuo\",\"barcode\":\"56789\",\"make"\":\\"Heinz,\"price\":3}' http://localhost:5000/products

@app.route('/products/<string:reg>', methods =['PUT'])
def update_products(type):
    foundProducts=list(filter(lambda t : t['type'] ==type, products))
    if len(foundProducts) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'barcode' in request.json and type(request.json['barcode']) != str:
        abort(400)
    if 'make' in request.json and type(request.json['make']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    foundProducts[0]['barcode']  = request.json.get('barcode', foundProducts[0]['barcode'])
    foundProducts[0]['make'] =request.json.get('make', foundProducts[0]['make'])
    foundProducts[0]['price'] =request.json.get('price', foundProducts[0]['price'])
    return jsonify( {'products':foundProducts[0]})
#curl -i -H "Content-Type:application/json" -X PUT -d '{"barcode":"56789"}' http://localhost:5000/products
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"barcode\":\"56789\"}" http://localhost:5000/products


@app.route('/products/<string:type>', methods =['DELETE'])
def delete_products(type):
    foundProducts= list(filter (lambda t : t['type'] == type, products))
    if len(foundProducts) == 0:
        abort(404)
    products.remove(foundProducts[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)
