#Base Image (Python)
FROM python:3.12

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# # Command to run the app
# CMD ["python", "app.py"]

