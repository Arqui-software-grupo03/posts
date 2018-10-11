FROM node:7
FROM python:latest
ENV LANG C.UTF-8

RUN mkdir /appPosts

RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev

WORKDIR /appPosts

COPY . /appPosts
RUN pip install -r /appPosts/requirements.txt

EXPOSE 8100