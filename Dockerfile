FROM python:3.7.0-stretch

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#RUN apt-get update && apt-get upgrade
#RUN apt-get install --force-yes -y nginx
#RUN /etc/init.d/nginx start

COPY run.py /app/

EXPOSE 5000
CMD [ "python", "./run.py"]

