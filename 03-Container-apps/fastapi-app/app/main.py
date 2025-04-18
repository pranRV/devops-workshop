from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="My FastAPI App")

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Boilerplate"}