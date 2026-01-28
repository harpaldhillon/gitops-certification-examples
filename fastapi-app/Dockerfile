FROM python:3.10.19-slim
WORKDIR /app
COPY main.py requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
