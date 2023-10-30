FROM python:alpine

WORKDIR /app

COPY exporter.py /app

ENV PORT=${PORT_ONCALL}

EXPOSE ${PORT}

RUN pip install requests environs prometheus_client

CMD ["python", "/app/exporter.py"]