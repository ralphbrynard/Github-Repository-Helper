# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install git and other required packages
RUN apt-get update &&     apt-get install -y git &&     apt-get clean &&     rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the textual app (if needed)
EXPOSE 5000

# Set the entrypoint to run the script
ENTRYPOINT ["python", "repository_helper.py"]
