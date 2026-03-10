from fastapi import FastAPI

app = FastAPI()

# Handles GET /yourname -> "hello_yourname"
@app.get("/{request_data}")
async def read_item(request_data: str):
    return f"hello_{request_data}"

# Handles POST / with body data
@app.post("/")
async def post_item(request_data: str):
    return f"hello_{request_data}"

