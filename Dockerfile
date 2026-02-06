FROM python:3.13-slim

WORKDIR /jv

# copy only requirements first
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# now copy rest of code
COPY . .

EXPOSE 5000

CMD ["python", "jv.py"]
