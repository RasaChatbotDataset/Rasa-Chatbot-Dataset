# Python version
FROM python:3.10.11-slim

# Work directory
WORKDIR /app

# Copy files
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Interactive terminal
CMD ["bash"]