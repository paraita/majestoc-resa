FROM python:3
LABEL maintainer=paraita.wohler@gmail.com

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "sh", "-c", "./starter.py"]
