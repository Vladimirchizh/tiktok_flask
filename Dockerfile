FROM python:3.7

COPY requirements.txt ./requirements.txt
COPY server.py ./server.py

RUN pip install -r requirements.txt
CMD ["python", "./server.py"]
