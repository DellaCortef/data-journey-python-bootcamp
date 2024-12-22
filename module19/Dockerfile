FROM python:3.12

# Installing Poetry
RUN pip install poetry

# Copy the contents of the current directory to the container
COPY . /src

# Set working directory
WORKDIR /src

# Install project dependencies with Poetry
RUN poetry install

# Expose the port on which the application will be listening
EXPOSE 8501

# Set the entrypoint to run the Uvicorn server
ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501"]