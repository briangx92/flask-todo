from flask import Flask, request, render_template
from datetime  import datetime 
import psycopg2




def create_app(): #Factory app
    app = Flask(__name__, instance_relative_config=True) #instantiating object

    conn = psycopg2.connect("dbname='Flask-Todo' host='localhost'")

    cur = conn.cursor()

    cur.execute("CREATE TABLE task (task varchar(30), description varchar(100), created varchar(30));")
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        
        task_date = datetime.now()


        if request.method == 'POST':
            req_task = request.form['task']
            description = request.form['description']
            task_dict = [{'task': req_task, 'description': description, 'time': task_date}]
            return render_template('todo.html',task_dict=task_dict, task_date=task_date)

        
        


        return render_template('index.html')

    
    return app


