from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Welcome"

@app.route("/about")
def about():
    return "About us"

@app.route("/services")
def services():
    return "Services"

@app.route("/contact")
def contact():
    return "Contact"

if __name__=='__main__' :
    app.run(debug=True)



   