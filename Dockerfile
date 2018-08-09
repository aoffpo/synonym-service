FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# COPY requirements.docker.txt /app/requirements.txt
WORKDIR /app
RUN pip freeze > /app/requirements.txt 
RUN pip install -r /app/requirements.txt 
RUN pip install flask \
    && pip install nltk

#certs fro downloader
RUN apk add ca-certificates  
RUN python -m nltk.downloader wordnet

COPY synapp.py /app

EXPOSE  8000
CMD ["python", "/app/synapp.py", "-p 8000"]