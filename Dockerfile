FROM python:3.8

RUN mkdir /usr/src/app/
#RUN mkdir /usr/src/resultados/images/
WORKDIR /usr/src/app/

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY ./code2 /usr/src/app/

#RUN apk update && apk add --no-cache python3-dev gcc libc-dev musl-dev linux-headers tesseract-ocr tesseract-ocr-data-spa
#RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN pip install --upgrade pip

CMD ["uvicorn", "app2:app", "--host", "0.0.0.0", "--port", "5050"]
#CMD uvicorn app2:app --host 0.0.0.0 --port 5050

#ENTRYPOINT ["uvicorn", "app2:app", "--host", "0.0.0.0", "--port", "5050"]