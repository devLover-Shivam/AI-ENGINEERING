
from pydantic import BaseModel  # Base class for models that validate and organize data.


class Address(BaseModel):
    # Store related address details together in a reusable model.
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    # Pydantic checks the patient data against these field types.
    name: str
    gender: str
    age: int

    # This field contains another model, so the address stays organized
    # as a group of related fields.
    address: Address


# Create and validate an Address object from a dictionary.
address_dict = {
    "city": "Haldia",
    "state": "West Bengal",
    "pin": "721657",
}
address1 = Address(**address_dict)

# Create a Patient object, using the validated Address object.
patient_dict = {
    "name": "Shivam",
    "gender": "male",
    "age": "35",  # Pydantic converts this compatible string to the integer 35.
    "address": address1,
}
patient1 = Patient(**patient_dict)

# Serialization means converting an object's data into a simpler format
# that can be stored or shared, such as a dictionary or JSON.
# It is useful when sending API responses, saving data, or passing it
# between parts of a program.
#
# model_dump() converts the Patient model into a Python dictionary.
# exclude removes the listed fields from that dictionary.
temp = patient1.model_dump(exclude=["name", "gender"])

# Show the serialized dictionary and its Python type.
print(temp)
print(type(temp))
