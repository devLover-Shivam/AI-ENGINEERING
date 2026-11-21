# Why Use Pydantic?

Python is dynamically typed: a variable can hold different kinds of values while the program runs. Type hints such as `name: str` and `age: int` help readers and editor tools understand the code, but Python does not enforce those hints by itself.

Without a validation library, developers must check every input manually. In the example below, the insert function checks that age is not negative, but the update function checks only the types. That means an update with age `-5` would be accepted. As an application grows, repeating and maintaining these checks across many functions becomes difficult.

```python
def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("age cant be negative")
        print("Inserted into database")
    else:
        raise TypeError("Incorrect Data Type")


def update_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print("Updated")
    else:
        raise TypeError("Incorrect Data Type")
```

## A real-life analogy

Imagine a senior developer writes these patient functions and shares them with a junior developer. The junior imports the functions into another part of the application. They might accidentally call `insert_patient_data("Asha", "30")`, passing the age as text, or call `update_patient_data("Asha", -5)`. The first call raises a type error; the second slips through because the update function forgot the non-negative age rule. The problem is not that the junior is careless—the rules are scattered and easy to miss.

Pydantic lets the senior developer define the rules once in a reusable model. When incoming data is checked against that model, Pydantic parses and validates it, and reports clear validation errors when it does not meet the model's requirements. FastAPI uses Pydantic models to validate request data and describe API inputs. This keeps validation consistent and reduces repetitive checks.

Pydantic does not make Python statically typed. It adds runtime validation at the points where data enters your application.
