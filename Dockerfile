# Use a lightweight official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project
COPY . .

# Create input and output directories inside the container
RUN mkdir -p /app/input /app/output

# Default command to run the main script
CMD ["python", "app/main.py"]
