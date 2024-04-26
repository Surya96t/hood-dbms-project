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