import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import product,user,info,like,comment
from db import models
from db.database import engine


app = FastAPI(
    title="Hw API",
    description="HW Fast API",
    version="0.0.1",
    terms_of_service="http://localhost:5000",
)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(info.router)
app.include_router(like.router)
app.include_router(comment.router)
if __name__ == "__main__":
    uvicorn.run("app:app", port= 5000, reload=True)


origins = [
    'http://localhost:3000',
    'web-production-e392.up.railway.app',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)

#add commit adding commits