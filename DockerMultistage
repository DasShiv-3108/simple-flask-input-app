
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target=/app/deps

COPY app.py .

FROM gcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /app/deps /app/deps

COPY --from=builder /app/app.py /app/app.py

ENV PYTHONPATH=/app/deps

CMD ["app.py"]
