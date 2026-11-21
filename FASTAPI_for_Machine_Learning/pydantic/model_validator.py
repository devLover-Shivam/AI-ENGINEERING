#suppose in the patient model we need to validate two fields , the field validator is only for single field validation, for more than one field validation we need model validator.

#for example:- suppose we will only create the entry for the patients above 60 yrs old only if they have an emergency contact.to serve this purpose we need model_validator.

from typing import Dict, List, Optional

from pydantic import (
    BaseModel,       # Provides the base class for a Pydantic data model.
    EmailStr,        # Checks that the email field contains a valid email address.
    model_validator, # Checks rules that depend on multiple fields together.
)


class Patient(BaseModel):
    # These type hints describe the patient data Pydantic should validate.
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    # A field validator checks one field at a time. This model validator is
    # useful when a rule depends on multiple fields: here, age and contacts.
    @model_validator(mode="after")
    def validate_emergency_contact(self):
        # Patients older than 60 must have an "emergency" entry in their
        # contact details. If not, raise an error and reject this patient data.
        if self.age > 60 and "emergency" not in self.contact_details:
            raise ValueError(
                "Patients older than 60 must have an emergency contact"
            )

        # Return the validated patient object so Pydantic can finish creating it.
        return self


def update_patient_data(patient: Patient) -> None:
    """Example of using patient data after Pydantic has validated it."""
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Updated in database")


# Example patient data, such as information received from an API request.
patient_info = {
    "name": "Nitish",
    "email": "nitish@hdfc.com",
    "age": "65",  # Pydantic converts this text to the integer 65.
    "weight": 75.2,
    "married": True,
    "contact_details": {
        "phone": "1234567890",
        "emergency": "1234567890",
    },
}

# ** unpacks the dictionary into Patient's named fields.
# Pydantic checks the field types and then runs the model validator.
patient = Patient(**patient_info)

# This function receives the patient only after validation succeeds.
update_patient_data(patient) 