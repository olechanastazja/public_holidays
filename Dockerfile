FROM python:3.7.2

RUN mkdir /code
WORKDIR /code/public_holidays/

COPY ./requirements.txt /code/

RUN apt-get update

RUN pip install -r /code/requirements.txt

COPY ./entrypoint.sh /code/entrypoint.sh

COPY . /code/

RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["sh", "/code/entrypoint.sh"]