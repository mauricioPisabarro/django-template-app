FROM python:3.7
EXPOSE 8000
WORKDIR /configbackend

ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN pip3 install poetry

RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip3 install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]