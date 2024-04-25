from flask import Flask, render_template, redirect, request, url_for, jsonify
from db import add_reservation

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

@app.route('/vw_res')
def vw_res():
    return render_template('view_reservation.html')

@app.route('/order_food')
def order_food():
    return render_template("order_food.html")

@app.route('/add_res', methods=['POST'])
def add_res():
    name = request.form['cust-name']
    email = request.form['cust-email']
    number = request.form['cust-num']
    date = request.form['cust-date']
    time = request.form['cust-time']
    size = request.form['cust-size']
    splreq = request.form['cust-requests']
    
    # print(f"Type Number: {type(number)}")
    # print(f"Tyoe date: {type(date)}")
    # print(f"Type time: {type(time)}")
    
    # print(f"Customer Name: {name}")
    # print(f"Customer Name: {email}")
    # print(f"Customer Name: {number}")
    # print(f"Customer Name: {date}")
    # print(f"Customer Name: {time}")
    # print(f"Customer Name: {size}")
    # print(f"Customer Name: {splreq}")

    # add_reservation(name, email, number, date, time, size, splreq)
    
    return(redirect(url_for('vw_res')))

if __name__ == '__main__':
    app.run(debug=True)
