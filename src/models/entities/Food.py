from utils.PasswordFormat import PasswordFormat

class Food():

    def __init__(self, id, name=None, type_food=None, price=None, image=None) -> None:
        self.id = id
        self.name = name
        self.type_food = type_food
        self.price = price
        self.image = image

    def to_JSON(self): 
        return {
            'id':self.id,
            'name': self.name,
            'type_food': self.type_food,
            'price' : self.price,
            'image' : self.image
            }

