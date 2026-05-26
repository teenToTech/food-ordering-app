# Project - Food ordering app 

from flask import Flask , render_template , request

app = Flask(__name__)

orders = [] 

@app.route("/")
def home():
    return render_template("index.html",orders=orders)

@app.route("/orders", methods=["POST"])
def add():

    name = request.form["name"]
    food = request.form["food"]

    order = {
        "Name" : name,
        "Food" : food
    }
    
    orders.append(order)

    return render_template("index.html",orders=orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)