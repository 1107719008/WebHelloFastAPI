import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"title":"Hello World"}

if _name_=="_main_":
    uvicorn.run("app:app",port=5000,reload=True)
