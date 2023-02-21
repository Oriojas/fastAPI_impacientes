import uvicorn
from fastapi import FastAPI

app = FastAPI()


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


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
