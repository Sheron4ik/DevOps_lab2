FROM python:3.10-slim
WORKDIR bot
COPY test.py test.py
ENTRYPOINT ["python", "test.py"]
