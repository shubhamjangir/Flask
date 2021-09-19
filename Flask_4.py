#Integrating HTML With FLASK Web Framework With HTTP VERBS(Get And POST)

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/',)
def main():
    return render_template('index.html')

@app.route('/success/<int:score>')
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

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    if total_score > 50:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res,score=total_score))
#request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
#request.form['name']: use indexing if you know the key exists
if __name__ == '__main__':
    app.run(debug=True)