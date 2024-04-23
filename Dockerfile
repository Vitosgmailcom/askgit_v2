FROM python:3.12.0a4-alpine3.17

RUN mkdir /automation

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

WORKDIR /automation

COPY ./ /automation
COPY ./requirements.txt /automation

RUN pip3 install -r requirements.txt # && playwright install && sudo apt-get install libevent-2.1-7  (install browsers for playwright)

