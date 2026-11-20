# Patients Project

## Overview

This project digitizes a clinic’s paper-based patient records with a FastAPI backend. Doctors can manage patient information through API endpoints, with a JSON file used as a simple data store during development.

## Core Features

The API supports five operations:

- Add a patient record.
- Retrieve all patient records.
- Retrieve one patient by ID.
- Update patient information, including recalculating BMI when weight or height changes.
- Delete a patient record.

## Technical Approach

FastAPI provides the backend API, while a JSON file stores patient data for this learning project. The focus is on backend development; a user interface may be added later.
