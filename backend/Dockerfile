FROM python:3.12-slim
WORKDIR /app

RUN groupadd -r appgroup && useradd -r -g appgroup -s /bin/false appuser

COPY app.py .

RUN chown -R appuser:appgroup /app
USER appuser

ARG APP_PORT=8080
ENV PORT=$APP_PORT
EXPOSE $PORT
HEALTHCHECK --start-period=5s \
            --interval=1m \
            --timeout=5s \
            --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:$PORT/health')" || exit 1
CMD ["python", "app.py"]
