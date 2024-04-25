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
    with conn.cursor() as cursor:
        sql = "SELECT customerID FROM customers WHERE email = %s"
        cursor.execute(sql, (email))
        cust_id = cursor.fetchone()[0]
        
    # Third create the reservation (insert details into reservation table)
    with conn.cursor as cursor:
        sql = "INSERT INTO reservation (customerID, reservationDateTime, size, tableNumber, specialRequests) VALUES(%s, %s, %s, %s, %s,)"
        cursor.execute(sql, (cust_id, f"{date} {time}", size, '1', splreq))
        conn.commit()
    
    conn.close()