from flask import Flask,request,jsonify,redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
app.config['SECRET_KEY'] = 'JIHDGJIDHFHJDFJ'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


#init database
db = SQLAlchemy(app)

#init marshmallow
ma = Marshmallow(app)

#product class
class  product(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(100), unique=True)
     description = db.Column(db.String(100))
     price = db.Column(db.Float)
     qty = db.Column(db.Integer)
     

def __init__(self, name,descripton,price,qty):
     self.name = name
     self.description = descripton
     self.price = price
     self.qty = qty



#product name
class ProductSchema(ma.Schema):
     class Meta:
          fields = ('id', 'name', 'description', 'price', 'qty')


# #init schema
product_schema = ProductSchema(strict=True)
products_schema =ProductSchema(many=True,strict=True)



#views
@app.route('/')
def index():
     return render_template('index.html')


# @app.route('/addproduct', methods=['GET','POST'])
# def addproduct():
#      if request.method =='POST':
#           name = request.form['name']
#           description = request.form['description']
#           price = request.form['price']
#           qty = request.form['qty']
#           #json
#           name= request.json['name']
#           description= request.json['description']
#           price= request.json['price']
#           qty= request.json['qty']
#           new_product = product(name,description,price,qty)
#           db.session.add(new_product)
#           db.session.commit()
#           flash("Registed")
#           return 'DONE'
#           # return product_schema.jsonify(new_product)
#      return render_template('addproduct.html')

@app.route('/addproduct', methods=['POST'])
def addproduct():
          name= request.json['name']
          description= request.json['description']
          price= request.json['price']
          qty= request.json['qty']
          new_product = product(name,description,price,qty)
          db.session.add(new_product)
          db.session.commit()
          return product_schema.jsonify(new_product)
     



@app.route('/updateproduct')
def updateproduct():
    return render_template('updateproduct.html')

@app.route('/delete')
def delete():
    return 'deleted'


@app.route('/login')
def login():
     return render_template('login.html')

@app.route('/register')     
def register():
         return render_template('register.html')


@app.route('/logout')
def logout():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('/dashboard/index.html')


#Run server 
if __name__ =='__main__':
    app.run(debug=True)