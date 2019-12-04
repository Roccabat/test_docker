FROM ubuntu

COPY ./LeftRotation.py /usr/app/LeftRotation.py
COPY ./main.py /usr/app/main.py

RUN apt-get update

RUN apt-get install python3.6 -y

RUN apt-get install python3-pip -y

RUN pip3 install numpy

ENTRYPOINT ["python3.6", "/usr/app/main.py"]

CMD ["abcde","3"]