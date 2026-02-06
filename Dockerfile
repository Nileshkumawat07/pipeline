FROM python:3.13.7

WORKDIR /jv
COPY . .

CMD ["python", "jv.py"]
