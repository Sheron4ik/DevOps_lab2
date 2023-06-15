FROM python
WORKDIR bot
COPY test.py test.py
ENTRYPOINT ["python", "test.py"]
