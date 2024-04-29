from flask import Flask, render_template, redirect, request, url_for, jsonify, session
from db import add_reservation, add_membership, get_reservation, add_order, get_cust_order_details, get_items_order_detail

app = Flask(__name__)
app.secret_key = "super secret key"

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
    if request.method == 'POST':
        number = request.form['cust-res-num']
        reservation = get_reservation(number)

        return render_template("check_reservation.html", reservation=reservation)
    else:
        return render_template("check_reservation.html")


# View the reservation details
@app.route('/vw_res')
def vw_res():
    return render_template('view_reservation.html')




# For Food Ordering stuff 

@app.route('/order_food', methods=["GET", "POST"])
def order_food():
    if request.method == "POST":
        item_list = []
        quantity_list = []
        ham_name = request.form["item_ham_name"]
        ham_price = request.form["item_ham_price"]
        ham_quantity = request.form["ham_quantity"]
        ham_subtotal = float(ham_price) * float(ham_quantity)
        if int(ham_quantity) > 0:
            item_list.append(ham_name)
            quantity_list.append(ham_quantity)

        salad_name = request.form["item_salad_name"]
        salad_price = request.form['item_salad_price']
        salad_quantity = request.form['salad_quantity']
        salad_subtotal = float(salad_price) * float(salad_quantity)
        if int(salad_quantity) > 0:
            item_list.append(salad_name)
            quantity_list.append(salad_quantity)
        
        
        spa_name = request.form["item_spa_name"]
        spa_price = request.form['item_spa_price']
        spa_quantity = request.form['spa_quantity']
        spa_subtotal = float(spa_price) * float(spa_quantity)
        if int(spa_quantity) > 0:
            item_list.append(spa_name)
            quantity_list.append(spa_quantity)
        
        cheese_name = request.form["item_cheese_name"]
        cheese_price = request.form['item_cheese_price']
        cheese_quantity = request.form['cheese_quantity']
        cheese_subtotal = float(cheese_price) * float(cheese_quantity)
        if int(cheese_quantity) > 0:
            item_list.append(cheese_name)
            quantity_list.append(cheese_quantity)
        
        cooler_name = request.form["item_cooler_name"]
        cooler_price = request.form['item_cooler_price']
        cooler_quantity = request.form['cooler_quantity']
        cooler_subtotal = float(cooler_price) * float(cooler_quantity)
        if int(cooler_quantity) > 0:
            item_list.append(cooler_name)
            quantity_list.append(cooler_quantity)            
        
        fizz_name = request.form["item_fizz_name"]
        fizz_price = request.form['item_fizz_price']
        fizz_quantity = request.form['fizz_quantity']
        fizz_subtotal = float(fizz_price) * float(fizz_quantity)
        if int(fizz_quantity) > 0:
            item_list.append(fizz_name)
            quantity_list.append(fizz_quantity)
        
        grand_total = ham_subtotal + salad_subtotal + spa_subtotal + cheese_subtotal + cooler_subtotal + fizz_subtotal
        
        order_name = request.form["order-name"]
        order_email = request.form["order-email"]
        order_number = request.form["order-num"]
        order_address = request.form["order-address"]

        session["cust_order_number"] = order_number
        
        add_order(order_name, order_email, order_number, order_address, grand_total, quantity_list, item_list)

        cust_details = get_cust_order_details(order_number)
        menu_details = get_items_order_detail(order_number)
        print(cust_details, "\n")
        print(menu_details, "\n")

        return render_template("order_congrats.html", cust_details=cust_details, menu_details=menu_details)
    else:
        return render_template("order_food.html")


@app.route('/order_congrats')
def order_congrats():
    order_number = session.get("cust_order_number")
    
    cust_details, menu_details = get_order_details(order_number)
    
    return render_template("order_congrats.html", cust_details=cust_details, menu_details=menu_details)


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
