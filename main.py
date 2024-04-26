from flask import Flask, render_template, redirect, request, url_for, jsonify
from db import add_reservation, add_membership, get_reservation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


# Make a reservation 
@app.route('/mk_res')
def mk_res():
    return render_template("make_reservation.html")
    
@app.route('/add_res', methods=['POST'])
def add_res():
    name = request.form['cust-name']
    email = request.form['cust-email']
    number = request.form['cust-num']
    date = request.form['cust-date']
    time = request.form['cust-time']
    size = request.form['cust-size']
    splreq = request.form['cust-requests']

    add_reservation(name, email, number, date, time, size, splreq)
    
    return redirect(url_for('res_congrats'))

@app.route('/res_congrats')
def res_congrats():
    return render_template('res_congrats.html')

# Check reservation using phone number 
@app.route('/check_res', methods=['GET', 'POST'])
def check_res():
    number = request.form['cust-res-num']
    reservation = get_reservation(number)
    return render_template("check_reservation.html", reservation=reservation)


# View the reservation details
@app.route('/vw_res')
def vw_res():
    return render_template('view_reservation.html')




# For Food Ordering stuff 

@app.route('/order_food')
def order_food():
    return render_template("order_food.html")



# For Membership stuff

@app.route('/new_membership')
def new_membership():
    return render_template("new_membership.html")

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['mem-name']
    email = request.form['mem-email']
    number = request.form['mem-num']
    dob = request.form['mem-date']
    address = request.form['mem-address']

    add_membership(name, email, number, dob, address)
    
    return redirect(url_for('member_congrats.html'))


@app.route('/member_congrats')
def member_congrats():
    return render_template("member_congrats.html")

if __name__ == '__main__':
    app.run(debug=True)
