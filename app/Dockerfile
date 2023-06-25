FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y x11-apps && rm -rf /var/lib/apt/lists/*
COPY src/ .
CMD ["python", "./main.py"]