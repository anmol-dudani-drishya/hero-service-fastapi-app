FROM amazon/aws-lambda-python:3.8
COPY ./code ./code
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
CMD ["code.main.handler"]