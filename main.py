from fastapi import FastAPI
from datetime import datetime, timezone
import httpx

app = FastAPI()


@app.get("/me")
async def root():
    try:
        async with httpx.AsyncClient(
            timeout=httpx.Timeout(10.0, connect=3.0)
        ) as client:
            resp = await client.get("https://catfact.ninja/fact")
        fact = resp.json().get("fact", "")
        return {
            "status": "success",
            "user": {
                "email": "okpunorrex@gmail.com",
                "name": "Emmanuel Okpunor",
                "stack": "Python",
            },
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            "fact": fact,
        }
    except httpx.RequestError as e:
        return {
            "status": "error",
            "message": str(e),
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        }
