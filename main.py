import uvicorn
import pandas as pd
from fastapi import FastAPI
import data_description as dd
from pydantic import BaseModel
from typing import List, Union
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()





if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
