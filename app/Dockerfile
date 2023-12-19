# Use Python 3.10-slim-buster for the Docker image
FROM python:3.10-slim-buster
# application code placed in the working directory to /app
WORKDIR /app
# Copies content of current directory onto 'app' directory 
COPY . /app
# Installs the requirements in the requirements.txt file
RUN pip install -r requirements.txt 
# use port 5000
EXPOSE 5000
# command to run app.py using python
CMD ["python", "app.py"]


