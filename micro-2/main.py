import uvicorn
import os
from fastapi import FastAPI

__version__ = "0.0.1b"

app = FastAPI()

PORT = os.environ.get("PORT", 3000)
HOST = os.environ.get("HOST", "0.0.0.0")


@app.get("/version")
def get_version():
    return {"version": __version__, "name": "micro-2"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST)
