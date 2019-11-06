from flask import Flask, render_template, request, url_for 
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask (__name__)

app.config["MONGO_URI"] ="mongodb+srv://test:test123@gantuangco-mcrfn.azure.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app) 

posts = [
    {
        "author": "Melton",
        "title": "Getting started with flask",
        "content": "First Content",
        "date_posted": "November 6, 2019"
    },
    {
        "author": "Rinku",
        "title": "Getting started with flask",
        "content": "Second Content",
        "date_posted": "November 6, 2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html" , title = "about")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/create", methods = ["POST"])
def create():
    if "profile_image" in request.files:
        profile_image = request.files["profile_image"]
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({"username": request.form.get("username"), "profile_image_name": profile_image.filename})
    return "Done!"

#@app.route("/file/<filename>")
#def file(filename):
    #return mongo.send_file(filename)

#@app.route("/profile/<username>")
#def profile(username):
    #user = mongo.db.users.find_one_or_404({"username": username})
    #return f'''
    #<h1>{username}</h1>
    #<img src = "{url for("file", filename = user["profile_image_name"])}">
#'''

if __name__ == "__main__":
    app.run(debug=True)