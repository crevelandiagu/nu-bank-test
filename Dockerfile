FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN pytest --cov=. -v -s --cov-fail-under=70 --cov-report=html

CMD ["python","main.py"]
