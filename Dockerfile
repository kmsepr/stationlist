# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies (only if needed)
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Ensure stationlist directory exists and copy files
RUN mkdir -p stationlist
COPY stationlist/ stationlist/

# Copy the application files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["python", "stream.py"]
