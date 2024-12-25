# Use the latest slim Python image as the base image
FROM python:slim@sha256:d4ea1ac67b80976f46d5f9a2051bdbc963d16b766692472c65e478cdf97b8064

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
