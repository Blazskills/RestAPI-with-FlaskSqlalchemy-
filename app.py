from flask import Flask,request,jsonify,redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from marshmallow import fields, post_dump, pre_dump
# import json
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
class ProductSchema(ma.ModelSchema):
     class Meta:
          # model = product
          fields = ('id','name', 'description','price', 'qty')




#views
@app.route('/')
def index():
     return render_template('index.html')





@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
     if request.method =='POST':
          name = request.form['name']
          description = request.form['description']
          price = request.form['price']
          qty = request.form['qty']
          new_product = product(name = name, description = description, price=price,qty=qty)
          db.session.add(new_product)
          db.session.commit()
          flash("Registed")
          return redirect(url_for('index'))
     return render_template('addproduct.html')


#APIs Connections/Get product

@app.route('/apiaddproduct')
def apiaddproducts():
     products = product.query.all()
     product_schema = ProductSchema(many=True)
     output = product_schema.dump(products).data
     return jsonify({'user': output})

#alternative
# @app.route('/apiaddproduct')
# def apiaddproduct():
#      products = product.query.all()
#      product_schema = ProductSchema(many=True)
#      output = product_schema.dump(products).data
#      return jsonify(output)


#get single product
# @app.route('/updateapiaddproduct/<id>')
# def updateapiaddproduct(id):
#       Product = product.query.get(id)
#       name = request.json['name']
#       description= request.json['description']
#       price=request.json['price']
#       qty = request.json['qty']
      

#       product.name=name
#       product.description=description
#       product.price=price
#       product.qty=qty
      
#       db.session.comment()
#       product_schema = ProductSchema()
#       output = product_schema.dump(Product).data
#       return jsonify(output)


#update single product
@app.route('/apiaddproduct/<id>', methods=['PUT'])
def apiaddproduct(id):

      Product = product.query.get(id)
      product_schema = ProductSchema()
      output = product_schema.dump(Product).data
      return jsonify({'user': output})      
     



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