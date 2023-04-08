from flask import Blueprint, jsonify, request
import uuid 

# entities
from models.entities.Restaurant import Restaurant
# Models
from models.RestaurantModel import RestaurantModel

main = Blueprint ('restaurant_blueprint',__name__)

@main.route('/')
def get_restaurants():
    try:
        restaurants = RestaurantModel.get_restaurants()
        return jsonify(restaurants)
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route('/<username>')
def get_restaurant(username):
    try:
        restaurant = RestaurantModel.get_restaurant(username)
        if restaurant != None:
            return jsonify(restaurant)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route('/add',methods=['POST'])
def add_restaurant():
    try:
        username = request.json('username')
        password = request.json('password')
        id = uuid.uuid4()
        restaurant = Restaurant(str(id), username, password)

        affected_rows=RestaurantModel.add_restaurant(restaurant)

        if affected_rows ==1:
            return jsonify(restaurant.id)
        else:
            return jsonify({"message": "Error on insert"}),500

    except Exception as ex:
        return jsonify({"message": str(ex)}),500
    
@main.route('/add',methods=['PUT'])
def update_restaurant(id):
    try:
        username = request.json('username')
        password = request.json('password')
        restaurant = Restaurant(id, username, password)

        affected_rows=RestaurantModel.update_restaurant(restaurant)

        if affected_rows ==1:
            return jsonify(restaurant.id)
        else:
            return jsonify({"message": "No restaurant updated"}),404

    except Exception as ex:
        return jsonify({"message": str(ex)}),500
    
@main.route('/delete/<id>',methods=['DELETE'])
def delete_restaurant(id):
    try:
        restaurant = Restaurant(id)

        affected_rows=RestaurantModel.add_restaurant(restaurant)

        if affected_rows ==1:
            return jsonify(restaurant.id)
        else:
            return jsonify({"message": "No restaurant deleted"}),404

    except Exception as ex:
        return jsonify({"message": str(ex)}),500