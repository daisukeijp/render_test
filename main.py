from fastapi import FastAPI

app = FastAPI()

#"/"にGetリクエストが来た際の処理
@app.get("/")
def index():
    return {"message": "Hello, World"}

#"/items/{item_id}"にGetリクエストが来た際の処理
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

