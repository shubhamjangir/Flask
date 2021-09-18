from flask import Flask #Import Flask module

#Flask Constructor
app = Flask(__name__) #Creating the Flask object, an object of Flask class is considered as the WSGI application

#Flask Decorator
@app.route('/') #URL mapping of the associated function
def home():
    return "Hello, welcome to the home page"
#app.route(rule, options)
#It accepts the following parameters.

#rule: It represents the URL binding with the function.
#options: It represents the list of parameters to be associated with the rule object
#As we can see here, the / URL is bound to the main function which is responsible for returning the server response. It can return a string to be printed on the browser's window or we can use the HTML template to return the HTML file as a response from the server.

if __name__ == '__main__':
    app.run(debug=True)
#app.run(host, port, debug, options)
#SN	Option	Description
#1	host	The default hostname is 127.0.0.1, i.e. localhost.
#2	port	The port number to which the server is listening to. The default port number is 5000.
#3	debug	The default is false. It provides debug information if it is set to true.
#4	options	It contains the information to be forwarded to the server.




