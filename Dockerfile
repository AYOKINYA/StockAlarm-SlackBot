FROM frolvlad/alpine-python3
COPY *.py /
COPY requirements.txt /
RUN pip3 install -r requirements.txt
CMD [ "python", "./slack.py" ]