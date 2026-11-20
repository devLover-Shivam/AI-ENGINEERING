from fastapi import FastAPI

app = FastAPI()

""" GET REQUEST """

@app.get("/")
def hello():
    return{'message':'Hello World'}

@app.get('/about')
def about():
    return {
        'message':'Recode is a social media platform for recoding  your life.'
    }


