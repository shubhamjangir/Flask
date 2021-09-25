#GET
'''
Sends data in unencrypted form to the server. Most common method.
HTTP get method sends unencrypted data to the target script through URL for processing.
When Flask request get is used the form data is passed on to the requested script in form action through URL as arguments.
'''

from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/quiz', methods=["GET"])
def quiz():
    shu = request.args.get('sub')
    return shu

if __name__ == '__main__':
   app.run(debug = True)
