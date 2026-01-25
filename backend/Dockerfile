# ---------- Stage 1: Build dependencies ----------
FROM python:3.10 AS builder

WORKDIR /app

# Install system dependencies (needed for psycopg2)
RUN apt-get update && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    django \
    django-cors-headers \
    psycopg2-binary

# ---------- Stage 2: Runtime ----------
FROM python:3.10

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /usr/local /usr/local

# Copy backend source code
COPY . .

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=True

USER appuser

EXPOSE 8000

# Same as: python manage.py runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
