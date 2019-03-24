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

    @app.route('/todo')
    def todo(name="World"):

        # for key, value in request.args.items():
        #     print(f"{key}: {value}")
        name = request.args.get('name', 'World') # get the request from flask
        return render_template('todo.html', name=name)

    
  


    return app