FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cach-dir -r requierments.txt
EXPOSE 8000
COPY . .
CMD ["python3", "manage.py", "runserver"]
