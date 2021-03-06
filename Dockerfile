FROM python:3
ENV  PYTHONNUMBERBUFFERED=1
WORKDIR /app
COPY requirement.txt requirement.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirement.txt
COPY . /app
EXPOSE 8000

