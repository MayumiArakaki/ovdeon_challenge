from flask import Blueprint, jsonify, request
import uuid 

# entities
from models.entities.Food import Food
# Models
from models.FoodModel import FoodModel

main = Blueprint ('restaurant_blueprint',__name__)

@main.route('/')
def get_foods():
    try:
        foods = FoodModel.get_foods()
        return jsonify(foods)
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route('/<id>')
def get_food(id):
    try:
        food = FoodModel.get_food(id)
        if food != None:
            return jsonify(food)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route('/add',methods=['POST'])
def add_food():
    try:
        name = request.json('name')
        type_food = request.json('type_food')
        price = request.json('price')
        image = request.json('image')
        id = uuid.uuid4()
        food = Food(str(id), name, type_food, price, image)

        affected_rows=FoodModel.add_food(food)

        if affected_rows ==1:
            return jsonify(food.id)
        else:
            return jsonify({"message": "Error on insert"}),500

    except Exception as ex:
        return jsonify({"message": str(ex)}),500
    
@main.route('/update/<id>',methods=['PUT'])
def update_food(id):
    try:
        name = request.json('name')
        type_food = request.json('type_food')
        price = request.json('price')
        image = request.json('image')
        food = Food(id, name, type_food, price, image)

        affected_rows=FoodModel.update_food(food)

        if affected_rows ==1:
            return jsonify(food.id)
        else:
            return jsonify({"message": "No food updated"}),404

    except Exception as ex:
        return jsonify({"message": str(ex)}),500
    
@main.route('/delete/<id>',methods=['DELETE'])
def delete_food(id):
    try:
        food = Food(id)

        affected_rows=FoodModel.delete_food(food)

        if affected_rows ==1:
            return jsonify(food.id)
        else:
            return jsonify({"message": "No food deleted"}),404

    except Exception as ex:
        return jsonify({"message": str(ex)}),500