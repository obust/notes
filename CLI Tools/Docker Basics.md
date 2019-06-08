# Docker Basics

## Installation

## Manage images

#### List images

`docker images`  

```bash
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              c54a2cc56cbb        11 weeks ago        1.848 kB
docker/whalesay     latest              6b362a9f73eb        16 months ago       247 MB
```

#### Build an image (from a Dockerfile)

A Dockerfile **describes the software recipe that is “baked” into an image**. It can tell the software what environment to use or what commands to run, etc.

`docker build <dockerfile-path> -t <image-name>`

1. Reads the Dockerfile at <dockerfile-path>
2. Builds an image called <image-name> on your local system

#### Run an image

`docker run <image>`  
1. Looks for the <image> image on the local system. If the image isn't there, docker downloads it from [Docker Hub](https://hub.docker.com/).
3. Loads the image in a container.
4. Runs the container.

#### Remove an image

`docker rmi <image>`

## Docker Hub

Docker Hub is a cloud-based registry service which allows you to link to code repositories, build your images and test them, stores manually pushed images, and links to Docker Cloud so you can deploy images to your hosts.

#### Tag an image

`docker tag <image-id> <image-name>:<tag>`

- `<image-id>`: The image ID
- `<image-name>`: The image name. To associate the image with your Docker Hub account, follow the repository syntax `<dockerhub-namespace>/<repo-name>` for `<image-name>`.
- `<tag>`: Version label or tag (e.g. `latest`, `1.5.0`)

#### Log into Docker Hub from CLI

Login with your Docker ID to push and pull images from Docker Hub.

`docker login`

```
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username:
Password:        
Login Succeeded
```

#### Push an image

`docker push <image>`

#### Pull an image

`docker run <dockerhub-namespace>/<repo-name>`

## Manage containers

#### List containers

`docker ps -a`

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
d8339466bdb2        docker/whalesay     "cowsay boo"        14 minutes ago      Exited (0) 14 minutes ago                       thirsty_shirley
2cbc2af55011        hello-world         "/hello"            33 minutes ago      Exited (0) 33 minutes ago                       berserk_cori
```

#### Remove a container

`docker rm <container>`

#### Rename a container

`docker rename <old-name> <new-name>`

## Schedule containers

- `docker start <container> [<container>]`: Start one/many stopped containers
- `docker stop <container> [<container>]`: Stop one/many running containers
- `docker pause <container> [<container>]`: Pause all processes within one/many containers
- `docker restart <container> [<container>]`: Restart a container
