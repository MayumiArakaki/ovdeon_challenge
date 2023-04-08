from flask import Flask

from config import config

app = Flask(__name__)

def page_not_found(error):
    return '<h1>Not found page</h1>', 404

#Routes
from routes import Restaurant

if  __name__=='__main__':
    app.config.from_object(config['development'])


    #Blueprints
    app.register_blueprint(Restaurant.main, url_prefix='/restaurants')
    #error handlers
    app.register_error_handler(404, page_not_found)
    app.run()


