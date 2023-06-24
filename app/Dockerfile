FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src /code/
COPY src/db /code/src
COPY src/main.py main.py
CMD ["python", "main.py"]