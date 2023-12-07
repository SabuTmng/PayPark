# Build environment
FROM python:3.8-slim as builder
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN touch .env

# CMD to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]