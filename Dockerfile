FROM python:3.10.5

# Install app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Migrate
RUN python manage.py migrate

# Run app
EXPOSE 5000
CMD ["python", "manage.py", "runserver"]
