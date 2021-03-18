from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)


class Customer(db.Model, SerializerMixin):
    id = db.Column(db.Integer(100))
    name_pers = db.Column(db.String(100))
    ages_all = db.Column(db.Integer(100))
    hobby = db.Column(db.Boolean(100))
    heh = db.Column(db.Boolean(100))
   

class Item(db.Model, SerializerMixin):
    id = db.Column(db.Integer(100))
    name = db.Column(db.String(100))
    price = db.Column(db.Float(100))
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    asd = db.Column(db.String(100))
   

class Hey(db.Model, SerializerMixin):
    id = db.Column(db.Integer(100))
    price = db.Column(db.Float(100))
    asd = db.Column(db.String(100))
    uff = db.Column(db.String(100))
   


db.create_all()
@app.route('/')
def index():
    return "Api"



@app.route('/customer')
def customer_all():
    customer_list = Customer.query.all()
    return jsonify([Customer.to_dict() for Customer in customer_list])


@app.route('/customer/<id>')
def customer_profile(id):
    customer = Customer.query.filter_by(id=id).first()
    return jsonify(customer.to_dict())



@app.route('/customer', methods = ['POST'])
def customer_add():
    data = request.get_json()
    
    id = data["id"]
    name_pers = data["name_pers"]
    ages_all = data["ages_all"]
    hobby = data["hobby"]
    heh = data["heh"]
    customer = Customer( id=id, name_pers=name_pers, AgesAll=ages_all, hobby=hobby, heh=heh)
    db.session.add(customer)
    db.session.commit()
    return 'ok', 201


@app.route('/customer/<int:id>', methods=['DELETE'])
def customer_delete(id):
    customer = Customer.query.filter_by(id=id).first()
    db.session.delete(customer)
    db.session.commit()
    return 'ok', 200

@app.route('/customer/<id>', methods = ['PUT'])
def customer_update(id):
    customer = Customer.query.filter_by(id=id).first()
    data = request.get_json()
    
    id = data["id"]
    name_pers = data["name_pers"]
    ages_all = data["ages_all"]
    hobby = data["hobby"]
    heh = data["heh"]
    
    customer.id = id
    
    customer.name_pers = name_pers
    
    customer.ages_all = ages_all
    
    customer.hobby = hobby
    
    customer.heh = heh
    
    db.session.commit()
    return 'ok', 200





@app.route('/item')
def item_all():
    item_list = Item.query.all()
    return jsonify([Item.to_dict() for Item in item_list])


@app.route('/item/<id>')
def item_profile(id):
    item = Item.query.filter_by(id=id).first()
    return jsonify(item.to_dict())



@app.route('/item', methods = ['POST'])
def item_add():
    data = request.get_json()
    
    id = data["id"]
    name = data["name"]
    price = data["price"]
    customer_id = data["customer_id"]
    asd = data["asd"]
    item = Item( id=id, name=name, price=price, customer_id=customer_id, asd=asd)
    db.session.add(item)
    db.session.commit()
    return 'ok', 201


@app.route('/item/<int:id>', methods=['DELETE'])
def item_delete(id):
    item = Item.query.filter_by(id=id).first()
    db.session.delete(item)
    db.session.commit()
    return 'ok', 200

@app.route('/item/<id>', methods = ['PUT'])
def item_update(id):
    item = Item.query.filter_by(id=id).first()
    data = request.get_json()
    
    id = data["id"]
    name = data["name"]
    price = data["price"]
    customer_id = data["customer_id"]
    asd = data["asd"]
    
    item.id = id
    
    item.name = name
    
    item.price = price
    
    item.customer_id = customer_id
    
    item.asd = asd
    
    db.session.commit()
    return 'ok', 200





@app.route('/hey')
def hey_all():
    hey_list = Hey.query.all()
    return jsonify([Hey.to_dict() for Hey in hey_list])


@app.route('/hey/<id>')
def hey_profile(id):
    hey = Hey.query.filter_by(id=id).first()
    return jsonify(hey.to_dict())



@app.route('/hey', methods = ['POST'])
def hey_add():
    data = request.get_json()
    
    id = data["id"]
    price = data["price"]
    asd = data["asd"]
    uff = data["uff"]
    hey = Hey( id=id, price=price, asd=asd, uff=uff)
    db.session.add(hey)
    db.session.commit()
    return 'ok', 201


@app.route('/hey/<int:id>', methods=['DELETE'])
def hey_delete(id):
    hey = Hey.query.filter_by(id=id).first()
    db.session.delete(hey)
    db.session.commit()
    return 'ok', 200

@app.route('/hey/<id>', methods = ['PUT'])
def hey_update(id):
    hey = Hey.query.filter_by(id=id).first()
    data = request.get_json()
    
    id = data["id"]
    price = data["price"]
    asd = data["asd"]
    uff = data["uff"]
    
    hey.id = id
    
    hey.price = price
    
    hey.asd = asd
    
    hey.uff = uff
    
    db.session.commit()
    return 'ok', 200





if __name__ == '__main__':
    app.run(debug=True)