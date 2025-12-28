from fastapi import FastAPI

app = FastAPI(title="Scalyz Challenge API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Auth API"}

@app.post("/signup")
def signup():
    return {"message": "Signup route placeholder"}

@app.post("/login")
def login():
    return {"message": "Login route placeholder"}
