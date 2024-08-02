FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1


WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY ./.mikrus/scripts /scripts

ENV PATH="/usr/local/bin:/scripts:$PATH"
RUN sed -i 's/\r$//' /scripts/app/run.sh \
    && chmod -R +x /scripts \
    && mkdir static/ \
    && chown -R nobody:nogroup /app/static/
USER nobody
