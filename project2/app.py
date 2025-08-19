from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/myDatabase"
client = MongoClient(MONGO_URI)
db = client["myDatabase"]
collection = db["users"]

@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        try:
            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
