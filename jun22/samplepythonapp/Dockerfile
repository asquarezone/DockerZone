FROM python:3.9
LABEL author "khaja"
ADD . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]