FROM python:3.11.4

ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app

# Required to install mysqlclient client and other dependencies
RUN apt-get update \
  && apt-get install -y libpq-dev gcc

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev --verbose --skip-lock

# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container
EXPOSE 8000