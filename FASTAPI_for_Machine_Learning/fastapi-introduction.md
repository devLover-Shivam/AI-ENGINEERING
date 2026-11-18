# Introduction to FastAPI for Machine Learning

> **Learning goal:** Understand why APIs matter, how FastAPI helps expose Python code over the web, and how an ML model can move from a notebook into a service that real applications can use.

## 1. From a notebook to a product

A trained machine learning model in a notebook can make predictions, but a notebook is not usually a convenient way for an application or user to request them. A website, mobile app, or another service needs a reliable way to send input and receive a result.

An **API** (Application Programming Interface) provides that connection. It defines how one software component can ask another to perform an operation, what data it must send, and what response it will receive. For an ML system, an API can accept features such as a house's size and location, pass them to a model, and return a predicted price.

This makes the model available to different clients—web, Android, iOS, or other backend services—without rebuilding its logic for every platform.

## 2. The API as a waiter

Imagine a restaurant. A customer chooses a meal and gives the order to a waiter. The waiter takes it to the kitchen, then brings the prepared meal back. The customer does not need to enter the kitchen or know how the chefs work.

In a software system:

- The **client** (for example, a browser or phone app) is the customer.
- The **API** is the waiter. It accepts requests and returns responses according to defined rules.
- The **backend** is the kitchen. It performs the requested work, which might involve a database, business logic, or an ML model.

The API separates the user-facing application from the implementation behind it. The client does not need to know how the model was trained or which Python library runs it; it needs to know what to send and how to interpret the answer.

## 3. Requests, responses, HTTP, and JSON

Web APIs commonly use **HTTP**, the protocol that browsers and servers use to communicate. A client sends an HTTP request to a URL. The request includes a method, headers, and sometimes a body. The server processes it and returns a status code, headers, and usually a body.

For example, a client might send a `POST` request to `/predict` with input values. `POST` is commonly used when sending data for the server to process. A successful response might use status `200` and include the prediction.

**JSON** (JavaScript Object Notation) is a common data format for request and response bodies. It is text-based, compact, and supported by most programming languages:

```json
{
  "area": 85.5,
  "bedrooms": 2
}
```

A response could be:

```json
{
  "estimated_price": 412000
}
```

Because HTTP and JSON are widely supported, the client and server do not need to use the same programming language. A JavaScript phone app can call an API written in Python.

## 4. Why separate the front end and back end?

In a tightly coupled or **monolithic** design, user-interface code and backend behavior are bundled together. This can work well for many applications, especially when they are small. But when every client has to share the same backend behavior, or the interface and backend need to change independently, a clear API boundary becomes useful.

With an API, teams can update or scale the front end and back end independently, and multiple clients can reuse the same service. Third-party applications can also use approved API operations without needing access to the backend's internal code or database. A travel service, for example, can combine information from separate providers through their APIs rather than directly connecting to each provider's internal database.

APIs do not automatically make an application scalable or secure. The API still needs sensible design, access controls, validation, monitoring, and enough server capacity. What it provides is a defined boundary that makes those responsibilities easier to manage.

## 5. How FastAPI fits in

**FastAPI** is a Python framework for building APIs. It lets you define HTTP routes using Python functions and provides request validation and API documentation features. It is a practical fit for ML services because models and much of the Python ML ecosystem already live in Python.

A small API might look like this:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionInput(BaseModel):
    area: float
    bedrooms: int

@app.post("/predict")
def predict(data: PredictionInput):
    # Replace this example calculation with a loaded ML model.
    price = data.area * 3000 + data.bedrooms * 10000
    return {"estimated_price": price}
```

The `PredictionInput` model describes the expected JSON fields and types. FastAPI uses it to parse and validate incoming data. If the client sends invalid input, the framework can return a useful client error instead of passing malformed values into the prediction logic. The route function receives valid data and returns a Python dictionary, which FastAPI serializes as JSON.

FastAPI also generates interactive documentation from the routes and input models. This helps developers inspect available endpoints and try sample requests while building the service.

## 6. Serving a trained ML model

A real prediction service replaces the example calculation with a model trained and saved separately. A simplified flow is:

1. Train and evaluate the model using appropriate data.
2. Save the model artifact and any required preprocessing steps.
3. Load them when the API service starts.
4. Validate each incoming request and prepare features in the same way as training.
5. Run inference and return a structured result.

Conceptually:

```python
@app.post("/predict")
def predict(data: PredictionInput):
    features = [[data.area, data.bedrooms]]
    result = model.predict(features)[0]
    return {"estimated_price": float(result)}
```

The code is illustrative: the real app must load `model`, apply the exact preprocessing used during training, handle errors, and return appropriate units and confidence information when relevant. Keeping training separate from serving is common: training may be resource-intensive and happen periodically, while the API focuses on loading a selected model and making predictions.

## 7. A typical ML API architecture

A request to an ML service typically travels through these parts:

```text
Web / mobile app / another service
                 │  HTTP request with JSON
                 ▼
             FastAPI route
                 ▼
     Validate and prepare input data
                 ▼
         Model inference code
                 ▼
       Prediction and response shaping
                 │  HTTP response with JSON
                 ▼
              API client
```

The client sends features; the API validates them, invokes the model, and returns a result. The model may be the central component instead of a database, though production ML APIs often use both—for example, to retrieve features or record predictions. Authentication, logging, monitoring, and rate limits may also be part of a real service.

## 8. Learning path: build, integrate, deploy

A practical FastAPI learning path has three stages:

1. **FastAPI fundamentals:** Learn routes, HTTP methods, request and response data, validation, and error handling by building a small project.
2. **ML integration:** Load a trained model and expose prediction functionality through a well-defined endpoint.
3. **Deployment:** Package the application and its dependencies in a container such as Docker, then deploy it to a cloud platform such as AWS.

Deployment makes the service reachable outside a developer's computer. It also introduces operational concerns—configuration, security, scaling, monitoring, and keeping model artifacts and dependencies consistent. Start with a small working API, then add these concerns as you prepare it for real users.

## Key idea

An API is a defined communication boundary between software components. FastAPI makes it straightforward to build that boundary in Python. By wrapping a trained model in an API, you can let different applications request predictions through standard HTTP and JSON, while the model and backend remain independently maintained.

