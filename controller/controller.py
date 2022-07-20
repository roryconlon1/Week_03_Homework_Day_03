from tokenize import Number
from app import app
from flask import render_template
from models.shopping_list import people as all_people

@app.route('/')
def index():
    return 'Hi'

@app.route('/order')
def people():
    return render_template('index.html', title="Order", all_people=all_people )

@app.route('/<index>')
def  order(index):
    order_number = int(index)
    return render_template('order.html', title='Individual Order', orders=all_people[order_number])