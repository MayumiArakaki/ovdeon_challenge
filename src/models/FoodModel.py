from database.db_foods import get_connection
from .entities.Food import Food

class FoodModel():
    
    @classmethod
    def get_foods(self):
        try:
            connection = get_connection()
            foods = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, type_food, price, image FROM food ORDER BY name ASC")
                resultset=cursor.fetchall()

                for row in resultset:
                    food = Food(row[0], row[1], row[2], row[3], row[4])
                    foods.append(food.to_JSON())
            
            connection.close()
            return foods
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_food(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, type_food, price, image FROM food WHERE id = %s",(id,))
                row = cursor.fetchone()

                food = None
                if row != None:
                    food = Food(row[0], row[1], row[2])
                    food = food.to_JSON()
            
            connection.close()
            return food
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_food(self, food):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO food (id, name, type_food, price, image) VALUES (%s, %s, %s, %s, %s)""", (food.id, food.name, food.type_food, food.price, food.image))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_food(self, food):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE food SET name=%s, type_food=%s, price=%s, image=%s WHERE id=%s""", (food.name, food.type_food, food.price, food.image, food.id))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_food(self, food):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM food WHERE id= %s)", (food.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    
