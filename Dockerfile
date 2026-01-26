
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target=/app/deps

COPY app.py .

COPY index.html .

FROM gcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /app/deps /app/deps

COPY --from=builder /app/app.py /app/app.py

COPY --from=builder /app/index.html /app/index.html

ENV PYTHONPATH=/app/deps

EXPOSE "5000"

CMD ["app.py"]
