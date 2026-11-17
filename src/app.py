from fastapi import FastAPI


app=FastAPI()

@app.get("/hello-name")
def hello_name():
    return { "user" : "neethunazrin"}


posts={"1":{"name":"san","post_type":"text","update_ts":"2025-09-08 11:11:45"}}
@app.get("/posts")
def get_posts():
    return posts

@app.get("/posts/{id}")
def get_post(id:str):
    return posts[id]



