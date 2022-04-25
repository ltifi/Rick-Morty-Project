# main.py
# Import FastAPI
from fastapi import FastAPI
from routes.api import router as api_router

# Initialize the app
app = FastAPI()

app.include_router(api_router)


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Rick&Morty Universe"}

