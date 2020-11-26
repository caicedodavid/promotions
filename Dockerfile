FROM python:3.9.0-alpine3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
ENV FLASK_ENV development
ENV FLASK_APP /app/src/app.py
ENV PYTHONUNBUFFERED 1
ENV APP_CONFIG project.configs.DevelopmentConfig
ENV MONGODB_HOST mongodb://productListUser:productListPassword@mongo:27017/promotions?authSource=admin
ENV WAIT_DB 1

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

WORKDIR /app/src

COPY . /app/

RUN chmod +x /app/entrypoint.sh

EXPOSE $PORT

CMD ["/app/entrypoint.sh"]