from flask import Flask, redirect, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

header = """
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
"""

footer = """
    </body>
    </html>
"""

form = """
    <form action="/" method="POST" />
        <label for="user_input">User Input: 
            <input type="text" name="user_input" id="user_input" value="{0}"/>
        </label>
        <br>
        <label for="another_input">Another Input: 
            <input type="text" name="another_input" id="another_input" value="{1}" />
        </label>
        <input type="submit" value="Enter" />
    </form>
"""

@app.route('/')
def get_index():
    return header + form.format("", "") + footer

@app.route('/', methods=['POST'])
def post_index():
    user_input = request.form.get("user_input")
    another_input = request.form.get("another_input")
    
    user_input = user_input * 2 if not user_input is None else ""
    another_input = another_input * 2 if not another_input is None else ""
    
    return header + form.format(user_input, another_input) + footer

app.run()