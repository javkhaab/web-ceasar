from flask import Flask
from ceasar import rotate_string
from flask import Flask, request
import string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
     <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html> 


"""

@app.route("/", methods=['POST'])
def encrypt():
    a = int(request.form['rot'])
    b = str(request.form['text'])
    c = rotate_string(b,a)
    return "<h1>" + c + "<h1>"


@app.route("/", methods=['GET','POST'])
def index():
    return form

app.run()