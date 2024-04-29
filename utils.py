
from flask import request

def process_item(item_name, price_key, quantity_key):
    item_list = []
    name = request.form[item_name]
    price = request.form[price_key]
    quantity = request.form[quantity_key]
    subtotal = float(price) * float(quantity)
    if subtotal > 0:
        item_list.append(name)