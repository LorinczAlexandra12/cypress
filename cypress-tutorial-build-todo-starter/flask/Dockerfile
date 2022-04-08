FROM python:3.9-slim
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY ./results /code/results
RUN pip install -r requirements.txt
COPY . /code/
CMD python run.py