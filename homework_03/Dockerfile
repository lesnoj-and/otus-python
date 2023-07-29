FROM ubuntu:latest
ARG CACHEBUST=1
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install uvicorn fastapi

COPY main.py /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

