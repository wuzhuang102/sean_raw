---
title: "Docker 常用基础语法"
type: "topic"
status: "active"
created: "2026-05-22"
updated: "2026-05-22"
sources:
  - "../../raw/docker-basic-syntax-sources.md"
tags: ["docker", "container", "image", "compose", "infra"]
---

# Docker 常用基础语法

Docker 的日常使用可以按生命周期理解：拉取或构建镜像，基于镜像运行容器，查看和进入容器，管理端口、环境变量、存储、网络，最后清理资源。官方 CLI 中很多命令同时存在长写法和短写法，例如 `docker image pull` 与 `docker pull` 等价。

## 核心概念

- 镜像 image：只读模板，包含应用、运行时、依赖和默认启动配置。
- 容器 container：镜像运行后的进程实例，有自己的文件系统、网络和进程空间。
- Dockerfile：描述如何构建镜像的文本文件。
- volume：Docker 管理的持久化数据卷，适合数据库和长期数据。
- bind mount：把宿主机路径直接挂进容器，适合开发时同步代码。
- Compose：用 `compose.yaml` 描述多容器应用，并用 `docker compose` 统一启动、停止和查看。

## 镜像命令

```bash
docker pull nginx:latest
docker images
docker image ls
docker image inspect nginx:latest
docker tag my-app:local registry.example.com/team/my-app:1.0.0
docker push registry.example.com/team/my-app:1.0.0
docker rmi nginx:latest
docker image prune
```

镜像引用格式通常是：

```text
[HOST[:PORT]/]NAMESPACE/REPOSITORY[:TAG]
```

例如 `alpine` 会默认解析为 Docker Hub 的 `library/alpine:latest`。生产环境应尽量显式写 tag，避免依赖可变的 `latest`。

## 运行容器

通用形式：

```bash
docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```

常用示例：

```bash
docker run nginx:latest
docker run --name web nginx:latest
docker run -d --name web nginx:latest
docker run --rm alpine:latest echo hello
docker run -it ubuntu:24.04 bash
docker run -p 8080:80 nginx:latest
docker run -e NODE_ENV=production my-node-app:1.0.0
docker run --env-file .env my-app:1.0.0
docker run -w /app my-image:latest npm test
docker run --restart unless-stopped redis:latest
```

常用参数：

- `--name <name>`：指定容器名。
- `-d`：后台运行。
- `--rm`：容器退出后自动删除，适合一次性命令。
- `-it`：交互式终端，常用于 shell。
- `-p <host_port>:<container_port>`：端口映射。
- `-e KEY=value`：注入环境变量。
- `--env-file <file>`：从文件加载环境变量。
- `-v <source>:<target>`：挂载 volume 或宿主机路径。
- `--mount type=volume,source=<name>,target=<path>`：更明确的挂载语法。
- `--network <network>`：加入指定网络。
- `--restart <policy>`：设置重启策略，如 `no`、`on-failure[:n]`、`always`、`unless-stopped`。

## 查看和操作容器

```bash
docker ps
docker ps -a
docker logs web
docker logs -f --tail 100 web
docker exec -it web sh
docker stop web
docker start web
docker restart web
docker rm web
docker rm -f web
docker inspect web
docker stats
```

常见判断：

- `docker ps` 只看运行中的容器。
- `docker ps -a` 包括已退出容器。
- `docker logs -f` 追踪日志。
- `docker exec -it <container> sh` 进入正在运行的容器；基础镜像不一定有 `bash`。
- 删除运行中的容器需要先 `docker stop`，或用 `docker rm -f` 强制删除。

## Dockerfile 基础

一个常见 Dockerfile：

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "server.js"]
```

常用指令：

- `FROM <image>`：指定基础镜像，也会开始一个新的构建阶段。
- `WORKDIR <dir>`：设置后续指令的工作目录。
- `COPY <src> <dest>`：复制构建上下文中的文件到镜像。
- `RUN <command>`：在构建阶段执行命令并生成新层。
- `ENV KEY=value`：设置运行时环境变量。
- `ARG KEY=value`：设置构建时变量。
- `EXPOSE <port>`：声明容器内应用监听端口，不等于自动发布到宿主机。
- `CMD [...]`：容器默认命令，一个 Dockerfile 只有最后一个 `CMD` 生效。
- `ENTRYPOINT [...]`：默认可执行入口，常和 `CMD` 配合。
- `USER <user>`：切换运行用户，减少以 root 运行的风险。
- `HEALTHCHECK ...`：声明健康检查。

构建镜像：

```bash
docker build -t my-app:1.0.0 .
docker build -f Dockerfile.prod -t my-app:prod .
docker build --build-arg NODE_ENV=production -t my-app:prod .
```

`.` 是 build context，Dockerfile 中的 `COPY` 只能访问 context 内的文件。应使用 `.dockerignore` 排除 `node_modules`、日志、临时文件、密钥和本地构建产物。

## 存储挂载

创建和管理 volume：

```bash
docker volume create app-data
docker volume ls
docker volume inspect app-data
docker volume rm app-data
```

运行时挂载：

```bash
docker run -d --name db -v pg-data:/var/lib/postgresql/data postgres:16
docker run -d --name web --mount type=volume,source=app-data,target=/app/data nginx
docker run -it --rm -v "$PWD":/app -w /app node:22-alpine npm test
```

选择规则：

- 长期数据优先用 named volume，例如数据库数据目录。
- 开发代码同步优先用 bind mount，例如 `"$PWD":/app`。
- 敏感临时数据或缓存可考虑 tmpfs，但容器停止后数据会丢失。

## 网络和端口

```bash
docker network ls
docker network create app-net
docker run -d --name redis --network app-net redis:latest
docker run -d --name api --network app-net -p 8080:8080 my-api:latest
docker network inspect app-net
docker network rm app-net
```

同一个自定义网络内，容器通常可以用容器名互相访问，例如应用容器连接 `redis:6379`。`-p` 是把容器端口发布到宿主机；没有 `-p` 时，容器内服务不一定能从宿主机直接访问。

## Compose 基础

`compose.yaml` 示例：

```yaml
services:
  api:
    build: .
    ports:
      - "8080:8080"
    environment:
      NODE_ENV: production
    depends_on:
      - redis
  redis:
    image: redis:latest
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

常用命令：

```bash
docker compose up
docker compose up -d
docker compose up --build
docker compose ps
docker compose logs -f
docker compose exec api sh
docker compose down
docker compose down -v
```

注意：`docker compose down` 默认会删除 Compose 创建的容器和网络，但不会删除 named volumes；`docker compose down -v` 会同时删除 volumes，可能清掉数据库数据。

## 清理命令

```bash
docker container prune
docker image prune
docker image prune -a
docker volume prune
docker network prune
docker system df
docker system prune
```

清理前先看 `docker system df`。带 `-a` 或 `-v` 的清理命令影响更大，应确认不会删掉仍需要的镜像或数据卷。

## 常见工作流

开发本地应用：

```bash
docker build -t my-app:dev .
docker run --rm -it -p 3000:3000 -v "$PWD":/app -w /app my-app:dev npm run dev
```

一次性调试容器：

```bash
docker run --rm -it alpine:latest sh
```

查看服务问题：

```bash
docker ps -a
docker logs --tail 200 <container>
docker inspect <container>
docker exec -it <container> sh
```

发布镜像：

```bash
docker build -t my-app:1.0.0 .
docker tag my-app:1.0.0 registry.example.com/team/my-app:1.0.0
docker push registry.example.com/team/my-app:1.0.0
```

## 易错点

- `EXPOSE` 只是镜像元数据，不会自动把端口映射到宿主机；运行时仍需 `-p`。
- 容器删除后，写在容器 writable layer 的数据会丢失；需要持久化就挂 volume 或 bind mount。
- `latest` 不是“最新版保证”，只是一个普通 tag。
- `docker exec` 只能进入正在运行的容器。
- `COPY . .` 容易把无关文件放进镜像，应配合 `.dockerignore`。
- `CMD` 可以被 `docker run IMAGE command` 覆盖；`ENTRYPOINT` 更适合固定入口程序。
- `docker compose down -v` 会删除 volume，谨慎用于有状态服务。

## Sources

- [Docker run containers](https://docs.docker.com/engine/containers/run/)
- [Dockerfile overview](https://docs.docker.com/build/concepts/dockerfile/)
- [Dockerfile reference](https://docs.docker.com/reference/builder)
- [Docker image CLI](https://docs.docker.com/reference/cli/docker/image/)
- [Docker image pull](https://docs.docker.com/reference/cli/docker/image/pull/)
- [Docker image tag](https://docs.docker.com/engine/reference/commandline/tag/)
- [Docker volumes](https://docs.docker.com/engine/storage/volumes/)
- [Docker storage overview](https://docs.docker.com/storage/)
- [Docker Compose CLI](https://docs.docker.com/reference/cli/docker/compose/)
- [Docker reference overview](https://docs.docker.com/reference/)
