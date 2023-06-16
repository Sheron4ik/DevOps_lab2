FROM python:3.10-slim
WORKDIR bot
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY todosher.py todosher.py
ENTRYPOINT ["python", "todosher.py"]
