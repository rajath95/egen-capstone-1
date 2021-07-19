# syntax=docker/dockerfile:1

FROM python:3.8

ADD cloud_sub.py /

COPY req.txt req.txt
RUN pip3 install -r req.txt

COPY . .

CMD [ "python3", "cloud_pub.py"]
