import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class dataFrame(BaseModel):
    mpg: float
    cylinders: int
    displacement: float
    horsepower: float
    weight: float
    acceleration: float
    model: float
    year: int
    origin: int
    car_name: str


@app.get("/hello/")
async def hello():
    greeting = "Hello world"
    print(f"{greeting}")

    return greeting


@app.get("/hello_you/")
async def hello_you(name: str):
    greeting = f"Hello world {name}"
    print(f"{greeting}")

    return greeting


@app.get("/sum_num/")
async def sum_num(num1: float, num2: float):
    result = num1 + num2
    string_result = f"La suma de los dos numéros es: {result}"

    return string_result


@app.post("/describe/")
async def describe(data_frame_j: Union[List[dataFrame]]):
    json_data_input = jsonable_encoder(data_frame_j)

    json_output = jsonable_encoder(json_data_input)

    return json_output


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
