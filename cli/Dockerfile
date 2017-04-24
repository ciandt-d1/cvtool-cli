FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements_docker.txt

RUN python setup.py install

ENTRYPOINT ["kpick"]

CMD ["-h"]
