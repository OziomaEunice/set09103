# import flask | redirect user to a web page | url_for is used for creating a URL to prevent the overhead of having to change URLs 
# throughout the application (including in templates)
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return "The default, 'root' root" #This will show up in the webpage (in the address code/)

@app.route("/hello/")
def hello():
    return "Hello Napier!!!  :D" #This will show up in the webpage (in the address code/hello/)

@app.route("/hello/<name>")
def hello2(name):
    return "Hello " + name  #This will show up in the webpage (in the address code/hello/eunice). This particular code is useful for
#for example, when you may want to query a data on a profile.
#In any case, this will print out "Hello" (as in the code above) plus a name you type in after the hello/ .

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world  :("  #This will show up in the webpage (in the address code/goodbye/)


@app.route("/private")
def private():
    # Test for user logged in failed
    # so redirect to login URL
    return redirect(url_for('login')) 

@app.route('/login')
def login():
    return "Now we would get username & password" # This is the login page

# Create a (custom) error message when a page is not found
@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)