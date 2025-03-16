# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Expose the Flask port
EXPOSE 8000

# Set environment variables for Flask
ENV FLASK_APP=stream.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Run the Flask application
CMD ["flask", "run"]
