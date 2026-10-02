FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt
COPY main-script.py . 
CMD ["python", "main-script.py"]
RUN apt update -y && apt upgrade -y && apt install -y iproute2 net-tools curl 
 





