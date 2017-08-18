FROM python:3
ADD . /program
RUN pip install -U pip
RUN pip install requests

