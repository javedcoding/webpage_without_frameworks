FROM python:alpine
ADD server.py code/
WORKDIR /code
EXPOSE 8080
RUN pip install gunicorn