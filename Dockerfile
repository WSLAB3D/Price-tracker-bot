FROM python:3.11-slim

# System packages for OpenCV & fonts
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY . .

# Set environment variable for production
ENV ULTRALYTICS_LOGGING=INFO

CMD ["python", "bot.py"]