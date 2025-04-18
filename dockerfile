FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app/

ENV PYTHONPATH=/app

COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
