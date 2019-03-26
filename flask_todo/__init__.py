from flask import Flask, request, make_response, render_template, redirect, url_for
from flask_todo.todo import Todos

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

    task1 = Todos(name='Grocery', description='Get milk')
    task2 = Todos(name='Clean', description='Clean room')
    
    task_list = [task1, task2]

    @app.route('/todo', methods=['GET', 'POST'])
    def todo():
        
        return render_template('todo.html', task_list=task_list) 


    return app