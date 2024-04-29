# db.py model
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    
    return conn


def add_reservation(name, email, number, date, time, size, splreq):
    conn = open_connection()
    
    # First insert into the customer table to generate a customerID
    with conn.cursor() as cursor:
        sql = "INSERT INTO customers (name, email, PhoneNumber) VALUES(%s, %s, %s)"
        cursor.execute(sql, (name, email, number))
        conn.commit()
    
    # Second get the newly generated customerID based on email 
    # with conn.cursor() as cursor:
    #     sql = "SELECT PhoneNumber FROM customers WHERE email = %s"
    #     cursor.execute(sql, (email))
    #     cust_id = cursor.fetchone()[0]  # PhoneNumber instead of cust_id
        
    # Third create the reservation (insert details into reservation table)
    with conn.cursor() as cursor:
        sql = "INSERT INTO reservation (PhoneNumber, reservationDateTime, size, specialRequests) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (number, f"{date} {time}", size, splreq))
        conn.commit()
    
    conn.close()
    
def get_reservation(number):
    conn = open_connection()
    with conn.cursor() as cursor:
        sql = f"SELECT c.name, c.email, c.PhoneNumber, r.reservationDateTime, r.size, r.specialRequests FROM customers AS c INNER JOIN reservation AS r ON c.PhoneNumber = r.PhoneNumber WHERE c.PhoneNumber = {number};"     
        cursor.execute(sql)
        reservation_details = cursor.fetchall()
        return reservation_details
    
def add_membership(name, email, number, dob, address):
    conn = open_connection()
    
    # Insert the data into customer table
    with conn.cursor() as cursor:
        sql = "INSERT INTO customers (name, email, PhoneNumber, address, dob, membership) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, email, number, address, dob, True))
        conn.commit()
        
    conn.close()
    
def add_order(name, email, number, address, totalBill, quantityList, itemList):
    conn = open_connection()
    
    with conn.cursor() as cursor:
        check_num = f"SELECT PhoneNumber FROM customers WHERE PhoneNumber = {number}"
        cursor.execute(check_num)
        result = cursor.fetchone()
        if result:
            pass
        else:
            sql = "INSERT INTO customers (name, email, PhoneNumber, address) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, email, number, address))
            conn.commit()


    # First insert into any_order to generate orderID
    with conn.cursor() as cursor:
        sql = "INSERT INTO any_order (PhoneNumber, totalBill) VALUES (%s, %s)"
        cursor.execute(sql, (number, totalBill))
        conn.commit()
        
    # Getting the most recent orderID based on PhoneNumber
    with conn.cursor() as cursor:
        sql = f"SELECT MAX(orderID) FROM any_order WHERE PhoneNumber = {number}"
        cursor.execute(sql)
        order_id = cursor.fetchone()[0]
        
    # get itemID using item name.
    item_id_list = []
    with conn.cursor() as cursor:
        for item_Name in itemList:
            #sql = f"SELECT itemID FROM menu_items WHERE itemName=?"
            cursor.execute("SELECT itemID FROM menu_items WHERE itemName = %s", [item_Name])
            item_id = cursor.fetchone()
            item_id_list.append(item_id)
            
    # try:
    #     with conn.cursor() as cursor: 
    #         for i_id, item_quantity in zip(item_id_list, quantityList):
    #             print(f"order_id: {order_id}, i_id: {i_id}, item_quantity: {item_quantity}")
    #             sql = "INSERT INTO order_items (orderID, itemID, quantity) VALUES (%s, %s, %s)"
    #             cursor.execute(sql, (order_id, i_id, item_quantity))
    #         conn.commit()
    # except Exception as e:
    #     print(f"Error occured: {e}")

    
    with conn.cursor() as cursor: 
        for i_id, item_quantity in zip(item_id_list, quantityList):
            sql = "INSERT INTO order_items (orderID, itemID, quantity) VALUES (%s, %s, %s)"
            cursor.execute(sql, (order_id, i_id, item_quantity))
        conn.commit()
    
    conn.close()