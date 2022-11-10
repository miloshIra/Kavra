FROM python:3.8.3-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /kavsite

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /kavsite /kavsite/

CMD ["cd", "kavsite"]
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



