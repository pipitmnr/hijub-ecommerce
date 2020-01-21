FROM python:3.6.5
MAINTAINER Your Name "syafitri@alterra.id"
RUN mkdir -p /demo1
COPY . /demo1
RUN pip install -r /demo1/requirement.txt
WORKDIR /demo1
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
