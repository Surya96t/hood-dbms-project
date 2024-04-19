from flask import Flask, render_template, redirect, request, url_for, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/mk_res')
def mk_res():
    return render_template("make_reservation.html")

@app.route('/check_res')
def check_res():
    return render_template("check_reservation.html")

@app.route('/order_food')
def order_fod():
    return render_template("order_food.html")

if __name__ == '__main__':
    app.run(debug=True)