# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies (only if requirements.txt exists)
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements file found"

# Copy the remaining application files
COPY . .

# Ensure the stationlist directory exists
RUN mkdir -p /
