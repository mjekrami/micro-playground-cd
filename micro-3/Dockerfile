FROM python:3.11

WORKDIR /app 
COPY requirements.txt /app
COPY main.py /app

# Install Dependecies
RUN pip3 install -r requirements.txt 

CMD ["python3","main.py"]
