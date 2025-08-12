# all the imports
from starlette.middleware.cors import CORSMiddleware

from blog.blogController import blog_router
from fastapi import FastAPI
from DB import lifespan

# creating a server with python FastAPI
app = FastAPI(lifespan=lifespan)
app.include_router(blog_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
)

@app.get("/")
def read_root():  # function that is binded with the endpoint
    return {"Hello": "World"}
