from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.post("/creation")
async def mock_api():
    await asyncio.sleep(0.5)  # 500 ms delay
    return {
        "id": "123456",
        "profile-id": "01I1000123456"
    }
