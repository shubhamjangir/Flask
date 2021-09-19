#Jinja2 Template Engine

'''

{% ... %} -> for statement
{{     }} ->expression to print
{# ... #} ->comment

'''

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/',)
def main():
    return render_template('index.html')

@app.route('/final_result/<int:score>')
def final_result(score):
    return render_template('result.html',result=score)

'''
@app.route('/success/<int:score>')
def success(score):
    return "The person failed the exam and score is "+str(score)

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
'''
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=''
    return redirect(url_for('final_result',score=total_score))
#Here we have created a index.html and it will help in checking the if condition and show the result, reduces load
#because we will be loading single website.
'''
    if total_score > 50:
        res="success"
    else:
        res="fail"
'''


if __name__ == '__main__':
    app.run(debug=True)