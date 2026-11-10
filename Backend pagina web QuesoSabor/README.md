FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY common /app/common
COPY services /app/services
COPY seed /app/seed
COPY scripts /app/scripts
HEALTHCHECK --interval=15s --timeout=5s --retries=3 CMD python -c "import urllib.request,os; urllib.request.urlopen('http://127.0.0.1:'+os.environ['SERVICE_PORT']+'/health',timeout=2)"
