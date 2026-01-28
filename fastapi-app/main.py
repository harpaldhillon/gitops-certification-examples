from fastapi import FastAPI, status
from prometheus_fastapi_instrumentator import Instrumentator
import random

app = FastAPI()

# Initialize the Prometheus instrumentation
Instrumentator().instrument(app).expose(app)

# Endpoint that returns a random error code
@app.get("/error")
async def get_error():
    error_codes = [status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR]
    error_code = random.choice(error_codes)
    if error_code == status.HTTP_400_BAD_REQUEST:
        return {"message": "Bad Request"}, error_code
    elif error_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        return {"message": "Internal Server Error"}, error_code

# Endpoint that returns some data (for monitoring purposes)
@app.get("/data")
async def get_data():
    return {"value": 42}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
