FROM python:3.11

WORKDIR /dockerDir

COPY ./requirements.txt /dockerDir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /dockerDir/requirements.txt

COPY ./app /dockerDir/app

EXPOSE 8000

WORKDIR /dockerDir/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
