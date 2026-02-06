# 1️⃣ Use lightweight Python image (FAST)
FROM python:3.13-slim

# 2️⃣ Set working directory inside container
WORKDIR /jv

# 3️⃣ Copy only dependencies first (enables caching)
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy application code
COPY . .

# 6️⃣ Expose Flask port
EXPOSE 5000

# 7️⃣ Run the Flask app
CMD ["python", "jv.py"]
