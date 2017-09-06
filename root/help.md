% NGINX (1) Container Image Pages
% Jan Koscielniak
% June 19, 2017

# NAME
nginx - HTTP and reverse proxy server, mail proxy server

# DESCRIPTION
This image is meant to provide a nginx web server. Image is based on Fedora 26 Boltron and nginx module.

This repository contains file nginx.conf in files folder, where you can configure all the settings you need for nginx to suit your needs. However, please don't change the following lines, as they are needed for proper functionality in a container.

	error_log stderr;
	daemon off;

These lines will redirect error log to stderr and prevent nginx from demonizing itself, which if enabled, would result in docker stopping the container right after starting it, because the root process would exit right after spawning worker processes.

# USAGE
You can run this image in docker like this:

	# docker run -p 8080:80 -v $DIR:/var/www/html/

$DIR in this context is the root of your web application. 

Image can also be run in Openshift. You can obtain the template in the repository of this image - https://github.com/container-images/nginx. You also need to have SCC RunAsUser set to RunAsAny. Then run:

	# oc create -f openshift-template.yml

# ENVIRONMENT VARIABLES
There are no environment variables to be set.

# SECURITY IMPLICATIONS
-p 8080:80
	Exposes port 80 on the container and forwards it to port 8080 on the host. 

-v $DIR:/var/www/html/
	Mounts path $DIR as a web root.

This container runs as root user.

# HISTORY
Similar to a Changelog of sorts which can be as detailed as the maintainer wishes.

# SEE ALSO
Github page for this container with detailed description: https://github.com/container-images/nginx