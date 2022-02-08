# League Backend Challenge
### Python FastAPI

## Instructions

Given an uploaded csv file
```
1,2,3
4,5,6
7,8,9
```

1. Echo (given)
    - Return the matrix as a string in matrix format.
    
    ```
    // Expected output
    1,2,3
    4,5,6
    7,8,9
    ``` 
2. Invert
    - Return the matrix as a string in matrix format where the columns and rows are inverted
    ```
    // Expected output
    1,4,7
    2,5,8
    3,6,9
    ``` 
3. Flatten
    - Return the matrix as a 1 line string, with values separated by commas.
    ```
    // Expected output
    1,2,3,4,5,6,7,8,9
    ``` 
4. Sum
    - Return the sum of the integers in the matrix
    ```
    // Expected output
    45
    ``` 
5. Multiply
    - Return the product of the integers in the matrix
    ```
    // Expected output
    362880
    ``` 

The input file to these functions is a matrix, of any dimension where the number of rows are equal to the number of columns (square). Each value is an integer, and there is no header row. matrix.csv is example valid input.  

Send request
```
curl -F 'file=@/app/matrix.csv' "localhost:8080/echo"
```

## What we're looking for

- [x] The solution runs 
- [x] The solution performs all cases correctly
- [x] The code is easy to read
- [x] The code is reasonably documented
- [x] The code is tested
- [x] The code is robust and handles invalid input and provides helpful error messages

## How to run it

### Locally 
    1- Create a virtual environment 
    2.- Activate your virtual environment
    3.-Install requirements as 
    ```pip install -r requirements_dev.txt```
    4.- Run the application 
    ```uvicorn app.main:app ```
    This application run at 127.0.0.1:8000/

### Docker 
This project uses docker compose, if you have docker installed use 

```docker-compose -f docker_compose.yml build```

and 

```docker-compose -f docker_compose.yml up``` 

### Documentation
Once is runnig tou can look into 

local: 127.0.0.1:8000/docs 

docker: 127.0.0.1:80/docs