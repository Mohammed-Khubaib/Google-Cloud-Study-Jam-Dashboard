# Use the official Python image as the base image
FROM python:3.10.13-slim-bullseye


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
