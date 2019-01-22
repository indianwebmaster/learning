## Sources:
 1. https://opensource.com/resources/what-docker
 1. https://opensource.com/business/14/8/docker-is-not-virtualization
 1. https://tutorials.ubuntu.com/tutorial/tutorial-windows-ubuntu-hyperv-containers
 1. https://ropenscilabs.github.io/r-docker-tutorial/01-what-and-why.html
 1. https://blog.docker.com/2016/03/docker-for-mac-windows-beta/

## Keywords
 1. __Image__: A distributable dockerized package of an application is referred to as an Image.
 1. __Container__: An instance of an _image_ installed within a Docker environment, so the application can be run, is termed as a Container. A single image can have multiple containers on a single target host.
 
## What is Docker
Docker, unlike a virtual machine, is a tool designed to make it easier to create, deploy and run applications by using containers. With Containers, developers can package up an application with all of the parts needed by the application, such as libraries and other dependencies, and ship it all as one package. With this container, the developer can be assured that the application will run on any other machine<sup>[1](#footnote1)</sup> that has the Docker platform installed, regardless of any differences in settings between the original developer's machine vs the other machine.

## Docker vs Virtual Machine
In a way, Docker is a bit like a virtual machine, in that its purpose is to allow a "containerized" application to run on any other client. However, unlike a VM that creates a whole virtual operating system, Docker allows applications to use the same kernel<sup>[1](#footnote1)</sup> as the system they are running on and only requires applications to be shipped with things not already running on the target computer. This gives a significant performance boost and reduces the size of the application.

However, Docker does not provide *__virtualization__* as mostly understood. __Virtualization__ is an act of isolating the _consumers_ of a service with the _providers_ of a service (file system access, networking etc.) in such as way so as to make the _provider_ appear as something else, so it can be used by the _consumer_. This lack of key functionality in Docker, of abstracting services, is what makes it short of a __virtualization__ tool. For example, a virtual machine framework such as VirtualBox or VMWare allows multiple discrete operating systems to consume a physical server by abstracting the services provided by the host server (CPU, memory, disk etc.) in such a way that each _virtual_ operating system is oblivous to the true underlying characteristics of the host server.

Even now, if you are thinking, _But doesn't Docker provide virtualization to applications by virtualizing the operating system to them?_ I would say, unlike a VM framework, you can think of Docker as a *__conductor__* that orchestrates the services offerred by the host server and those packaged in the dockerized application in a way that they can run cooperatively in a seamless fashion. In fact, you can do this without Docker, as was being done (and is still done) for many applications, by wrapping the application in an *__install script__*. However, the question to ask would be, "Why, when Docker does it for us?".

## Why would I want to use Docker
Imagine you are working on an analysis in python and you send your code to a friend. Your friend runs exactly this code on exactly the same data set but gets a slightly different result. This can have various reasons such as a different operating system, a different version of a python package, etc. Docker is trying to solve problems like that. In the above example, if instead you send your application as a docker container to your friend, both should get identical results.

Another use case would be if you are working on an analysis project on your computer, but want to run it on another much more powerful machine or a machine in the "cloud".

Now, one can easily argue that you can address both the use cases above by expecting that the target server install the required virtual machine framework with the required specifications. Heck, the developer could install his application in a virtual environment and create a _virtual appliance_ image to make this easier. For example, provide a _VirtualBox appliance image with Ubuntu 11.05, with php 7.0, Laravel, nginx and your application_. All the user has to do is install the VirtualBox application on their machine (on any machine/any OS that supports it), create a new virtual machine using the appliance you provided, start this virtual machine and viola, they are in business. Other than performance, all other results should match those of the application developer.

The above scenario is definitely a plausible option, and in this day and age where disk space and processing power are available in abundance, it may be an option to seriously consider. First, let's look at the same scenario when using Docker.

The developer has Docker installed on this computer, and uses the same to create a Docker image of his application. The user would take this Docker image *__on a compatible operating system__*<sup>[2](#footnote2)</sup> (that would not need a Virtual Machine layer - more on this later) running Docker. He would install this image as a Docker container on his machine and launch the application within this container. As before, other than performance, all other results should match those of the application developer.

### Pros and Cons of Docker Image vs VM appliance
So, we can achieve the same result in either case. And, at first glance, it would appear that the VM appliance scenario is "easier" and more failproof. Agreed. If the Docker image is installed on a target machine running a incompatible operating system<sup>[2](#footnote2)</sup> than the developer's machine, the benefits of the Docker image are lost. However, if that is not the case, then the relatively lightweight Docker image greatly outweighs the VM appliance. Consider the scenario where you have three applications to run, all on linux but one and two with php 7.0 and two and three with apache. In case of VM appliances, you will need three VM instances to ensure each variant has exactly the services they desire, a resource intensive option. However, with Docker, you have three containers and the "shared resources" for the three containers are made available to each isolated container. A much better usability aspect for most users, that expect to generally expect to run multiple applications. In addition, since march 2016, Docker has created a deep integration with the [low level virtualization capabilities available within Windows and MacOS](https://blog.docker.com/2016/03/docker-for-mac-windows-beta/), such that running a linux application in a Docker container on these two operating systems is much more seamless (and _lighter weight_ ) than before when Docker actually would include and start a VirtualBox instance. Docker for Mac integration has further been architected from scratch to be able to fit the OS X sandbox security model.

# More to come
 1. A quick tutorial to use a Docker container
 1. A quick tutorial to dockerize an application

##### footnote1
While a docker container that has packaged a linux application, cannot run directly on a Windows machine even with Docker installed, the docker framework makes it "easy" to download and install a Virtual Machine Container, and execute the application in this VM. See [Run Linux containers in Windows](https://tutorials.ubuntu.com/tutorial/tutorial-windows-ubuntu-hyperv-containers).
The same is true in the other direction too, and so also for linux applications that need to run on MacOS etc. Because, a variety of linux distributions rely on the same low level linux kernel, the biggest bang for the buck for Docker comes when dockerizing linux applications and running them on other flavors, albeit linux, target systems.

##### footnote2
As mentioned in <sup>[1](#footnote1)</sup>, you cannot setup a linux docker image as a container on a Windows server, without inserting a linux virtual machine layer. This is because Docker containers use many different technologies build into the Linux kernel (_Hope you know the difference between a Linux kernel and Linux Distribution. If not, that is another discussion_). Most linux distributions share the same base kernel. When you create a Docker container (on a Linux server), the application uses these technologies to create an isolated _container_ environment to run the application. The isolation is in various forms, such as a _jailed_ filesystem from within a directory and not knowing that there's a whole other world out there. Thus, within the linux world, there are many different flavors compatible with a docker image. *__Can a docker image created on MacOS be run on Linux without a VM layer (and vice versa)?__*

