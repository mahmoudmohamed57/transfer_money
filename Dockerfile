# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libssl-dev \
    libffi-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    libpq-dev \
    git \
    iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /django_app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt /django_app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /django_app

# Create logs directory
RUN mkdir -p /django_app/logs && chown -R www-data:www-data /django_app/logs && chmod -R 755 /django_app/logs

# Expose the application port
EXPOSE 8000

# Run django_app development server with hot-reloading
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
