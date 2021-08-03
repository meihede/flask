FROM python:3.6
ADD . /flask
WORKDIR /flask
RUN pip install -r requirements.txt
