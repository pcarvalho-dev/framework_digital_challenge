FROM python:3.7-alpine

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && apk add musl-dev openssl-dev libffi-dev gcc tzdata freetype-dev fribidi-dev harfbuzz-dev jpeg-dev lcms2-dev openjpeg-dev tcl-dev tiff-dev tk-dev zlib-dev \
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" >  /etc/timezone \
    && apk del tzdata

WORKDIR /flask-api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY docker-entrypoint.py /docker-entrypoint.py
RUN chmod +x /docker-entrypoint.py
COPY . .
EXPOSE 5000

CMD ["python", "/docker-entrypoint.py" ]
