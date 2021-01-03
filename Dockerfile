FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR ./lux/
COPY requirements.txt /lux/
RUN pip install -r requirements.txt
COPY . /lux/
