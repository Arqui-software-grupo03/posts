FROM node:7
FROM python:latest
ENV LANG C.UTF-8

RUN mkdir /appPosts

RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev

# ADD requirements.txt /app/requirements.txt

WORKDIR /appPosts

COPY . /appPosts
RUN pip install -r /appPosts/requirements.txt

# RUN apt-get -y update && apt-get -y autoremove
EXPOSE 8000
# CMD gunicorn -b :8000 app.wsgi


# FROM node:7
# WORKDIR /app2
# COPY package.json /app2
# RUN npm install
# COPY . /app2
# CMD npm start
# EXPOSE 3000