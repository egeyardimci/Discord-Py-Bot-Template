# Use a Python 3.8 runtime as a base image
FROM python:3.10.11-alpine3.17
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY . .
RUN sh setup.sh

CMD ["python", "Bot.py"]