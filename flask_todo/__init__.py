from flask import Flask, request, make_response, render_template, redirect, url_for
from flask_todo.todo import Todos
import psycopg2

conn=psycopg2.connect("dbname='Flask-Todo' host='localhost'")
try:
    conn=psycopg2.connect("dbname='Flask-Todo' host='localhost'")
    print("connection successful")
except:
    print("I am unable to connect to the database.")
    
cur = conn.cursor()
cur.execute("""CREATE TABLE test (test varchar(30)); """)
try:
    cur.execute("""DROP TABLE task""")
    print("table dropped")
except:
    print("I can't drop our test database!")
# rows = cur.fetchall()
# print("\nShow me the databases:\n")
# for row in rows:
#     print("   ", row[0])

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
        # result = None
        # if request.method == 'GET':
        #     return render_template('todo.html')
        # elif request.method == 'POST':
        #     task = request.form['task']
        #     description = request.form['description']
        #     action = request.form['action']

        #     if action == "task":

            
        #     return render_template('todo.html', task=task, description=description, action=action)
        
        return render_template('todo.html', task_list=task_list) 


    return app