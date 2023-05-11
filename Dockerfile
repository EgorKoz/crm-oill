FROM python:3.10-alpine

WORKDIR /usr/crm_oil

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./req .
RUN pip install -r req

COPY . .

ENTRYPOINT ["/usr/crm_oil/entrypoint.sh"]