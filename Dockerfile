# Dockerfile

# Base image
FROM python:3.9.7

# Set the working directory
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y gettext vim

ENV PYTHONUNBUFFERED 1
ENV PYTHONOPTIMIZE 1
# Expose port 8000 for the Django server
EXPOSE 8000

# Start the Django server
ENTRYPOINT ["/app/entrypoint.sh"]