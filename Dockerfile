# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=api/app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]


# To build 'docker build -t book-fetcher-image .'
# To build 'docker buildx build --platform linux/amd64 -t book-fetcher-image .'

# To run 'docker run -p 4999:5000 book-fetcher-image'