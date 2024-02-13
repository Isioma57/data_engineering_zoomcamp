# Docker

| Description                                         | Command                                      |
|-----------------------------------------------------|----------------------------------------------|
| **Start a new container**                           | `docker run [options] image [command]`       |
| **List running containers**                         | `docker ps`                                  |
| **List all containers (running and stopped)**       | `docker ps -a`                               |
| **Run container in the background (detached)**      | `docker run -d [container_id/name]`          |
| **Stop a running container**                        | `docker stop [container_id/name]`            |
| **Remove a container**                              | `docker rm [container_id/name]`              |
| **Pull an image from a registry**                   | `docker pull [image_name]`                   |
| **Build an image from a Dockerfile**                | `docker build -t [image_name] .`             |
| **List all images**                                 | `docker images`                              |
| **Remove an image**                                 | `docker rmi [image_name]`                    |
| **Execute a command in a running container**        | `docker exec [options] [container_id] [cmd]` |
| **View logs of a container**                        | `docker logs [container_id/name]`            |
| **Inspect a container (get detailed info in JSON)** | `docker inspect [container_id/name]`         |
| **View real-time events from the Docker daemon**    | `docker events`                              |
| **Tag an image for a repository**                   | `docker tag [source_image] [target_image]`   |
| **Push an image to a registry**                     | `docker push [image_name]`                   |
| **Create a new network**                            | `docker network create [network_name]`       |
| **List networks**                                   | `docker network ls`                          |
| **Remove a network**                                | `docker network rm [network_name]`           |
| **Attach a running container to a network**         | `docker network connect [network_name][container_id/name]`|
| **Detach a container from a network**               | `docker network disconnect [network_name] [container_id/name]` |

