# Use the official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Set environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=core.settings

# Command to run the Django development server
CMD ["python", "core/manage.py", "runserver", "0.0.0.0:8000"]