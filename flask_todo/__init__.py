from flask import Flask, request, make_response, render_template


def create_app(test_config=None): #Factory app
    app = Flask(__name__, instance_relative_config=True) #instantiating object

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index(): 
       return render_template('index.html')

    return app