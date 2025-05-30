FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your application code
COPY ./app /app/app

# Copy your requirements.txt
COPY requirements.txt .

# Set PYTHONPATH so "app" package is discoverable
ENV PYTHONPATH=/app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
