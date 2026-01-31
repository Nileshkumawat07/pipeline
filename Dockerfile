FROM python:3.13.7
COPY ./ jv
WORKDIR / jv
ENTRYPOINT ["python"]
CMD ["jv.py"]
