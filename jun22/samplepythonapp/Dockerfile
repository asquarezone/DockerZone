FROM python:3.9-alpine
LABEL author "khaja"
RUN adduser -D qtuser && mkdir /home/qtuser/sample
USER qtuser
WORKDIR /home/qtuser/sample
ADD . /home/qtuser/sample/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]