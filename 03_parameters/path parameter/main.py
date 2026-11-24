from fastapi import FastAPI, Path
import json

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

app = FastAPI()
@app.get("/")
def hello():
    return {'message' : 'Patient Managment System API'}

@app.get("/about")
def about():
    return {'message' : 'A fully functional API to manage patient records'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description='Id of the patient in the DB', example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'Error':'Patient not found'}