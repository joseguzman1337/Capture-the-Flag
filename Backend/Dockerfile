# Use the latest slim Python image as the base image
FROM python:slim@sha256:66eca1a0be6b978565f2d6e7f89daf4e1f1891380a2278feecf003d1537c7630

# Set the environment variable to not buffer Python outputs
ENV PYTHONUNBUFFERED 1

# Set an argument for the app directory
ARG APP=/app
WORKDIR $APP
VOLUME $APP

# Install system dependencies and clean up apt cache
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        gcc \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Django server
CMD ["./manage.py", "runserver", "0:3000"]

# Expose the Django server port
EXPOSE 3000
