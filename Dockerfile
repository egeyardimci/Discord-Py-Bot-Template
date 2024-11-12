# Python 3 base image
FROM python:3.10.11-alpine3.17
WORKDIR /app

# Set an environment variable for the bot key
ENV TOKEN="YOUR_BOT_TOKEN"

# Disable Python output buffering
ENV PYTHONUNBUFFERED=1

# Install any needed packages specified in requirements.txt
COPY . .
RUN sh setup.sh

# Run the bot
CMD ["python", "bot.py"]