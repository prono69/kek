FROM helowarld/bookworm:v2
ARG DEBIAN_FRONTEND=noninteractive
ARG USER=root
USER $USER

RUN apt-get update
COPY installer.sh ./installer.sh
RUN bash installer.sh
WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY start.sh ./start.sh
COPY app.py ./app.py
COPY config.py ./config.py

RUN pip3 install -r requirements.txt
RUN chmod +x /app/start.sh

EXPOSE 5000
ENTRYPOINT ["./start.sh"]
