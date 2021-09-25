#POST
'''
Used to send HTML form data to server. Data received by POST method is not cached by server.
HTTP post method sends encrypted data to the requested script.
When Flask request post is used the form data is collected from the requesting form and passed on to the script.
This data is not sent along with URL as arguments. This sent data is not visible in the URL.
'''
from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/quiz', methods=["POST"])
def quiz():
    shu = request.form.get('sub')
    return shu

if __name__ == '__main__':
   app.run(debug = True)