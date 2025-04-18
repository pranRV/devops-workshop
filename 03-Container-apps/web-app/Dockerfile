# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything to /app
COPY . .

# Install Streamlit and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
