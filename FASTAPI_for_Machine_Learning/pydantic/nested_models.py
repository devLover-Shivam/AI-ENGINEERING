from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    #complex data type address
    address: Address

address_dict = {'city':'haldia','state':'west bengal','pin':'721657'}

address1 = Address(**address_dict)

patient_dict= {
    'name':'shivam',
    'gender':'male',
    'age':'35',
    'address':address1
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

#Better organisation of related data(e.g. vitals,address,insurance)

#Reusability: Use vitals in mulitple models(e.g.,Patient,MedicalRecord)
#Readability:Easier for developers and API consumers to understand
#Validation: Nested Models are validated automatically-no extra work needed