FROM python:3.11-slim

WORKDIR /app
COPY app/server.py .
RUN pip install requests

EXPOSE 8080
CMD ["python", "server.py"]
