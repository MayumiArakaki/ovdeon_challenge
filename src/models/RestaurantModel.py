from database.db_restaurants import get_connection
from .entities.Restaurant import Restaurant

class RestaurantModel():
    
    @classmethod
    def get_restaurants(self):
        try:
            connection = get_connection()
            restaurants = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, password FROM restaurant ORDER BY username ASC")
                resultset=cursor.fetchall()

                for row in resultset:
                    restaurant = Restaurant(row[0], row[1], row[2])
                    restaurants.append(restaurant.to_JSON())
            
            connection.close()
            return restaurants
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_restaurant(self, username):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, password FROM restaurant WHERE username = %s",(username,))
                row = cursor.fetchone()

                restaurant = None
                if row != None:
                    restaurant = Restaurant(row[0], row[1], row[2])
                    restaurant = restaurant.to_JSON()
            
            connection.close()
            return restaurant
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_restaurant(self, restaurant):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO restaurant (id, username, password) VALUES (%s %s, %s)""", (restaurant.id, restaurant.username, restaurant.password))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_restaurant(self, restaurant):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE restaurant SET username=%s, password=%s WHERE id=%s""", (restaurant.username, restaurant.password, restaurant.id))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_restaurant(self, restaurant):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM restaurant WHERE id= %s)", (restaurant.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    
