# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies (if a requirements file exists)
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the root of the repo
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["python", "stream.py"]
