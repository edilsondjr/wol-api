FROM python:3.8-slim-buster

## Setting Working Dir
WORKDIR /app

## Copy Pipenv files only
COPY Pipfile ./

RUN pip install --no-cache-dir pipenv && \
    pipenv lock && \
    pipenv install --system --deploy --clear


COPY ./ /app
RUN touch ./wolapi.log && \
    chmod 755 ./wolapi.log && \
    ln -sf /proc/1/fd/1 ./wolapi.log

## Create minimal SqLite DB
RUN python create_db.py

## Expose port and run the application
EXPOSE 5000
CMD ["python", "wol.py"]