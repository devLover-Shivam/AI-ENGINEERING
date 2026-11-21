# Import the tools needed to build the API and describe or report errors.
from fastapi import FastAPI, Path, HTTPException, Query

# Import Python's built-in tool for reading JSON files.
import json

# Create the FastAPI application. Uvicorn uses this object to run the API.
app = FastAPI()


def load_data():
    """Read patient records from patients.json and return them as Python data."""
    # Open patients.json in read mode ('r'). The 'with' block closes the file
    # automatically when the indented code finishes.
    with open("patients.json", "r") as f:
        # Convert the JSON text in the file into Python dictionaries and lists.
        data = json.load(f)

    # Give the loaded patient records back to whoever called this function.
    return data


# Create a GET endpoint at the root URL: http://127.0.0.1:8000/
@app.get("/")
def hello():
    # Return a dictionary. FastAPI sends it to the caller as JSON.
    return {"message": "Patient Management System API"}


# Create a GET endpoint at http://127.0.0.1:8000/about
@app.get("/about")
def about():
    # Briefly describe what this API does.
    return {"message": "A fully functional API to manage your patient records."}


# Create a GET endpoint at http://127.0.0.1:8000/view
@app.get("/view")
def view():
    # Load all patient records from the JSON file.
    data = load_data()

    # Return all the records to the caller.
    return data


# Create a GET endpoint where the patient ID is part of the URL,
# for example: http://127.0.0.1:8000/patient/P001
@app.get("/patient/{patient_id}")
def view_patient(
    # FastAPI takes this value from the URL.
    # Path(...) means the value is required.
    # The description and example appear in the automatic API documentation.
    patient_id: str = Path(
        ...,
        description="ID of the patient from DB",
        example="P001",
    )
):
    # Load all patient records before searching for the requested ID.
    data = load_data()

    # Check whether the requested ID is a key in the patient records.
    if patient_id in data:
        # Return the record for this patient.
        return data[patient_id]

    # If the ID was not found, return an HTTP 404 "Not Found" error.
    raise HTTPException(status_code=404, detail="Patient Not Found!")


# Create a GET endpoint at http://127.0.0.1:8000/sort
@app.get("/sort")
def sort_patients(
    # Query(...) makes sort_by required.
    # The caller can provide it in the URL, such as ?sort_by=height.
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight or bmi",
    ),

    # Set the default order to ascending.
    # The caller can change it with a URL such as ?sort_by=height&order=desc.
    order: str = Query(
        "asc",
        description="Sort in asc or desc order",
    ),
):
    # Only allow sorting by these three patient record fields.
    valid_fields = ["height", "weight", "bmi"]

    # Reject a field name that is not in the allowed list.
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field selected. Choose from {valid_fields}",
        )

    # Only accept "asc" (ascending) or "desc" (descending).
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Choose 'asc' or 'desc'.",
        )

    # Load all patient records from the JSON file.
    data = load_data()

    # Python's sorted() uses reverse=False for ascending and reverse=True
    # for descending. This expression sets the correct value from "order".
    sort_order = True if order == "desc" else False

    # data.values() gives the patient records without their ID keys.
    # key tells sorted() which field to compare for each record.
    # lambda x creates a small function: get the selected field from a record.
    # If that field is missing, use 0 as its value.
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order,
    )

    # Return the patient records in the requested order.
    return sorted_data