from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql+psycopg2://doadmin:AVNS_UIvkdQ1sd7yQvtkLK8e@db-postgresql-sfo2-35206-do-user-17895402-0.h.db.ondigitalocean.com:25060/defaultdb?sslmode=require'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


#Initial the Table in DataBase  ⬇︎⬇︎⬇︎⬇︎

#

# Define the animal table
class Animal(db.Model):
    __tablename__ = 'animal'  

    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, nullable=True)  # Foreign key to owner table
    vet_id = db.Column(db.Integer, nullable=True)    # Foreign key to vet table
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=True)  
    breed = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)

# Define the history_bird table
class HistoryBird(db.Model):
    __tablename__ = 'history_bird' 

    case_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, nullable=False)  # Foreign key to animal table
    vet_id = db.Column(db.Integer, nullable=False)     # Foreign key to vet table
    date_visit = db.Column(db.Date, nullable=True)     
    weight = db.Column(db.Numeric, nullable=True)   
    wingspan = db.Column(db.Numeric, nullable=True)    
    comment = db.Column(db.Text, nullable=True)      
    reason_visit = db.Column(db.Text, nullable=True)  
    wingclip = db.Column(db.Boolean, nullable=True)   
    flying_capacity = db.Column(db.Text, nullable=True) 
    cage_only = db.Column(db.Boolean, nullable=True) 

# Define the history_cat table
class HistoryCat(db.Model):
    __tablename__ = 'history_cat'

    case_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, nullable=False)
    vet_id = db.Column(db.Integer, nullable=False)
    date_visit = db.Column(db.Date, nullable=True)
    weight = db.Column(db.Numeric, nullable=True)
    sterilization = db.Column(db.Boolean, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    reason_visit = db.Column(db.Text, nullable=True)
    in_outdoor = db.Column(db.Boolean, nullable=True)
    food_passion = db.Column(db.String(100), nullable=True)

# Define the history_dog table
class HistoryDog(db.Model):
    __tablename__ = 'history_dog'

    case_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, nullable=False)
    vet_id = db.Column(db.Integer, nullable=False)
    date_visit = db.Column(db.Date, nullable=True)
    weight = db.Column(db.Numeric, nullable=True)
    sterilization = db.Column(db.Boolean, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    reason_visit = db.Column(db.Text, nullable=True)
    exercise_level = db.Column(db.String(100), nullable=True)
    food_passion = db.Column(db.String(100), nullable=True)

# Define the history_reptile table
class HistoryReptile(db.Model):
    __tablename__ = 'history_reptile'

    case_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, nullable=False)
    vet_id = db.Column(db.Integer, nullable=False)
    date_visit = db.Column(db.Date, nullable=True)
    weight = db.Column(db.Numeric, nullable=True)
    length = db.Column(db.Numeric, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    reason_visit = db.Column(db.Text, nullable=True)
    housing_type = db.Column(db.String(100), nullable=True)
    temperature_keep = db.Column(db.Numeric, nullable=True)
    humidity_keep = db.Column(db.Numeric, nullable=True)

# Define the medical table
class Medical(db.Model):
    __tablename__ = 'medical'

    medical_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, nullable=False)
    symptoms = db.Column(db.String(255), nullable=True)
    treatment = db.Column(db.Text, nullable=True)
    record_date = db.Column(db.Date, nullable=True)

# Define the medicine table
class Medicine(db.Model):
    __tablename__ = 'medicine'

    medicine_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medical_id = db.Column(db.Integer, nullable=False)
    animal_id = db.Column(db.Integer, nullable=False)
    medicine_name = db.Column(db.String(100), nullable=True)
    doses = db.Column(db.Integer, nullable=True)
    date_issue = db.Column(db.Date, nullable=True)

# Define the owner table
class Owner(db.Model):
    __tablename__ = 'owner'

    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False)

# Define the vaccination table
class Vaccination(db.Model):
    __tablename__ = 'vaccinations'

    vaccine_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, nullable=False)
    vaccine_name = db.Column(db.String(100), nullable=True)
    vaccine_date = db.Column(db.Date, nullable=True)
    num_doses = db.Column(db.Integer, nullable=True)

# Define the vet table
class Vet(db.Model):
    __tablename__ = 'vet'

    vet_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


#Initial some get all function for check update or view    ⬇︎⬇︎⬇︎⬇︎

#

@app.route('/animals', methods=['GET'])
def getAllAnimals():
    animals = Animal.query.order_by(Animal.animal_id).all()
    return jsonify([{
        'Animal_id': animal.animal_id,
        'Owner_id': animal.owner_id,
        'Vet_id': animal.vet_id,
        'Name': animal.name,
        'Last_name': animal.last_name,
        'Species': animal.species,
        'DOB': animal.dob,
        'Breed': animal.breed,
        'Color': animal.color
    } for animal in animals])

@app.route('/history_birds', methods=['GET'])
def getAllHistoryBirds():
    history_birds = HistoryBird.query.order_by(HistoryBird.case_id).all()
    return jsonify([{
        'Case_id': history_bird.case_id,
        'Animal_id': history_bird.animal_id,
        'Vet_id': history_bird.vet_id,
        'Date_visit': history_bird.date_visit,
        'Weight': history_bird.weight,
        'Wingspan': history_bird.wingspan,
        'Comment': history_bird.comment,
        'Reason_visit': history_bird.reason_visit,
        'Wingclip': history_bird.wingclip,
        'Flying_capacity': history_bird.flying_capacity,
        'Cage_only': history_bird.cage_only
    } for history_bird in history_birds])

@app.route('/history_cats', methods=['GET'])
def getAllHistoryCats():
    history_cats = HistoryCat.query.order_by(HistoryCat.case_id).all()
    return jsonify([{
        'Case_id': history_cat.case_id,
        'Animal_id': history_cat.animal_id,
        'Vet_id': history_cat.vet_id,
        'Date_visit': history_cat.date_visit,
        'Weight': history_cat.weight,
        'Sterilization': history_cat.sterilization,
        'Comment': history_cat.comment,
        'Reason_visit': history_cat.reason_visit,
        'In_outdoor': history_cat.in_outdoor,
        'Food_passion': history_cat.food_passion
    } for history_cat in history_cats])

@app.route('/history_dogs', methods=['GET'])
def getAllHistoryDogs():
    history_dogs = HistoryDog.query.order_by(HistoryDog.case_id).all()
    return jsonify([{
        'Case_id': history_dog.case_id,
        'Animal_id': history_dog.animal_id,
        'Vet_id': history_dog.vet_id,
        'Date_visit': history_dog.date_visit,
        'Weight': history_dog.weight,
        'Sterilization': history_dog.sterilization,
        'Comment': history_dog.comment,
        'Reason_visit': history_dog.reason_visit,
        'Exercise_level': history_dog.exercise_level,
        'Food_passion': history_dog.food_passion
    } for history_dog in history_dogs])

@app.route('/history_reptiles', methods=['GET'])
def getAllHistoryReptiles():
    history_reptiles = HistoryReptile.query.order_by(HistoryReptile.case_id).all()
    return jsonify([{
        'Case_id': history_reptile.case_id,
        'Animal_id': history_reptile.animal_id,
        'Vet_id': history_reptile.vet_id,
        'Date_visit': history_reptile.date_visit,
        'Weight': history_reptile.weight,
        'Length': history_reptile.length,
        'Comment': history_reptile.comment,
        'Reason_visit': history_reptile.reason_visit,
        'Housing_type': history_reptile.housing_type,
        'Temperature_keep': history_reptile.temperature_keep,
        'Humidity_keep': history_reptile.humidity_keep
    } for history_reptile in history_reptiles])

@app.route('/medicals', methods=['GET'])
def getAllMedicals():
    medicals = Medical.query.order_by(Medical.medical_id).all()
    return jsonify([{
        'Medical_id': medical.medical_id,
        'Animal_id': medical.animal_id,
        'Symptoms': medical.symptoms,
        'Treatment': medical.treatment,
        'Record_date': medical.record_date
    } for medical in medicals])

@app.route('/medicines', methods=['GET'])
def getAllMedicines():
    medicines = Medicine.query.order_by(Medicine.medicine_id).all()
    return jsonify([{
        'Medicine_id': medicine.medicine_id,
        'Medical_id': medicine.medical_id,
        'Animal_id': medicine.animal_id,
        'Medicine_name': medicine.medicine_name,
        'Doses': medicine.doses,
        'Date_issue': medicine.date_issue
    } for medicine in medicines])

@app.route('/owners', methods=['GET'])
def getAllOwners():
    owners = Owner.query.order_by(Owner.owner_id).all()
    return jsonify([{
        'Owner_id': owner.owner_id,
        'Name': owner.name,
        'Email_address': owner.email_address
    } for owner in owners])

@app.route('/vaccinations', methods=['GET'])
def getAllVaccinations():
    vaccinations = Vaccination.query.order_by(Vaccination.vaccine_id).all()
    return jsonify([{
        'Vaccine_id': vaccination.vaccine_id,
        'Animal_id': vaccination.animal_id,
        'Vaccine_name': vaccination.vaccine_name,
        'Vaccine_date': vaccination.vaccine_date,
        'Num_doses': vaccination.num_doses
    } for vaccination in vaccinations])

@app.route('/vets', methods=['GET'])
def getAllvets():
    vets = Vet.query.order_by(Vet.vet_id).all()
    return jsonify([{
        'Vet_id': vet.vet_id,
        'Role': vet.role,
        'Username': vet.username,
        'Password': vet.password
    } for vet in vets])



@app.route('/animal-list', methods=['GET'])
def animal_list():
    vet_id = request.args.get('vet_id', type=int)

    if not vet_id:
        return jsonify({"error": "vet_id is required"}), 400

    # Filter animals based on the vet_id
    animals = Animal.query.with_entities(
        Animal.animal_id, Animal.name, Animal.last_name, Animal.species, Animal.dob
    ).filter(Animal.vet_id == vet_id).all()

    # Transform data into JSON format
    data = [
        {
            "animal_id": animal.animal_id,
            "name": animal.name,
            "last_name": animal.last_name,
            "species": animal.species,
            "dob": animal.dob.strftime('%Y-%m-%d') if animal.dob else None
        }
        for animal in animals
    ]

    return jsonify(data)





if __name__ == '__main__':
    app.run(debug=True)
