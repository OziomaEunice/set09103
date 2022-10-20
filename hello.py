# import flask | redirect user to a web page | url_for is used for creating a URL to prevent the overhead of having to change URLs 
# throughout the application (including in templates)
from fileinput import filename
from os import abort
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return "The default, 'root' root" #This will show up in the webpage (in the address code/)

@app.route("/hello/")
def hello():
    return "Hello Napier!!!  :D" #This will show up in the webpage (in the address code/hello/)

@app.route("/hello/<name>") 
def hello2(name):
    return "Hello %s" % name  #This will show up in the webpage (in the address code/hello/eunice). This particular code is useful for
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

# static image example
@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename = 'vmask.jpg')
    end = '">'
    return start + url + end, 200

# In this line the abort function is used which
# immediately causes an error to occur resulting in the corresponding errorhandler being
# called.
@app.route('/force404')
def force404():
    abort(404)

# Create a (custom) error message when a page is not found
@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested", 404

# using GET & POST
@app.route("/account/", methods = ['GET', 'POST'])
def account():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        page = '''
        <html><body>
            <form action = "" method = "post" name = "form">
             <label for = "name">Name:</label>
             <input type = "text" name = "name" id = "name"/>
             <input type = "submit" name = "submit" id = "submit"/>
            </form>
            </body></html>'''
            
        return page
    
# URL variables
@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first + second)

# another hello
@app.route("/hello1/")
def hello3():
    name = request.args.get('name', '')
    if name == '':
        return "no param supplied"
    else:
        return "Hello %s" % name

# using hello.html file
@app.route('/hello2/<name>')
def hello4(name = None):
    user = {'name': name}
    return render_template('hello.html', user = user)


# using conditional.html file
@app.route('/hello3/')
@app.route('/hello3/<name>')
def hello5(name = None):
    user = {'name': name}
    return render_template('conditional.html', name = name)

# using loops.html file
@app.route('/users/')
def users():
    names = ['Simon','Thomas','Lee','Jamie','Sylvester']
    return render_template('loops.html', names = names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)