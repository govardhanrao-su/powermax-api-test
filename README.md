# powermax-api-test
Unisphere for PowerMax REST API calls  test using PyU4V python module in a docker container. 

# pmax-automation
PowerMAX2000 storage systems automation

# PyU4V Configuration
Create `PyU4V.conf` in the current working directory and edit PyU4V configuration settings in `PyU4V.conf` under the [setup] heading, these setting will need to reflect your environment configuration:

```
[setup]
username=pyu4v-user
password=secret-pass
server_ip=10.0.0.75
port=8443
array=00012345678
verify=False
```

## Demo

- Install Docker Desktop - https://docs.docker.com/desktop/

- clone repo - `git clone git@github.com:govardhanrao-su/powermax-api-test.git`

- cd `powermax-api-test`

- Run command `docker-compose build` to build the docker image

- Run command `docker-compose up` to start the container

- open another terminal to test API using curl command `curl localhost:8000`

- Run command `docker-compose up -d ` to start the container in detach mode
