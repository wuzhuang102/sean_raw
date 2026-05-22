---
created: "2026-05-22"
sources:
  - "https://docs.docker.com/engine/containers/run/"
  - "https://docs.docker.com/build/concepts/dockerfile/"
  - "https://docs.docker.com/reference/builder"
  - "https://docs.docker.com/reference/cli/docker/image/"
  - "https://docs.docker.com/reference/cli/docker/image/pull/"
  - "https://docs.docker.com/engine/reference/commandline/tag/"
  - "https://docs.docker.com/engine/storage/volumes/"
  - "https://docs.docker.com/storage/"
  - "https://docs.docker.com/reference/cli/docker/compose/"
  - "https://docs.docker.com/reference/"
---

This raw source note captures the official Docker documentation pages used to compile the Docker basic syntax topic.

## Source Notes

- Docker run: `docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]` starts a container from an image, with flags that can override image defaults such as command, port exposure, environment variables, user, healthcheck, and working directory.
- Dockerfile overview and reference: Docker builds images from Dockerfile instructions. Common instructions include `FROM`, `RUN`, `WORKDIR`, `COPY`, `CMD`, `ENTRYPOINT`, `ENV`, `EXPOSE`, `ARG`, `USER`, `VOLUME`, and `HEALTHCHECK`.
- Docker image CLI: `docker image` groups image operations including build, list, inspect, pull, push, remove, prune, save, load, and tag.
- Docker pull/tag: image references use `[HOST[:PORT]/]NAMESPACE/REPOSITORY[:TAG]`; when omitted, Docker defaults to Docker Hub, the `library` namespace, and the `latest` tag.
- Docker storage and volumes: data in a container writable layer does not persist after the container is removed. Volumes are Docker-managed persistent storage. Bind mounts map host paths directly into containers.
- Docker Compose CLI: Compose is the CLI for building and running multi-container applications from Compose files.

## URLs

- Docker run containers: https://docs.docker.com/engine/containers/run/
- Dockerfile overview: https://docs.docker.com/build/concepts/dockerfile/
- Dockerfile reference: https://docs.docker.com/reference/builder
- Docker image CLI: https://docs.docker.com/reference/cli/docker/image/
- Docker image pull: https://docs.docker.com/reference/cli/docker/image/pull/
- Docker image tag: https://docs.docker.com/engine/reference/commandline/tag/
- Docker volumes: https://docs.docker.com/engine/storage/volumes/
- Docker storage overview: https://docs.docker.com/storage/
- Docker Compose CLI: https://docs.docker.com/reference/cli/docker/compose/
- Docker reference overview: https://docs.docker.com/reference/
