FROM ubuntu
COPY . /
ENV DISPLAY=:0
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN yes | apt-get install python3
RUN yes | apt-get install python3-tk
CMD python3 gui.py
