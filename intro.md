# Computer Vision in FRC

So, let's talk about computer vision in FRC. First, what do I mean when I say computer vision? I simply mean finding a target using a camera. I'm going to focus on how to actually find and hit a stationary target in FRC. For this article we're going to be using Python and OpenCV. In competition you would likely want to use Java/C++ bindings for OpenCV for if you need more speed, however, you likely don't need to and Python would be fine.

We're going to go over a few various options for what folks have been doing in FRC for a while. The first big decision you have to make (after deciding you need vision) is whether you want to do it onboard the RoboRio or offboard. Both have their advantages.

Onboard:

- Easier integration into main robot code
- Typically lower latency between acquiring image and processing it

Offboard:

- Typically faster processors
- Can develop offboard robot

For the purposes of this article we're going to assume offboard. Being able to develop off the robot is a serious benefit as it allows you to tune your algorithms easier. Next we have a couple options for how to process the image:

Grip
- Simple, doesn't require much in the way of coding
- Communication to Robot is handled for you

OpenCV
- More complete control of image processing


900's Neural Network Stuff
- Not going to lie, I mention this for completeness, 900 is full of wizards, read some of their whitepapers. If you're looking into this I doubt this post will help you.

Scoping tutorials is important so we're going to focus on OpenCV (also, Grip is pretty well documented elsewhere).

Now, let's talk about general steps for computer vision stuff in FRC:

1. Acquire Image
2. Process Image
3. Determine Pose Change

Honestly, the magic happens in steps 2 and 3, let's jump right into this. To make your life easier I've put together a simple OpenCV playground for you. You can download the repo [here](git@github.com:schreiaj/open-cv-playground.git). Im going to assume you're using that from here on out. I put it together because installing OpenCV tends to get hairy and I don't want to have folks fighting with install issues on top of learning the tool. Also, Docker is awesome and special thanks to Team 900 for providing sample images for this.

To get started, follow the instructions in the repo (it should be a simple matter of building the docker image and running it) You can then navigate to localhost:8888 and open the training notebook. In it you can open the `01_Getting_Started` notebook. It will walk you through the process of processing the image.
