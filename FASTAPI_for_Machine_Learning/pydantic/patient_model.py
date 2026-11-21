from pydantic import BaseModel  

class Patient(BaseModel):
    #DEFINE YOUR IDEAL SCHEMA
    name: str
    age: int
    weight: float

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into db')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated into db')

patient_info = {'name':'nitish','age':30}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

