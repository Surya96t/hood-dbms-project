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
def order_food():
    return render_template("order_food.html")

@app.route('/add_res', methods=['POST'])
def add_res():
    create(request.form['cust_name'], request.form['cust_email'], request.form['cust_num'],
           request.form['cust_date'], request.form['cust_time'], request.form['cust_size'],
           request.form['cust-requests'])
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
