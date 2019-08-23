#!/usr/bin/python3

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']



            with sql.connect('database.db') as con:
                cur = con.cursor()

                cur.execute("INSERT INTO  students (name,addr,city,pin) VALUES (?,?,?,?)", (nm,addr,city,pin))
                con.commit()
            msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            con.close()
            return render_template("result.html",msg = msg)
@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur= con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows = rows)

if __name__ == "__main__":
    try:
        conn = sql.connect('database.db')
        print ("Database opened successfully")
        conn.execute('CREATE TABLE if not exists students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
        print ("Table created successfully")
        conn.close()
        app.run(port=5006)
    except:
        print("App failed on boot")
        


