# syntax=docker/dockerfile:1

FROM python:3.9-alpine
WORKDIR /sigmac-service

ENV FLASK_APP=microservices/sigmac-service/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

RUN apk add --no-cache gcc musl-dev linux-headers && apk add git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ["microservices/sigmacService/.", "microservices/sigmacService/"]

RUN mkdir -p microservices/sigmacService/sigma
RUN cd microservices/sigmacService/sigma
RUN git clone https://github.com/SigmaHQ/sigma.git

WORKDIR /sigmac-service
CMD [ "python", "microservices/sigmacService/app.py" ]