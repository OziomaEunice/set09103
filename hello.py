from flask import Flask
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
    return "Goodbye cruel world  :("

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)