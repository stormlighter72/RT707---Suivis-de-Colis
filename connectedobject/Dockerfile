FROM python:3.10.6
WORKDIR /ConnectedObject
COPY requirement.txt /ConnectedObject/
RUN pip install -r requirement.txt
COPY send_to_mqtt.py /ConnectedObject/
RUN python3 send_to_mqtt.py