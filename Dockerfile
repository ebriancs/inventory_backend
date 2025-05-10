# Step 1: Use the official Python image as the base
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy requirements.txt to the container
COPY requirements.txt .

# Step 4: Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project files to the container
COPY . .

# Step 6: Expose the port that Django will run on (usually 8000)
EXPOSE 8000

# Step 7: Run the Django application when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
