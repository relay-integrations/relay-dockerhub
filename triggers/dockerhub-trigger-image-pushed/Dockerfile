FROM relaysh/core:latest-python
RUN pip --no-cache-dir install quart
COPY "./handler.py" "/handler.py"
ENTRYPOINT []
CMD ["python3", "/handler.py"]

LABEL "org.opencontainers.image.title"="Docker Hub image pushed"
LABEL "org.opencontainers.image.description"="This trigger fires when an image is pushed to the Docker Hub registry."
LABEL "com.puppet.nebula.sdk.version"="v1"
