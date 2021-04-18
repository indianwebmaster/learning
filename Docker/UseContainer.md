## Tutorial on how to use a Docker Container
You have started the container for this tutorial! Here's the command:
  `docker run -d -p 80:80 docker/getting-started`
flags being used
	-d - run the container in detached mode (in the background)
	-p 80:80 - map port 80 of the host to port 80 in the container
	docker/getting-started - the image to use
