# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message": 'Hello World to LFH and Alex!'}

from fastapi import FastAPI
from .database import engine
from app import models
from .routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# not needed any more if support alembic
# tell the sqlalchemy to run CREATE statement to generate all the tables
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = ["https://www.google.com"]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

# my_posts =  [{'title':'first post','content':'XCY','id':1}, {'title':'second post','content':'HHHHH','id':2}]

@app.get("/")
def root():
    return {"message": "hello world"}
