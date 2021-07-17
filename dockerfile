FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./api ./api

COPY ./data ./data

EXPOSE 80

WORKDIR ./api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
