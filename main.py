import uvicorn
import pandas as pd
from fastapi import FastAPI
import data_description as dd
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
    weight: int
    acceleration: float
    modelYear: int
    origin: int
    carName: str


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
    """
    this function sum two numbers
    :param num1: float, first number to sum
    :param num2: float, second number to sum
    :return: float, result of sum
    """
    result = num1 + num2
    string_result = f"La suma de los dos numeros es: {result}"

    return string_result


@app.post("/describe/")
async def describe(json_input: Union[List[dataFrame]]):
    """
    this function return a mpg_car dataframe to describe
    :param json_input: json, input data
    :return: json, resume data from json_input
    """

    json_data_input = jsonable_encoder(json_input)
    df_resp = pd.DataFrame(json_data_input)

    des_dict = dd.dataDescription(df=df_resp).fit()

    json_output = jsonable_encoder(str(des_dict))

    return JSONResponse(content=json_output)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
