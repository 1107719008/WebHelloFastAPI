import uvicorn
from fastapi import FastAPI
from router import product

app = FastAPI(
    title="Beach Crab API",
    description="期末 Fast API",
    version="0.0.1",
    terms_of_service="http://localhost:5000",
)
app.include_router(product.router)


@app.get("/")
def root():
    return {"title": 'HELLO'}


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)
