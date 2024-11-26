from fastapi import FastAPI
from database import MongoDBHandler

app = FastAPI()
db_handler = MongoDBHandler()

@app.get("/status_count")
def get_status_count(start_time: float, end_time: float):
    result = db_handler.aggregate_status_count(start_time, end_time)
    return {"status_counts": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
