from fastapi import FastAPI
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