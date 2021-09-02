FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y

RUN git clone https://github.com/PATRICIAGANG/ytdl

RUN pip3 install --upgrade pip
RUN pip3 install -u -r requirements.txt

CMD python3 -m main.py
