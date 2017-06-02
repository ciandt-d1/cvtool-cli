FROM python:3-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apt-get update && \
    apt-get install -y git && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ARG setup_mode=install

RUN python setup.py $setup_mode

ENTRYPOINT ["kpick"]

CMD ["-h"]
