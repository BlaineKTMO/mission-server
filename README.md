# Mission Server
Hosts a simple flask api

## Requirements
- Docker

## Install
This repo contains a Dockerfile for simple installation of this app
- Clone the repo
- Create the docker container
```sh
docker build -t <container-name> .
```
- Verify successful installation

## Deploy
Build your docker container as mentioned in the install section
- Run your docker container
```sh
docker run --network host -it <container-name>
```

