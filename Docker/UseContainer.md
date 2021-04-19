# Tutorial on how to use a Docker Container

You have started the container for this tutorial! Here's the command:

  `docker run -d -p 80:80 docker/getting-started`

flags being used
* -d - run the container in detached mode (in the background)
* -p 80:80 - map port 80 of the host to port 80 in the container
* docker/getting-started - the image to use

## What is a container image
When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image. Since the image contains the container's filesystem, it must contain everything needed to run an application - all dependencies, configuration, scripts, binaries, etc. The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.

