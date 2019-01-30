FROM ubuntu:16.04
RUN dpkg --add-architecture i386
RUN useradd -ms /bin/bash compfest

RUN apt-get update -y && apt-get upgrade -y && apt-get install socat openssh-server -y

# COPY id_rsa.pub /tmp/
# RUN mkdir -p /home/compfest/.ssh
# RUN mv /tmp/id_rsa.pub /home/compfest/.ssh/authorized_keys
# RUN chown -R compfest:compfest /home/compfest/.ssh
# RUN chmod 644 /home/compfest/.ssh/authorized_keys



COPY flag.txt manage.py db.sqlite3 docker-compose.yml /opt/
COPY pwn_docs /opt/pwn_docs
COPY show_docs /opt/show_docs
WORKDIR /opt
RUN chown compfest:compfest -R /opt/

ENV TERM linux

RUN apt-get update -y
RUN apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential -y
RUN pip install --upgrade pip
RUN pip install pyelftools==0.24
RUN pip install --upgrade pwntools

RUN pip install django==1.11

CMD service ssh start & python manage.py runserver 0.0.0.0:8000 --insecure;
