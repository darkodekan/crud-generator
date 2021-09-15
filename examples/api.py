from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)


class Osoba(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    ime = db.Column(db.String(100))
    prezime = db.Column(db.String(100))
   

class Zadatak(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    opis = db.Column(db.String(100))
    osoba_id = db.Column(db.Integer, db.ForeignKey("osoba.id"))
   


db.create_all()
@app.route('/')
def index():
    return "Api"



@app.route('/osoba')
def osoba_all():
    osoba_list = Osoba.query.all()
    return jsonify([Osoba.to_dict() for Osoba in osoba_list])


@app.route('/osoba/<id>')
def osoba_profile(id):
    osoba = Osoba.query.filter_by(id=id).first()
    return jsonify(osoba.to_dict())



@app.route('/osoba', methods = ['POST'])
def osoba_add():
    data = request.get_json()
    
    
    
    ime = data["ime"]
    
    prezime = data["prezime"]
    osoba = Osoba(   ime=ime ,  prezime=prezime )
    db.session.add(osoba)
    db.session.commit()
    return 'ok', 201


@app.route('/osoba/<int:id>', methods=['DELETE'])
def osoba_delete(id):
    osoba = Osoba.query.filter_by(id=id).first()
    db.session.delete(osoba)
    db.session.commit()
    return 'ok', 200

@app.route('/osoba/<id>', methods = ['PUT'])
def osoba_update(id):
    osoba = Osoba.query.filter_by(id=id).first()
    data = request.get_json()
    
    
    
    ime = data["ime"]
    
    prezime = data["prezime"]
    
    
    
    
    osoba.ime = ime
    
    
    osoba.prezime = prezime
    
    db.session.commit()
    return 'ok', 200





@app.route('/zadatak')
def zadatak_all():
    zadatak_list = Zadatak.query.all()
    return jsonify([Zadatak.to_dict() for Zadatak in zadatak_list])


@app.route('/zadatak/<id>')
def zadatak_profile(id):
    zadatak = Zadatak.query.filter_by(id=id).first()
    return jsonify(zadatak.to_dict())



@app.route('/zadatak', methods = ['POST'])
def zadatak_add():
    data = request.get_json()
    
    
    
    opis = data["opis"]
    
    osoba = data["osoba"]
    zadatak = Zadatak(   opis=opis ,  osoba=osoba )
    db.session.add(zadatak)
    db.session.commit()
    return 'ok', 201


@app.route('/zadatak/<int:id>', methods=['DELETE'])
def zadatak_delete(id):
    zadatak = Zadatak.query.filter_by(id=id).first()
    db.session.delete(zadatak)
    db.session.commit()
    return 'ok', 200

@app.route('/zadatak/<id>', methods = ['PUT'])
def zadatak_update(id):
    zadatak = Zadatak.query.filter_by(id=id).first()
    data = request.get_json()
    
    
    
    opis = data["opis"]
    
    osoba = data["osoba"]
    
    
    
    
    zadatak.opis = opis
    
    
    zadatak.osoba = osoba
    
    db.session.commit()
    return 'ok', 200





if __name__ == '__main__':
    app.run(debug=True)