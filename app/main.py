from typing import Optional 
from fastapi import FastAPI 
from fastapi.responses import HTMLResponse

# Tools
from app.matrix_opeations.matrix_ops import MatrixOperators

app = FastAPI()

default__matrix_csv = "app/matrix.csv"

@app.get("/echo")
def echo(file: Optional[str]=default__matrix_csv):
    """Return a matrix representation in table."""
    try:
        mx_op = MatrixOperators(file)
        return HTMLResponse(content=mx_op.print(mx_op.matrix), status_code=200)
    except Exception as e:
        return e

@app.get("/invert")
def  invert(file: Optional[str]=default__matrix_csv):
    """Return a table with matrix transpose."""
    try:
        mx_op = MatrixOperators(file)
        return HTMLResponse(content=mx_op.print(mx_op.invert()), status_code=200)
    except Exception as e:
        return e

@app.get("/flatten")
def  flatten(file: Optional[str]=default__matrix_csv):
    """Rerturn a vector representation of matrix."""
    try:
        mx_op = MatrixOperators(file)
        return mx_op.flatten().tolist()
    except Exception as e:
        return e


@app.get("/sum")
def  sum(file: Optional[str]=default__matrix_csv):
    """Return cumulative sum of matrix."""
    try:
        mx_op = MatrixOperators(file)
        return mx_op.sum()
    except Exception as e:
        return e


@app.get("/multiply")
def  multiply(file: Optional[str]=default__matrix_csv):
    """Return of matrix values multiplication."""
    try:
        mx_op = MatrixOperators(file)
        return mx_op.multiply()
    except Exception as e:
        return e


@app.get("/")
def  presentation():
    """HI."""
    return {
       "name": "Jose de Jesus Herrera Ledon",
       "email": "jesushledon@gmail.com"
   } 
