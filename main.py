from flask import Flask, render_template, redirect, request, url_for, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/mk_res')
def mk_res():
    return render_template("make_reservation.html")


if __name__ == '__main__':
    app.run(debug=True)