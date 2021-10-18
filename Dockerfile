FROM python:3.8-alpine
WORKDIR /code
COPY requirements*.txt ./
RUN pip install -r requirements_test.txt -r requirements.txt
CMD sleep 3600000
