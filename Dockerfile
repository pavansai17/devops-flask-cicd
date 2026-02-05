# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 5001
EXPOSE 5001

# Set environment variables
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]