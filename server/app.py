from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import desc


app = Flask(__name__)
CORS(app)
app.template_folder = '../client/templates'
app.static_folder = '../client/static'  # Change this to point to static folder
app.static_url_path = '/static'  # Add this line to define the URL path for static files
app.secret_key = 'v3ry_s3cr3t_k3y!'
# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    #TODO: databse link here
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(vet_id):
    return Vet.query.get(int(vet_id))

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
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.animal_id'), nullable=False)
    vaccine_name = db.Column(db.String(100), nullable=True)
    vaccine_date = db.Column(db.Date, nullable=True)
    num_doses = db.Column(db.Integer, nullable=True)

    # join
    animal = db.relationship('Animal', backref='vaccines')

# Define the vet table
class Vet(UserMixin, db.Model):
    __tablename__ = 'vet'

    vet_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def get_id(self):
        return str(self.vet_id)


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
    medicals = db.session.query(
        Medical.medical_id,
        Medical.animal_id,
        Medical.symptoms,
        Medical.treatment,
        Medical.record_date,
        Animal.name.label('animal_name')
    ).join(Animal, Medical.animal_id == Animal.animal_id).order_by(Medical.medical_id).all()

    return jsonify([{
        'Medical_id': medical.medical_id,
        'Animal_id': medical.animal_id,
        'Animal_name': medical.animal_name,
        'Symptoms': medical.symptoms,
        'Treatment': medical.treatment,
        'Record_date': medical.record_date.strftime('%Y-%m-%d') if medical.record_date else None
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
        'Date_issue': medicine.date_issue.strftime('%Y-%m-%d') if medicine.date_issue else None
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
    results = db.session.query(
        Vaccination.vaccine_id,
        Vaccination.animal_id,
        Animal.name,
        Animal.last_name,
        Vaccination.vaccine_name,
        Vaccination.vaccine_date,
        Vaccination.num_doses
    ).join(Animal, Vaccination.animal_id == Animal.animal_id).order_by(Vaccination.vaccine_id).all()

    vaccine_records = [
        {
            "vaccine_id": row.vaccine_id,
            "animal_id": row.animal_id,
            "animal_name": row.name,
            "last_name": row.last_name,
            "vaccine_name": row.vaccine_name,
            "vaccine_date": row.vaccine_date.strftime('%Y-%m-%d') if row.vaccine_date else None,
            "num_doses": row.num_doses
        }
        for row in results
    ]

    return jsonify(vaccine_records)

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

    # Join with owner table and include owner information
    animals = db.session.query(
        Animal, Owner
    ).outerjoin(
        Owner, Animal.owner_id == Owner.owner_id
    ).filter(
        Animal.vet_id == vet_id
    ).order_by(Animal.animal_id).all()

    data = [{
        "animal_id": animal.animal_id,
        "name": animal.name,
        "last_name": animal.last_name,
        "species": animal.species,
        "dob": animal.dob.strftime('%Y-%m-%d') if animal.dob else None,
        "breed": animal.breed,
        "color": animal.color,
        "owner_name": owner.name if owner else None,
        "owner_email": owner.email_address if owner else None,
        "owner_id": owner.owner_id if owner else None
    } for animal, owner in animals]

    return jsonify(data)

@app.route('/history', methods=['GET'])
def get_history():
    animal_id = request.args.get('animal_id')
    species = request.args.get('species')

    if not animal_id or not species:
        return jsonify([]), 400  # Return empty array instead of error

    try:
        # Get the appropriate history model based on species
        history_model = {
            'Dog': HistoryDog,
            'Cat': HistoryCat,
            'Bird': HistoryBird,
            'Reptile': HistoryReptile
        }.get(species)

        if not history_model:
            return jsonify([]), 400

        cases = history_model.query.filter_by(animal_id=animal_id).order_by(desc(history_model.date_visit)).all()
        return jsonify([{
            'Case_id': case.case_id,
            'Animal_id': case.animal_id,
            'Date_visit': case.date_visit.strftime('%Y-%m-%d') if case.date_visit else None,
            'Reason_visit': case.reason_visit
        } for case in cases])

    except Exception as e:
        print(f"Error fetching history: {str(e)}")
        return jsonify([]), 500

@app.route('/case-details', methods=['GET'])
def get_case_details():
    case_id = request.args.get('case_id', type=int)
    species = request.args.get('species')

    if not case_id or not species:
        return jsonify({"error": "case_id and species are required"}), 400

    history_models = {
        "Bird": HistoryBird,
        "Cat": HistoryCat,
        "Dog": HistoryDog,
        "Reptile": HistoryReptile
    }

    model = history_models.get(species)
    if not model:
        return jsonify({"error": f"Unsupported species: {species}"}), 400

    case = model.query.filter_by(case_id=case_id).first()
    if not case:
        return jsonify({"error": "Case not found"}), 404

    if species == "Bird":
        data = {
            "Case ID": case.case_id,
            "Animal ID": case.animal_id,
            "Date Visit": case.date_visit.strftime('%Y-%m-%d') if case.date_visit else "Unknown",
            "Weight": str(case.weight) if case.weight else "Unknown",
            "Wingspan": str(case.wingspan) if case.wingspan else "Unknown",
            "Wingclip": "Yes" if case.wingclip else "No",
            "Flying Capacity": case.flying_capacity or "Unknown",
            "Cage Only": "Yes" if case.cage_only else "No",
            "Comment": case.comment or "No comment",
            "Reason Visit": case.reason_visit or "No reason provided"
        }
    elif species == "Cat":
        data = {
            "Case ID": case.case_id,
            "Animal ID": case.animal_id,
            "Date Visit": case.date_visit.strftime('%Y-%m-%d') if case.date_visit else "Unknown",
            "Weight": str(case.weight) if case.weight else "Unknown",
            "Sterilization": "Yes" if case.sterilization else "No",
            "In/Outdoor": "Yes" if case.sterilization else "No",
            "Food Passion": case.food_passion or "Unknown",
            "Comment": case.comment or "No comment",
            "Reason Visit": case.reason_visit or "No reason provided"
        }
    elif species == "Dog":
        data = {
            "Case ID": case.case_id,
            "Animal ID": case.animal_id,
            "Date Visit": case.date_visit.strftime('%Y-%m-%d') if case.date_visit else "Unknown",
            "Weight": str(case.weight) if case.weight else "Unknown",
            "Sterilization": "Yes" if case.sterilization else "No",
            "Exercise Level": case.exercise_level or "Unknown",
            "Food Passion": case.food_passion or "Unknown",
            "Comment": case.comment or "No comment",
            "Reason Visit": case.reason_visit or "No reason provided"
        }
    elif species == "Reptile":
        data = {
            "Case ID": case.case_id,
            "Animal ID": case.animal_id,
            "Date Visit": case.date_visit.strftime('%Y-%m-%d') if case.date_visit else "Unknown",
            "Weight": str(case.weight) if case.weight else "Unknown",
            "Length": str(case.length) if case.length else "Unknown",
            "Housing Type": case.housing_type or "Unknown",
            "Temperature Keep": case.temperature_keep or "Unknown",
            "Humidity Keep": case.humidity_keep or "Unknown",
            "Comment": case.comment or "No comment",
            "Reason Visit": case.reason_visit or "No reason provided"
        }
    else:
        return jsonify({"error": f"Unhandled species: {species}"}), 400

    return jsonify(data)

    
@app.route('/add-history', methods=['POST'])
def add_history():
    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400

    species = data.pop('species', None)
    if not species:
        return jsonify({"error": "Species is required"}), 400

    try:
        if species == 'Dog':
            new_history = HistoryDog(
                animal_id=int(data.get('animal_id')),
                vet_id=int(data.get('vet_id')),
                date_visit=data.get('date_visit'),
                weight=float(data.get('weight', 0)),
                sterilization=data.get('sterilization', '').lower() in ['yes', 'true', '1'],
                comment=data.get('comment'),
                reason_visit=data.get('reason_visit'),
                exercise_level=data.get('exercise_level'),
                food_passion=data.get('food_passion'),
            )
        elif species == 'Cat':
            new_history = HistoryCat(
                animal_id=int(data.get('animal_id')),
                vet_id=int(data.get('vet_id')),
                date_visit=data.get('date_visit'),
                weight=float(data.get('weight', 0)),
                sterilization=data.get('sterilization', '').lower() in ['yes', 'true', '1'],
                comment=data.get('comment'),
                reason_visit=data.get('reason_visit'),
                in_outdoor=data.get('in_outdoor', '').lower() in ['indoor', 'true', '1'],
                food_passion=data.get('food_passion'),
            )
        elif species == 'Bird':
            new_history = HistoryBird(
                animal_id=int(data.get('animal_id')),
                vet_id=int(data.get('vet_id')),
                date_visit=data.get('date_visit'),
                weight=float(data.get('weight', 0)),
                wingspan=float(data.get('wingspan', 0)),
                wingclip=data.get('wingclip', '').lower() in ['yes', 'true', '1'],
                flying_capacity=data.get('flying_capacity'),
                cage_only=data.get('cage_only', '').lower() in ['yes', 'true', '1'],
                comment=data.get('comment'),
                reason_visit=data.get('reason_visit'),
            )
        elif species == 'Reptile':
            new_history = HistoryReptile(
                animal_id=int(data.get('animal_id')),
                vet_id=int(data.get('vet_id')),
                date_visit=data.get('date_visit'),
                weight=float(data.get('weight', 0)),
                length=float(data.get('length', 0)),
                temperature_keep=float(data.get('temperature_keep', 0)),
                humidity_keep=float(data.get('humidity_keep', 0)),
                housing_type=data.get('housing_type'),
                comment=data.get('comment'),
                reason_visit=data.get('reason_visit'),
            )
        else:
            return jsonify({"error": f"Unsupported species: {species}"}), 400

        db.session.add(new_history)
        db.session.commit()
        return jsonify({"message": "Record added successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/delete-history', methods=['DELETE'])
def delete_history():
    data = request.json  # Receive JSON payload
    species = data.get('species')
    case_id = data.get('case_id')

    if not species or not case_id:
        return jsonify({"error": "Both species and case_id are required."}), 400

    # Map species to the corresponding model
    history_models = {
        "Dog": HistoryDog,
        "Cat": HistoryCat,
        "Bird": HistoryBird,
        "Reptile": HistoryReptile,
    }

    model = history_models.get(species)
    if not model:
        return jsonify({"error": f"Unsupported species: {species}"}), 400

    try:
        # Query the record
        record = model.query.filter_by(case_id=case_id).first()
        if not record:
            return jsonify({"error": f"No record found for case_id: {case_id} in species: {species}"}), 404

        # Delete the record
        db.session.delete(record)
        db.session.commit()
        return jsonify({"message": "Record deleted successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        print("Error deleting history:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/add-medical', methods=['POST'])
def add_medical():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Create new medical record
        new_medical = Medical(
            animal_id=data.get('animal_id'),
            symptoms=data.get('symptoms'),
            treatment=data.get('treatment'),
            record_date=data.get('record_date')
        )

        db.session.add(new_medical)
        db.session.commit()

        return jsonify({"message": "Medical record added successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route('/add-medicine', methods=['POST'])
def add_medicine():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Create new medicine record
        new_medicine = Medicine(
            medical_id=data.get('medical_id'),
            medicine_name=data.get('medicine_name'),
            doses=data.get('doses'),
            date_issue=data.get('date_issue')
        )

        db.session.add(new_medicine)
        db.session.commit()

        return jsonify({"message": "Medicine record added successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/update-history', methods=['PUT'])
def edit_history():
    data = request.json
    print("Received Data:", data)
    if not data:
        return jsonify({"error": "No data provided"}), 400

    species = data.pop('species', None)
    case_id = data.pop('case_id', None)

    if not species:
        return jsonify({"error": "Species is required"}), 400
    if not case_id:
        return jsonify({"error": "Case ID is required"}), 400

    try:
        if species == 'Dog':
            record = HistoryDog.query.filter_by(case_id=case_id).first()
            if not record:
                return jsonify({"error": f"Record not found for Case ID: {case_id}"}), 404

            # Update fields for Dog
            record.date_visit = data.get('date_visit', record.date_visit)
            record.weight = float(data.get('weight', record.weight or 0))
            record.sterilization = data.get('sterilization', '').lower() in ['yes', 'true', '1']
            record.comment = data.get('comment', record.comment)
            record.reason_visit = data.get('reason_visit', record.reason_visit)
            record.exercise_level = data.get('exercise_level', record.exercise_level)
            record.food_passion = data.get('food_passion', record.food_passion)

        elif species == 'Cat':
            record = HistoryCat.query.filter_by(case_id=case_id).first()
            if not record:
                return jsonify({"error": f"Record not found for Case ID: {case_id}"}), 404

            # Update fields for Cat
            record.date_visit = data.get('date_visit', record.date_visit)
            record.weight = float(data.get('weight', record.weight or 0))
            record.sterilization = data.get('sterilization', '').lower() in ['yes', 'true', '1']
            record.comment = data.get('comment', record.comment)
            record.reason_visit = data.get('reason_visit', record.reason_visit)
            record.in_outdoor = data.get('in_outdoor', '').lower() in ['yes', 'true', '1']
            record.food_passion = data.get('food_passion', record.food_passion)

        elif species == 'Bird':
            record = HistoryBird.query.filter_by(case_id=case_id).first()
            if not record:
                return jsonify({"error": f"Record not found for Case ID: {case_id}"}), 404

            # Update fields for Bird
            record.date_visit = data.get('date_visit', record.date_visit)
            record.weight = float(data.get('weight', record.weight or 0))
            record.wingspan = float(data.get('wingspan', record.wingspan or 0))
            record.wingclip = data.get('wingclip', '').lower() in ['yes', 'true', '1']
            record.flying_capacity = data.get('flying_capacity', record.flying_capacity)
            record.cage_only = data.get('cage_only', '').lower() in ['yes', 'true', '1']
            record.comment = data.get('comment', record.comment)
            record.reason_visit = data.get('reason_visit', record.reason_visit)

        elif species == 'Reptile':
            record = HistoryReptile.query.filter_by(case_id=case_id).first()
            if not record:
                return jsonify({"error": f"Record not found for Case ID: {case_id}"}), 404

            # Update fields for Reptile
            record.date_visit = data.get('date_visit', record.date_visit)
            record.weight = float(data.get('weight', record.weight or 0))
            record.length = float(data.get('length', record.length or 0))
            record.temperature_keep = float(data.get('temperature_keep', record.temperature_keep or 0))
            record.humidity_keep = float(data.get('humidity_keep', record.humidity_keep or 0))
            record.housing_type = data.get('housing_type', record.housing_type)
            record.comment = data.get('comment', record.comment)
            record.reason_visit = data.get('reason_visit', record.reason_visit)

        else:
            return jsonify({"error": f"Unsupported species: {species}"}), 400

        # Commit the changes to the database
        db.session.commit()
        return jsonify({"message": "Record updated successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/update-vaccine', methods=['POST'])
def update_vaccine():
    data = request.json
    vaccine_id = data.get('vaccine_id')
    vaccine_name = data.get('vaccine_name')
    vaccine_date = data.get('vaccine_date')
    num_doses = data.get('num_doses')

    # Update vaccine in the database
    vaccine = Vaccination.query.get(vaccine_id)
    if vaccine:
        vaccine.vaccine_name = vaccine_name
        vaccine.vaccine_date = vaccine_date
        vaccine.num_doses = num_doses
        db.session.commit()
        return jsonify({"message": "Vaccine record updated successfully"}), 200
    else:
        return jsonify({"message": "Vaccine record not found"}), 404


@app.route('/search-animal', methods=['GET'])
def search_animal():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify([]) 

    animals = Animal.query.filter(Animal.name.ilike(f'%{query}%')).all()

    results = [
        {
            'id': animal.animal_id,
            'name': animal.name,
            'last_name': animal.last_name,
            'species': animal.species,
            'dob': animal.dob.strftime('%Y-%m-%d') if animal.dob else None
        }
        for animal in animals
    ]
    return jsonify(results)

@app.route('/check-owner', methods=['GET'])
def check_owner():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400

    owner = Owner.query.filter_by(email_address=email).first()
    if owner:
        return jsonify({"exists": True, "name": owner.name, "owner_id": owner.owner_id})
    return jsonify({"exists": False})

@app.route('/add-animal', methods=['POST'])
def add_animal():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        new_animal = Animal(
            name=data.get('name'),
            last_name=data.get('last_name'),
            species=data.get('species'),
            dob=data.get('dob'),
            breed=data.get('breed'),
            color=data.get('color'),
            vet_id=data.get('vet_id'),
            owner_id=data.get('owner_id')
        )

        db.session.add(new_animal)
        db.session.commit()

        return jsonify({"message": "Animal added successfully", "animal_id": new_animal.animal_id}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/add-owner', methods=['POST'])
def add_owner():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        new_owner = Owner(
            name=data.get('name'),
            email_address=data.get('email')
        )

        db.session.add(new_owner)
        db.session.commit()

        return jsonify({
            "message": "Owner added successfully",
            "owner_id": new_owner.owner_id
        }), 200

    except Exception as e:
        db.session.rollback()
        print(f"Error adding owner: {e}")  # Log the error
        return jsonify({"error": str(e)}), 500

@app.route('/update-animal/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    try:
        data = request.json
        animal = Animal.query.get(animal_id)
        
        if not animal:
            return jsonify({"error": "Animal not found"}), 404

        animal.name = data.get('name', animal.name)
        animal.last_name = data.get('last_name', animal.last_name)
        animal.dob = data.get('dob', animal.dob)
        animal.owner_id = data.get('owner_id', animal.owner_id)

        db.session.commit()
        return jsonify({"message": "Animal updated successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/owner/<int:owner_id>', methods=['GET'])
def get_owner(owner_id):
    owner = Owner.query.get(owner_id)
    if not owner:
        return jsonify({"error": "Owner not found"}), 404
    return jsonify({
        "name": owner.name,
        "email_address": owner.email_address
    })

    results = [
        {
            'id': animal.animal_id,
            'name': animal.name,
            'last_name': animal.last_name,
            'species': animal.species,
            'dob': animal.dob.strftime('%Y-%m-%d') if animal.dob else None
        }
        for animal in animals
    ]
    return jsonify(results)

@app.route('/add-vaccine', methods=['POST'])
def add_vaccine():
    data = request.get_json()  
    print(data)
    if not data.get('animal_id') or not data.get('vaccine_name') or not data.get('vaccine_date') or not data.get('num_doses'):
        return jsonify({'error': 'Missing required fields'}), 400

    new_vaccine = Vaccination(
        animal_id=data['animal_id'],
        vaccine_name=data['vaccine_name'],
        vaccine_date=data['vaccine_date'],
        num_doses=data['num_doses']
    )

    db.session.add(new_vaccine)
    db.session.commit()

    return jsonify({'message': 'Vaccine record added successfully'}), 201
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

        vet = Vet.query.filter_by(username=username).first()
        if vet and vet.password == password:
            login_user(vet)
            return redirect(url_for('home'))
        else:
            if request.is_json:
                return jsonify({'error': 'Invalid username or password'}), 401
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/history_page', methods=['GET'])
@login_required
def history_page():
    return render_template('history.html', active_page='history', vet_id=current_user.vet_id, username=current_user.username)

@app.route('/medical_page', methods=['GET'])
@login_required
def medical_page():
    return render_template('medical.html', active_page='medical', vet_id=current_user.vet_id, username=current_user.username)

@app.route('/vaccination_page', methods=['GET'])
@login_required
def vaccination_page():
    return render_template('vaccination.html', active_page='vaccination', vet_id=current_user.vet_id, username=current_user.username)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html', username=current_user.username, active_page='home', vet_id=current_user.vet_id)



if __name__ == '__main__':
    app.run(debug=True)
