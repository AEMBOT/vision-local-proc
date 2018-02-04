# Useful resources for figuring stuff out
### *WIP*
1. [Co-processor Network Tables (raspberry pi)](https://pypi.python.org/pypi/pynetworktables) - Network table library for the pi.  
    * [Pytables Startup](http://robotpy.readthedocs.io/en/stable/guide/nt.html)
    * (Screensteps) [IP Specs](https://wpilib.screenstepslive.com/s/4485/m/24193/l/319135-ip-networking-at-the-event )
    
2. [GRIP Piplline](https://github.com/WPIRoboticsProjects/GRIP) - Generates a pipeline so you don't have to mess with opencv under the hood.  If you use this, there is very little programmming you need to do with opencv.  Take a look at any of the generated code samples for more an example.
    * (Screensteps) [FIRST GRIP Tutorial](https://wpilib.screenstepslive.com/s/currentCS/m/vision/l/463566-introduction-to-grip)
    
3. (Screensteps) [Client Side Network Tables](https://wpilib.screenstepslive.com/s/3120/m/7912/l/80205-writing-a-simple-networktables-program-in-c-and-java-with-a-java-client-pc-side) - Client side code will be ran on the RoboRio, this code will search for network table values published by the raspberry pi/co-processor.

4. (Linux-esque Only) [Changing Camera Settings](http://www.techytalk.info/webcam-settings-control-ubuntu-linux/comment-page-1/) - Useful for when Grip settings aren't quite enough.  By physically changing exposure and saturation, Grip is able to more efficiently do stuff.

5. [All things opencv/rpi](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) - Guide for building opencv**3** on a raspberry pi, good luck. Python 3 preferably.
