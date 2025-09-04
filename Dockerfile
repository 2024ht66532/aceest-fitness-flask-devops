FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
