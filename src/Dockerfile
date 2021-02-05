# base image
FROM python:3.7

# set working directory
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN python -m pip install -r requirements.txt

# add app
COPY . /usr/src/app
