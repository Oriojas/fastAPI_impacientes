import uvicorn
import pandas as pd
from fastapi import FastAPI
import data_description as dd
from pydantic import BaseModel
from typing import List, Union
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()  # instancia de la app





@app.get("/hello/")
async def hello():
    greeting = "Hello Word"
    print(f"{greeting}")

    return greeting


@app.get("/hello_you/")
async def hello_you(name: str):
    greeting = f"Hello word {name}"
    print(f"{greeting}")

    return greeting


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
