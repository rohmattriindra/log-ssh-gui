FROM python:3.6.8-stretch

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
ENV FLASK_APP=webserver.py

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]