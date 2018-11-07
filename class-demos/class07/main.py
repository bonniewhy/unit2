from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

task_list = []

@app.route('/')
def index():
    return render_template('form.html', tasks=task_list)

@app.route('/', methods=['POST'])
def handleTodo():
    task = request.form.get('todo')
    task_list.append(task)

    return render_template("form.html", tasks=task_list, list_title="TODOs")

app.run()