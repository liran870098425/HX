from python:3.12.12-alpine
run mkdir /app
workdir /app
add . /app/
run pip install -r requirements.txt
run python run.py