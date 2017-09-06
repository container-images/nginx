# nginx web server container
This is an example of how nginx can be easily run in a Docker container. Please note that this version is not suitable for production use, but feel free to tinker with it. This container is built on top of [base-runtime](https://hub.docker.com/r/baseruntime/baseruntime/) (a minimal image) and uses nginx module.

# Configuration
This repository containes file **nginx.conf** in files folder, where you can configure all the settings you need for nginx to suit your needs. However, please don't change the following lines, as they are needed for proper functionality in a container.
```
error_log stderr;
daemon off;
```
These lines will redirect error log to stderr and prevent nginx from demonizing itself, which if enabled, would result in docker stopping the container right after starting it, because the root process would exit right after spawning worker processes.

You can mount your own web root like this:
```
$ docker run -v <DIR>:/var/www/html/
```
You can replace \<DIR> with location of your web root. Please note that this has to be an **absolute** path, due to Docker requirements. 



# Running in Docker
You can get this continer image from docker hub:

```
$ docker pull modularitycontainers/nginx
```

This container can be run in two ways:

1\) **From shell**
```sh
$ docker run -p 8080:80 
```
This starts the container and forwards port 80 from container to port 8080 on host. You'll see the nginx default page. 

2\) **With a Makefile**

In order to simplify running the container, you can use a supplied Makefile. By default it will only build the image and tag it. If you set the **DOCUMENT_ROOT** variable, executing make will also run the container. You can set the following options there:
```sh
# Docker container tag
IMAGE_NAME = nginx

# An absolute path to your web root
#DOCUMENT_ROOT = /

# A port you want your nginx server to run on host
PORT = 8080
```

# Running in Openshift
To run this container in OpenShift, you need to change the `RunAsUser` option in the `restricted` Security Context Constraint (SCC) from `MustRunAsRange` to `RunAsAny`. Do it by running:

```Shell
$ oc login -u system:admin
$ oc project default
$ oc edit scc restricted
```

Find `RunAsUser` and change its value from `MustRunAsRange` to `RunAsAny`. This is needed as nginx master process is running as a root.

Then you can run `openshift-template.yml` in this repository:

```Shell
$ oc login -u developer
$ oc create -f openshift-template.yml
```
