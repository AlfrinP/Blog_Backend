# all the imports
from blog.blogController import blog_router
from fastapi import FastAPI

# creating a server with python FastAPI
app = FastAPI()

app.include_router(blog_router)


@app.get("/")
def read_root():  # function that is binded with the endpoint
    return {"Hello": "World"}
