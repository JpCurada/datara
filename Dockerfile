FROM python:3.12-alpine AS builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

WORKDIR /app

RUN python -m venv /venv
COPY src/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PATH="/assistant:/venv/bin:$PATH"

RUN apk add postgresql16 postgresql16-contrib postgresql16-openrc

COPY src/ /app
COPY staticfiles/ /staticfiles
COPY --from=builder /venv /venv
COPY src/requirements.txt /app/.cache
