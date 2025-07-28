FROM python:3.10-slim

COPY package package
COPY models models
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install -r requirements.txt
RUN pip install -e .


# Local
# CMD uvicorn package_folder.api_file:app --host 0.0.0.0

# Deployed
CMD uvicorn package.api_file:app --host 0.0.0.0 --port $PORT
