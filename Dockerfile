FROM python:3.13.7
COPY . .
WORKDIR / jv
ENTRYPOINT ["python"]
CMD ["jv.py"]