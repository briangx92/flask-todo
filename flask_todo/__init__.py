from flask import Flask, request, render_template, make_response
from datetime  import datetime
import psycopg2

def create_app(): #Factory app
    app = Flask(__name__, instance_relative_config=True) #instantiating object
    
    conn = psycopg2.connect("dbname=Flask-Todo user=csetuser")

    cur = conn.cursor()

    # cur.execute("CREATE TABLE todos (task varchar(30), description varchar(100), created varchar(30));")
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        task_date = datetime.today()

        if request.method == 'POST':
            task = request.form['task']
            description = request.form['description']
            task_dict = [{'task': task, 'description': description, 'time': task_date, 'complete': False}]
            return render_template('index.html',task_dict=task_dict, task_date=task_date)
        
        elif request.method == 'GET':
            return render_template('index.html')

        cur.execute("INSERT INTO todos (task, description, created, complete) VALUES (%s,%s,%s,%s)", ("task", "description", "task_date", "False"))
        conn.commit()
        cur.close()
        conn.close()
        return render_template('index.html')

    return app


