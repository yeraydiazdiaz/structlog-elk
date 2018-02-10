FROM python:3.6.3-slim
RUN apt-get update && apt-get install -y build-essential python-dev
RUN mkdir /opt/app
WORKDIR /opt/app
RUN pip install -U pip setuptools wheel
RUN python3 -m venv /opt/app
ENV PATH="/opt/app/bin:${PATH}"
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /opt/app