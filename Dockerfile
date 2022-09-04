FROM python:3.8-alpine
ADD server.py /
RUN pip3 install flask
CMD ["python3", "server.py"]