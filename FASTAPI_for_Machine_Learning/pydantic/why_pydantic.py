#this is a correct way for type validation but this isnt a scalable way to do that
def insert_patient_data(name:str,age: int):
    if type(name) == str and type(age) == int:
        if age<0:
            raise ValueError('age cant be negative')
        else:
            print(name)
            print(age)
            print("Inserted into databse")
    else:
        raise TypeError('Incorrect Data Type')

insert_patient_data('shivam',30)

def update_patient_data(name:str,age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Updated")
    else:
        raise TypeError('Incorrect Data Type')

insert_patient_data('shivam',30)



