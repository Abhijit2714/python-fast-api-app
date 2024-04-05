from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Hope is a good thing may be the best of things and no good things ever dies!!!! Good Morning!!!!"}
