# Apacha Kafka
Apache Kafka is an open source messaging system.
We will install it inside a docker container.

## Setup on Raspberry Pi
As preperation, you need to download and flash the newest [Raspbian OS](https://www.raspbian.org/) to your raspberry pi.

Now please connect to your raspberry pi via [ssh](https://en.wikipedia.org/wiki/Secure_Shell) and change the user to **root**.
Download installer and let it run.
```bash
$ sudo su - 
$ cd ~
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
```

The installation can take some time, so please relax.
Double check if docker is installed properly.
```bash
$ docker --version
Docker version 19.03.8, build afacb8b
```

With the default setup, only users with root privileges can start an stop docker containers. If you prefer to manage docker with your own user and are bored to use `sudo`, please add your user to `docker` group.
```
$ usermod -aG docker <youUserName>
```

## Setup docker
https://success.docker.com/article/getting-started-with-kafka