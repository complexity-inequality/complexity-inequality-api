# Shebang

# 
# uvicorn main:app --reload

# libs
from fastapi import FastAPI

# api
app = FastAPI()


@app.get("/")
async def root():

    return {"message": "Hello World"}

