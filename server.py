from flask import Flask, render_template, request
from database.db import connect2SQL, add_user

app = Flask(__name__)

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/register_user', methods = ["post"])
def register_user():
    data_user = request.form
    id = data_user["id"]
    last_name = data_user["last_name"]
    first_name = data_user["first_name"]
    birthday = data_user["birthday"]
    add_user(id,first_name,last_name,birthday)
    return "User added"


if __name__ == "__main__":
    ip = "172.31.19.217"
    port = "80"
    app.run(ip, port)