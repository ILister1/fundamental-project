FROM python:3.9

WORKDIR /fundamental-project

COPY ./requirements.txt .

EXPOSE 5000

RUN pip3 install -r requirements.txt

COPY . .

ENV secret=${SECRET}


ENTRYPOINT ["python", "app.py"]

