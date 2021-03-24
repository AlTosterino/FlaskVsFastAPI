FROM python:3.9-slim-buster
COPY deployment/requirements/prod.txt prod.txt
RUN pip install -r prod.txt
WORKDIR /app