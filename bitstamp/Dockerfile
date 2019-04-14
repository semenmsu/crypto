FROM ubuntu:16.04
MAINTAINER Semen Koretskiy <semenmsu@gmail.com>
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
EXPOSE 5555
CMD node index.js

RUN apt-get update && apt-get install -y git build-essential libtool autoconf automake pkg-config unzip libkrb5-dev
RUN cd /tmp && git clone git://github.com/jedisct1/libsodium.git && cd libsodium && git checkout e2a30a && ./autogen.sh && ./configure && make check && make install && ldconfig
RUN cd /tmp && git clone --depth 1 git://github.com/zeromq/libzmq.git && cd libzmq && ./autogen.sh && ./configure && make
# RUN cd /tmp/libzmq && make check
RUN cd /tmp/libzmq && make install && ldconfig
RUN rm /tmp/* -rf
COPY ./artifacts /home/artifacts
WORKDIR /home/artifacts
RUN /home/artifacts/install.sh
WORKDIR /home