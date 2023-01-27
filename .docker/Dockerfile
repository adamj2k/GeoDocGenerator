FROM python:3.9-slim
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["python3", "./geo_doc_generator/manage.py", "runserver", "0.0.0.0:8000"]
