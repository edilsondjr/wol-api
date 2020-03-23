FROM python:3.8-slim-buster

COPY ./ /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt && python create_db.py
EXPOSE 5000
CMD python ./wol.py