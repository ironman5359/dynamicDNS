FROM python:3.10

ARG DNS_API_KEY
ARG DNS_API_SECRET

ENV DNS_API_KEY=$DNS_API_KEY
ENV DNS_API_SECRET=$DNS_API_SECRET

COPY . /app

# Set the working directory \
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3","main.py"]