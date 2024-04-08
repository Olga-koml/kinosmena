FROM python:3.10.6-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r /app/requirements.txt --no-cache-dir
COPY kinosmena_backend/ .
# CMD ["python", "manage.py", "runserver", "0.0.0.0:6080" ]
CMD ["gunicorn", "kinosmena_backend.wsgi:application", "--bind", "0.0.0.0:6080", "--log-level", "DEBUG"]