FROM python:3.7-alpine
RUN pip install flask
COPY server.py /server.py
CMD python /server.py
