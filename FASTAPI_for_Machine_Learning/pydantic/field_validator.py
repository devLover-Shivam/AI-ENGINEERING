#the patient model we made earlier , suppose this model is used by other banking enterprises where their clients can have their treatment at a discounted rate but to validate those users they have their own custom email id's assosciated with their bank for example rameh@hdfc.com so we need to verify that only those specific clients get the discount, and for that reason we need feild validator.

from typing import Dict, List, Optional

from pydantic import BaseModel, EmailStr, field_validator


class Patient(BaseModel):
    """
    Define the patient data this program accepts.

    Pydantic checks the supplied values when a Patient is created. It can
    convert compatible values, such as the text "30" into the integer 30,
    and raises a validation error when a value fails a rule.
    """

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_email_domain(cls, value: EmailStr) -> EmailStr:
        """
        Allow email addresses from the partner banks' domains only.

        EmailStr first checks that the value is a valid email address.
        This validator then checks its domain, the part after "@".
        """
        valid_domains = ["hdfc.com", "icici.com"]

        domain_name = str(value).split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Email must use an approved bank domain.")

        return value

    @field_validator("name")
    @classmethod
    def capitalize_name(cls, value: str) -> str:
        """Store the patient's name in uppercase for consistent display."""
        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value: int) -> int:
        """
        Check the age after Pydantic has validated and converted its type.

        For example, the string "30" in patient_info is converted to integer
        30 before this check runs.
        """
        if 0 < value < 100:
            return value

        raise ValueError("Age must be greater than 0 and less than 100.")


def update_patient_data(patient: Patient) -> None:
    """Example of using validated patient data when updating a record."""
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Updated in database")


# Example data that might come from an API request or another part of a program.
patient_info = {
    "name": "Nitish",
    "email": "nitish@hdfc.com",
    "age": "30",  # Pydantic converts this compatible text value to integer 30.
    "weight": 75.2,
    "married": True,
    "contact_details": {"phone": "1234567890"},
}

# ** unpacks the dictionary into named fields.
# Creating the Patient runs Pydantic's type checks and field validators.
patient = Patient(**patient_info)

# Pass the validated Patient object to the update function.
update_patient_data(patient)