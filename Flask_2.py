#Dynamic URL and Variable Rules
'''
When creating an application, it’s quite cumbersome to hard-code each URL.
A better way to resolve this problem is through building Dynamic URLs.
Let us briefly understand the meaning of a few common terms first.

Dynamic Routing: It is the process of getting dynamic data(variable names) in the URL and then using it.
Variable Rules: Variable sections can be added to a URL by marking sections with <variable_name>.

Now consider a situation where you have many users and you want to route the user to a specific page
with his or her name or ID in the URL as well as the template. If you try to do this manually then you
have to manually type the complete URL for every user. Doing this can be very tedious and next to impossible.
However, this can be solved using the flask with something called dynamic routing.

Let’s allow the user with having an ID of less than 25 to visit the page. The modified code with dynamic URL binding is given below.
The function uses the <variable name> passed in route() decorator as an argument.
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return 'You are at home page.'

'''
@app.route('/allow')
def allow():
    return 'You have been allowed to enter.'


@app.route('/disallow')
def disallow():
    return 'You have not been allowed to enter.'
'''

@app.route('/allow/<int:Number>')
def allow(Number):
    if Number <= 25:
        return f'You have been allowed to enter because your number is {str(Number)}'
    else:
       return f'You are not allowed because ID is above 25'


if __name__ == '__main__':
    app.run(debug=True)
