---
type: "topic"
status: "active"
created: "2026-05-22"
updated: "2026-05-22"
sources:
  - "../../_raw/infra/docker-basic-syntax-sources.md"
tags: ["docker", "container", "image", "compose", "infra"]
---

这页不是按 Docker CLI 字母表整理，而是按真实使用顺序组织：先理解镜像和容器，再学会运行、查看、进入、挂载、联网，最后用 Dockerfile 和 Compose 把流程固化。

## 先建立地图

Docker 日常工作可以压缩成一条链路：

```text
Dockerfile -> image -> container -> logs/exec/ports/volumes/networks -> cleanup
```

对应到命令：

```bash
docker build -t my-app:dev .
docker run --name app -p 3000:3000 my-app:dev
docker logs -f app
docker exec -it app sh
docker stop app
docker rm app
```

如果只记一件事：镜像是模板，容器是运行实例。你构建、拉取、打标签的是镜像；你启动、停止、看日志、进入 shell 的是容器。

## 1. 镜像：拿到可运行模板

镜像包含应用、依赖、运行时和默认启动配置。镜像可以从 registry 拉取，也可以从 Dockerfile 构建。

### 常用命令

| 任务 | 命令 |
| --- | --- |
| 拉取镜像 | `docker pull nginx:latest` |
| 查看本地镜像 | `docker images` 或 `docker image ls` |
| 查看镜像细节 | `docker image inspect nginx:latest` |
| 给镜像打标签 | `docker tag my-app:local registry.example.com/team/my-app:1.0.0` |
| 推送镜像 | `docker push registry.example.com/team/my-app:1.0.0` |
| 删除镜像 | `docker rmi nginx:latest` |
| 清理悬空镜像 | `docker image prune` |

### 镜像名怎么读

```text
[HOST[:PORT]/]NAMESPACE/REPOSITORY[:TAG]
```

例子：

```text
nginx:latest
redis:7
ghcr.io/org/app:1.2.3
registry.example.com/team/my-app:2026-05-22
```

省略 registry、namespace、tag 时，Docker 通常会按 Docker Hub、`library` 命名空间、`latest` tag 处理。生产环境尽量显式写 tag，因为 `latest` 只是一个普通标签，不等于稳定或最新保证。

## 2. 容器：把镜像跑起来

`docker run` 是最常见也最容易写长的命令。它的基本形状是：

```bash
docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```

### 从简单到常用

```bash
# 前台运行
docker run nginx:latest

# 后台运行，并指定容器名
docker run -d --name web nginx:latest

# 运行一次命令，退出后自动删除容器
docker run --rm alpine:latest echo hello

# 进入交互式 shell
docker run --rm -it ubuntu:24.04 bash

# 把容器 80 端口映射到宿主机 8080
docker run -d --name web -p 8080:80 nginx:latest

# 注入环境变量
docker run -e NODE_ENV=production --env-file .env my-app:1.0.0

# 指定工作目录并运行测试
docker run --rm -v "$PWD":/app -w /app node:22-alpine npm test
```

### 高频参数速查

| 参数 | 作用 | 常见场景 |
| --- | --- | --- |
| `--name web` | 指定容器名 | 后续用名字执行 `logs`、`exec`、`stop` |
| `-d` | 后台运行 | 服务类容器 |
| `--rm` | 退出后删除容器 | 一次性命令、临时调试 |
| `-it` | 交互式终端 | 进入 shell |
| `-p 8080:80` | 宿主机端口映射到容器端口 | 本机访问 Web 服务 |
| `-e KEY=value` | 设置环境变量 | 配置应用 |
| `--env-file .env` | 批量加载环境变量 | 本地开发配置 |
| `-v source:target` | 挂载 volume 或宿主机路径 | 持久化数据、同步代码 |
| `-w /app` | 设置工作目录 | 运行构建、测试命令 |
| `--network app-net` | 加入网络 | 多容器互相访问 |
| `--restart unless-stopped` | 设置重启策略 | 长期运行的服务 |

## 3. 查看、进入和控制容器

容器启动后，排查问题通常按这个顺序走：先看状态，再看日志，再进入容器，最后 inspect 配置。

```bash
docker ps
docker ps -a
docker logs --tail 100 web
docker logs -f web
docker exec -it web sh
docker inspect web
docker stats
docker stop web
docker start web
docker restart web
docker rm web
docker rm -f web
```

### 什么时候用哪个命令

| 问题 | 命令 | 判断点 |
| --- | --- | --- |
| 服务有没有跑 | `docker ps` | 只显示运行中的容器 |
| 容器是不是已退出 | `docker ps -a` | 看 `STATUS` 和退出时间 |
| 为什么启动失败 | `docker logs <container>` | 看应用错误和启动日志 |
| 需要实时看日志 | `docker logs -f <container>` | 类似 `tail -f` |
| 想进容器排查 | `docker exec -it <container> sh` | 容器必须正在运行 |
| 不知道端口、挂载、环境变量 | `docker inspect <container>` | 输出完整 JSON 配置 |
| 看资源占用 | `docker stats` | CPU、内存、网络、IO |

基础镜像里不一定有 `bash`，进入失败时先试 `sh`。

## 4. Dockerfile：把构建过程写下来

Dockerfile 用来描述镜像如何生成。一个最小的 Node 服务镜像大致长这样：

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

### 指令分层理解

| 层次 | 指令 | 作用 |
| --- | --- | --- |
| 基础 | `FROM` | 选择基础镜像，也开始一个新的构建阶段 |
| 目录 | `WORKDIR` | 设置后续命令的工作目录 |
| 文件 | `COPY` | 把构建上下文里的文件复制进镜像 |
| 构建 | `RUN` | 构建时执行命令并生成新镜像层 |
| 配置 | `ENV`、`ARG` | 分别设置运行时变量和构建时变量 |
| 端口 | `EXPOSE` | 声明容器内服务端口 |
| 启动 | `CMD`、`ENTRYPOINT` | 定义容器默认启动行为 |
| 权限 | `USER` | 切换运行用户，减少 root 运行风险 |
| 健康 | `HEALTHCHECK` | 声明健康检查 |

### 构建命令

```bash
docker build -t my-app:1.0.0 .
docker build -f Dockerfile.prod -t my-app:prod .
docker build --build-arg NODE_ENV=production -t my-app:prod .
```

`.` 是 build context，`COPY` 只能访问 context 内的文件。配合 `.dockerignore` 排除 `node_modules`、日志、临时文件、密钥和本地构建产物，可以让镜像更小，也减少泄漏风险。

## 5. 存储：区分临时文件和长期数据

容器自己的 writable layer 会随着容器删除而丢失。只要数据需要留下来，就应该显式挂载。

### 三种常见选择

| 类型 | 语法 | 适合场景 |
| --- | --- | --- |
| named volume | `-v pg-data:/var/lib/postgresql/data` | 数据库、上传文件、长期状态 |
| bind mount | `-v "$PWD":/app` | 本地开发时代码同步 |
| tmpfs | `--tmpfs /tmp` | 临时敏感数据或缓存 |

### volume 命令

```bash
docker volume create app-data
docker volume ls
docker volume inspect app-data
docker volume rm app-data
```

### 挂载示例

```bash
# 数据库数据持久化
docker run -d --name db -v pg-data:/var/lib/postgresql/data postgres:16

# 更明确的 --mount 写法
docker run -d --name web --mount type=volume,source=app-data,target=/app/data nginx

# 本地代码挂载进容器运行测试
docker run --rm -it -v "$PWD":/app -w /app node:22-alpine npm test
```

## 6. 网络和端口：容器之间、本机和外界

端口映射解决“宿主机访问容器”的问题；Docker network 解决“容器之间互相访问”的问题。

```bash
docker network ls
docker network create app-net
docker run -d --name redis --network app-net redis:latest
docker run -d --name api --network app-net -p 8080:8080 my-api:latest
docker network inspect app-net
docker network rm app-net
```

同一个自定义网络内，容器通常可以用容器名互相访问。例如 API 容器可以连接 `redis:6379`。`-p 8080:8080` 则是把容器端口发布到宿主机，让你能从本机访问服务。

## 7. Compose：把多容器应用写成配置

当应用需要数据库、缓存、队列等多个容器时，用 `docker compose` 比手写一串 `docker run` 更稳定。

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

`docker compose down` 默认删除 Compose 创建的容器和网络，但保留 named volumes。`docker compose down -v` 会删除 volumes，可能清掉数据库数据。

## 8. 清理：先看占用，再动手删

```bash
docker system df
docker container prune
docker image prune
docker image prune -a
docker volume prune
docker network prune
docker system prune
```

建议顺序：

1. 先用 `docker system df` 看磁盘占用。
2. 只清明确不需要的资源，例如停止的容器或悬空镜像。
3. 谨慎使用带 `-a` 或 `-v` 的清理命令，因为影响范围更大。

## 常见工作流

### 本地开发一个 Web 服务

```bash
docker build -t my-app:dev .
docker run --rm -it -p 3000:3000 -v "$PWD":/app -w /app my-app:dev npm run dev
```

### 临时开一个干净环境

```bash
docker run --rm -it alpine:latest sh
```

### 排查容器启动失败

```bash
docker ps -a
docker logs --tail 200 <container>
docker inspect <container>
docker exec -it <container> sh
```

如果容器已经退出，`docker exec` 不能进入；先看 `docker logs` 和 `docker inspect`。

### 构建并发布镜像

```bash
docker build -t my-app:1.0.0 .
docker tag my-app:1.0.0 registry.example.com/team/my-app:1.0.0
docker push registry.example.com/team/my-app:1.0.0
```

## 易错点

| 易错点 | 正确认知 |
| --- | --- |
| `EXPOSE` 会自动开放端口 | 不会。它只是镜像元数据，运行时仍要 `-p` |
| 删除容器后数据还在 | 不一定。容器 writable layer 会丢，持久数据要挂 volume |
| `latest` 就是最新版 | 不是。它只是一个普通 tag |
| `docker exec` 能进入任何容器 | 只能进入正在运行的容器 |
| `COPY . .` 很省事 | 也容易把无关文件和密钥复制进镜像，应使用 `.dockerignore` |
| `CMD` 和 `ENTRYPOINT` 一样 | `CMD` 更像默认参数或默认命令，`ENTRYPOINT` 更像固定入口 |
| `docker compose down -v` 很安全 | 它会删除 volumes，可能删除数据库数据 |

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
