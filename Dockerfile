# Use an official Python image as the base image (Python 3.10)
FROM python:3.10  

# Set the working directory inside the container to /app
WORKDIR /app  

# Copy only the requirements file first (better for caching dependencies)
COPY requirements.txt .  

# Update package lists and install dependencies from requirements.txt
RUN apt-get update && pip install --no-cache-dir -r requirements.txt  
# `apt-get update` updates package lists (needed if you install system packages)
# `pip install --no-cache-dir` prevents caching to keep the image size small

# Copy the rest of the application files into the container
COPY . .  

# Expose port 8000 so the container can accept traffic on this port
EXPOSE 8000  

# Default command to run the Flask application
CMD ["python", "app.py"]  
# Using CMD instead of RUN because CMD executes when the container starts

