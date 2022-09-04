# SensorData Back-End 



## Language
-python:3.8-alpine

## Tools
-Flask
-Docker


## Instructions
1.'docker build -t exercise:latest .'
2.'docker run --rm -it -p 8080:8080 exercise:latest'

Result:
Server accessible at `localhost:8080`. 
Routes:
    GET /healthz
    POST /data
    GET /statistics
    DELETE /statistics



server.py
post_data(): handles POST and input errors



## Testing
    1. 'pip install pytest'
    2.In tests directory, use 'pytest'



