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

    @app.route('/todo', methods=['GET', 'POST'])
    def todo():

        task_list = {
            'Task List': {'Name': '', 'Date': '', 'Time': '', 'Month': '', 'Day': '', 'Completed': '',
        'Task List 1': {'Name': '', 'Date': '', 'Time': '', 'Month': '', 'Day': '', 'Completed': ''}}


        return render_template('todo.html', todo=task_list)


    return app