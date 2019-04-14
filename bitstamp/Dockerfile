FROM python:3.8.0a3-alpine3.9
MAINTAINER Semen Koretskiy <semenmsu@gmail.com>
RUN mkdir /app && mkdir /data && pip install websocket-client
WORKDIR /app
COPY src /app
ENV APP_ENV "dev"
CMD python3 dump_data.py


#RUN cd /tmp && git clone git://github.com/jedisct1/libsodium.git && cd libsodium && git checkout e2a30a && ./autogen.sh && ./configure && make check && make install && ldconfig
#RUN cd /tmp && git clone --depth 1 git://github.com/zeromq/libzmq.git && cd libzmq && ./autogen.sh && ./configure && make
# RUN cd /tmp/libzmq && make check
#RUN cd /tmp/libzmq && make install && ldconfig
#RUN rm /tmp/* -rf
#COPY ./artifacts /home/artifacts
#WORKDIR /home/artifacts
#RUN /home/artifacts/install.sh
#WORKDIR /home