FROM tensorflow/tensorflow:1.14.0-gpu-py3-jupyter
WORKDIR /app

RUN pip install tflearn
COPY . .

WORKDIR /app/code 
CMD ["python3", "main.py"]