FROM python:3.6

COPY src/ /service/

COPY config.yml /service/

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /service

EXPOSE 5672

CMD ["nameko", "run", "--config", "config.yml", "service"]

