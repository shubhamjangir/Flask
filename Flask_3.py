#Building URL Dynamically

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/',)
def main():
    return "Welcome to the home page"

@app.route('/success/<int:score>') #Function name should be different for different URL but it can be same or different for the same URL and fuction
def success(score):
    return "The person cleared the exam and score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person failed the exam and score is "+str(score)

#Result Checker
@app.route('/result_checker/<int:score>')
def result_checker(score):
    result=""
    if score > 50:
        result="success"
    else:
        result = "fail"
    return redirect(url_for(result,score=score))
#While building the URL dynamically we need to provide the same url name so that it can redirect(success,fail)
#and give the score parameter also because success and fail is accepting two parameters

if __name__ == '__main__':
    app.run(debug=True)