FROM python:3.7

WORKDIR /app

COPY requirements.txt /tmp/
RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

ENV PYTHONPATH=/app/src

CMD ["uvicorn", "main:app", "--reload"]
