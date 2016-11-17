# OpenCV Playground

Because setting up OpenCV on your local machine can suck (esp if you're on OSX like I am) I put together a simple Dockerfile to set up a container. This is designed to give you a nice place to play with vision without having to deal with setting it up.

I've also included a sample image and am looking to find more for folks to experiment with.


## Getting Running

Install Docker for your operating system

Clone this repository.

Navigate to that directory in your terminal.

`docker build -t opencv .  `

`docker run -p 8888:8888 opencv`

You can then access IPython at [localhost:8888](localhost:8888)

It will have OpenCV bindings already installed and set up.

----

There's an example of a script in `completed.py`. 
