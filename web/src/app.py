from flask import Flask
app = Flask(__name__)

def hello_world():
    return 'Flask Dockerized part 2'

def create_app():
    '''
    Create flask application using app factory
    return: Flask app
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    app.route('/')(hello_world)
    return app
