# FastAPI: A Beginner’s Guide

## What is FastAPI?

FastAPI is a modern Python framework for building web APIs. An API is a way for programs to ask each other for information or to request an action. For example, a weather app might ask a weather API for the forecast in a particular city.

FastAPI aims to make APIs both quick to build and efficient to run. It combines the Starlette toolkit for web handling with Pydantic for validating data, and it can run on ASGI servers such as Uvicorn.

> **Everyday analogy:** Think of an API as a restaurant counter. A customer places an order in a known format, the kitchen processes it, and the counter returns the result. FastAPI helps define the menu, check that orders make sense, and serve many customers smoothly.

## Two kinds of “fast”

### Fast to run

FastAPI is built for ASGI, the asynchronous server interface used by Python web applications. With asynchronous code, an application can make progress on other requests while waiting for a slow operation—such as a database or another service—to respond.

This is especially useful when an API spends time waiting on network or database activity. It does not make every piece of code automatically faster: CPU-heavy work may need a different approach, and async benefits depend on how the application is written.

> **Analogy:** Imagine one cashier serving several customers. When one customer is waiting for a card payment to finish, the cashier can take the next customer’s order instead of standing idle. Async programming helps an API make productive use of waiting time.

### Fast to code

FastAPI reduces repetitive setup by using Python type hints and Pydantic models to describe and validate incoming data. It can also generate interactive API documentation from the routes and data models in your application.

> **Analogy:** Type hints and validation work like an order form with required fields and clear rules. If a customer leaves out a required detail or enters a value in the wrong format, the system can point that out before the kitchen starts preparing the order.

## FastAPI compared with Flask

Flask is a popular, flexible Python web framework. FastAPI is designed specifically around API development, type-hint-based validation, generated schemas, and ASGI support. The best fit depends on the project and the team: Flask can be a good choice for a small or highly customized application, while FastAPI provides useful API-focused features out of the box.

> **Analogy:** Flask is like a flexible workshop where you choose and assemble many of your own tools. FastAPI is like a workshop with several common API tools already arranged and connected. Either can produce a good result; the starting point differs.

## Install FastAPI and Uvicorn

A virtual environment keeps a project’s Python packages separate from other projects. Uvicorn is an ASGI server that runs the FastAPI application and accepts web requests.

In a terminal, create and activate a virtual environment, then install the packages:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

Install FastAPI and Uvicorn:

```bash
pip install "fastapi[standard]" uvicorn
```

The `fastapi[standard]` extra includes commonly used dependencies and tools. Installing Uvicorn explicitly makes the server dependency clear.

## Create a Hello World API

Create a file named `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
```

Here’s what each part does:

- `FastAPI()` creates the application.
- `@app.get("/")` registers a route for HTTP GET requests to the root path `/`.
- `read_root()` handles requests to that route.
- The returned Python dictionary is sent as JSON, a common format for API data.

> **Analogy:** The route is an address on the restaurant’s menu. `GET /` says, “When someone asks for the home page, use this handler.” The handler prepares the response and hands it back to the customer.

Run the application from the directory containing `main.py`:

```bash
uvicorn main:app --reload
```

`main:app` means “load the `app` object from `main.py`.” `--reload` restarts the development server when you edit the code; it is intended for local development.

Open `http://127.0.0.1:8000/` in a browser. The response should look like:

```json
{"message":"Hello, world!"}
```

## Try the interactive API documentation

With the server running, open:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

FastAPI builds these documentation pages from the application’s routes and data definitions. Swagger UI lets you inspect an endpoint and send a test request in the browser.

> **Analogy:** The `/docs` page is both a menu and a practice counter. It shows what the API can do and lets you try an order without first building a separate client application.

## What to remember

- FastAPI is a Python framework focused on building APIs.
- ASGI and asynchronous programming help applications handle waiting and concurrent requests efficiently when used appropriately.
- Pydantic helps validate and describe data.
- Uvicorn runs the application as an ASGI server.
- FastAPI generates interactive API documentation, including `/docs`.
- A route connects an HTTP method and URL path to a Python function.

The video’s key takeaway is that a small API can be started with little boilerplate, while FastAPI’s validation and documentation features can support larger projects as they grow.
