FROM python:3

COPY ./requirements.txt .

RUN pip install -r /requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "src/__init__.py"]