# Python slim  image
FROM python:3.8-slim-buster

# Set working dir in container
WORKDIR /app

# Run updates and install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt to working dir
COPY requirements.txt .

# Install packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy code to working dir
COPY . .

# start script
CMD ["python", "main.py"]