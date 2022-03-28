FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY ./entrypoint.sh /app/entrypoint.sh

COPY . /app/


ENTRYPOINT ["/app/entrypoint.sh"]