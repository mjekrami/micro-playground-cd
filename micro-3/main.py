import os
import uvicorn
from fastapi import FastAPI

__version__ = '0.0.1b'

PORT = os.environ.get("PORT",3000)
HOST = os.environ.get("HOST","0.0.0.0")

app = FastAPI()


@app.get("/version")
def get_version():
    return {"version": __version__, 
            "name":"micro-3"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT,host=HOST)