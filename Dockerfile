FROM python:3.7.5-slim
LABEL maintainer="Kevin Mathew <kevinam99@gmail.com>"


RUN mkdir app
COPY ./ ./app
WORKDIR ./app

RUN pip3 install -r requirements.txt

CMD flask run