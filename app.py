from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
faker = Faker()

# person modell definieras här
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(100), nullable=False)
    alder = db.Column(db.Integer)
    telefonnr = db.Column(db.String(20))
    land = db.Column(db.String(50))

# seedning funktionen för att initiera vår databas om den är tom
def seed_data():
    if Person.query.count() == 0:  # Kontrollera om det redan finns data i tabellen
        for _ in range(15):  # Skapa 15 nya personer använt mig av faker för slumpmässig info
            new_person = Person(
                namn=faker.name(),
                alder=random.randint(20, 80),
                telefonnr=faker.phone_number(),
                land=faker.country()
            )
            db.session.add(new_person)
        db.session.commit()

@app.before_first_request
def initialize():
    db.create_all()  # Skapar databastabeller baserat på modellerna om de inte redan finns
    seed_data()  # Seed databasen med fördefinierad data om den är tom        

@app.route('/')
def home():
    persons = Person.query.limit(15).all()  # Begränsa till 15 personer
    return render_template('index.html', persons=persons)

@app.route('/person/<int:person_id>')
def person_detail(person_id):
    person = Person.query.get_or_404(person_id)
    return render_template('person_detail.html', person=person)

if __name__ == '__main__':
    app.run(debug=True)
