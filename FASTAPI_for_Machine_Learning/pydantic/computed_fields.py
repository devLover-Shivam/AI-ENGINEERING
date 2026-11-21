#if we need to calculate something or we can say compute a field from pre-existing fields, we go for computed fields

from typing import Dict, List, Optional

from pydantic import (
    BaseModel,       # Base class for creating a model that validates patient data.
    EmailStr,        # Checks that the email field contains a valid email address.
    computed_field,  # Includes a calculated value as a field in the model's output.
)


class Patient(BaseModel):
    # Pydantic checks the supplied patient data against these types.
    name: str
    email: EmailStr
    age: int
    weight: float  # Patient's weight in kilograms.
    height: float  # Patient's height in meters.
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    # A computed field derives a value from other fields instead of requiring
    # it to be entered separately. Here, BMI is calculated from weight and height.
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        # BMI = weight in kilograms divided by height in meters squared.
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi


def update_patient_data(patient: Patient) -> None:
    """Example of using patient data after Pydantic has validated it."""
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("BMI:", patient.calculate_bmi)
    print("Updated in database")


# Example patient data, such as information received from an API request.
patient_info = {
    "name": "Nitish",
    "email": "nitish@hdfc.com",
    "age": "65",  # Pydantic converts this compatible text value to the integer 65.
    "weight": 75.2,
    "height": 1.72,
    "married": True,
    "contact_details": {
        "phone": "1234567890",
        "emergency": "1234567890",
    },
}

# ** unpacks the dictionary into Patient's named fields.
# Pydantic validates the data and creates a Patient object.
patient = Patient(**patient_info)

# The BMI is calculated from the patient's weight and height when accessed.
update_patient_data(patient)