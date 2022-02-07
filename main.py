from msilib.schema import Error
from typing import Optional 
from fastapi import FastAPI 

# Tools
from matrix_opeations.matrix_ops import MatrixOperators

app = FastAPI()

@app.get("/echo")
def echo(file: Optional[str]='matrix.csv'):
    try:
        mx_op = MatrixOperators(file)
        return mx_op.print(mx_op.matrix)
    except Error as e:
        return e

@app.get("/invert")
def  invert(file: Optional[str]='matrix.csv'):
    try:
        mx_op = MatrixOperators(file)
    except Error as e:
        return e

@app.get("/flatten")
def  flatten(file: Optional[str]='matrix.csv'):
    try:
        mx_op = MatrixOperators(file)
    except Error as e:
        return e


@app.get("/sum")
def  sum(file: Optional[str]='matrix.csv'):
    try:
        mx_op = MatrixOperators(file)
    except Error as e:
        return e


@app.get("/multiply")
def  multiply(file: Optional[str]='matrix.csv'):
    mx_op = MatrixOperators(file)
    try:
        mx_op = MatrixOperators(file)
    except Error as e:
        return e


@app.get("/")
def  presentation():
   return {
       "name": "Jose de Jesus Herrera Ledon",
       "email": "jesushledon@gmail.com"
   } 
