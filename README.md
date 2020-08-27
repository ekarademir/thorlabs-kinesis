# thorlabs_kinesis

Python bindings for Thorlabs Kinesis DLLs. This project aims to map all C API
functions provided by Kinesis libraries to python. More information on
Kinesis Motion Control Software can be found on
[Thorlabs' Website](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control).

The version I'm using to map the libraries is **1.14.4.0 64 Bit**

This project emerged as a need to use it with Thorlabs BSC201, BSC203, and LTS150. So examples are tested with those controllers on Windows 7 with Python 3.6.
Part of this project emerged as a need to use it with **Thorlabs KCube DC Servo**. So these examples are tested with those controllers on Windows 10 with Python 3.6.

Binding methodology is inspired by
[PySDL2](https://github.com/marcusva/py-sdl2) project.

Code structure in the original DLLs is transferred 1-1, even though it could
have benefited from some refactoring. This makes easier to map examples given in
Thorlabs' documentation.

## Using

At it's current stage this module only provides bindings. So, basic mapping of
C code provided with the Kinesis documentation should be enough to use the
module. **However** you have to make sure that DLLs are in the PATH. For that,
you can add the Kinesis folder to PATH.

## Status of this project

This is not a finished up project by any means. I have created this repo when I was working for a LASER manufacturing company. It served well for the two types of motorized stages that we had at hand, however Kinesis reigns over a lot more types. Kindly, **David Tebbe** has provided a patch for another type of stage.

If you wish to use this library, unfortunatelly you will need to figure out a lot of stuff for yourself. This is partly because I didn't have time to develop this project further, but mainly because Thorlabs kind of sucks at providing a good development kit.

The way to approach this library is to get an idea on how to approach Kinesis API, which is basically the way to communicate with the Kinesis server and also keeping in mind the fact that communicating with different devices is an asynchronous problem and asynchronous problems are hard to solve with synchronous code, but that didn't stop Thorlabs from trying! Hence best approach would be, try to wrap API functions by using this library and that wrap it again with async code. Don't try to communicate with the server all at once; verify each action is done correctly. Then if you need to synchronise several actions, use the async tools provided by Python.

There have been emails sent to me about how to set up such an environment, but actually I have no idea. I've set up one environment for myself about more than 2 years ago and it worked for me, but it might not work for you. I am going to quote the reply I've sent here if it might help:

  >I tried to find the code I've written around that library but I couldn't. However there are few stuff that I remember. First thing is that, thorlabs kinesis API by itself is not enough to make the motor move. It took me few days to figure that out. The API is actually for communicating with Kinesis server, which has to be running. Moreover, just starting the server is not enough. You'll notice that, 
  
  >1) If you start the server, then use the Kinesis software to control the motors, Then exit the Kinesis software, without stopping the server, then follow the examples, you will be able to move the motors.
  >2) If you start the server, then use the API directly, the motors won't move!

  >The reason that in the second case the motors don't move is that the server needs to initialize the motors. Unfortunately, all the initialization functions in the API are not enough. The server needs some parameters. Like the step size, backlash amount, max number of steps etc. Maybe few more that I can't remember. All those parameters have API functions for setting them. HOWEVER, there is no place that you are able to find them. I found them by trial and error and some luck guesses, and by following an incorrect PDF that I've downloaded from somewhere on Thorlabs. I also remember going through some XML and INI files that came with the Kinesis software. Another way is to use the Firmware debugger (if I remember correctly.) There are some low level commands that you can send through that debugger, some of those commands are retrieving these values. After firing up the Kinesis software and then exiting the program, you can use the debugger program to retrieve some of the correct values.

  >I don't remember the details of any of those unfortunately. I remember the stuff above because it was very painful. After two weeks of tinkering, I've created another library that handles those knarly details for me, however the code is not with me now.

  >To see if the stages move, first start with initializing the motors with the kinesis program and then exiting it. Then you should be able to control the motors through Python. 

  >Also keep in mind that I haven't implemented the whole API. I only implemented long stage and stepper motors. If you are using the brushless motor, you might need to add the necessary wrapping for that. Even if there is an implementation for brushless motor, it might not be correct as I just copied and pasted stuff from stepper motors and tried to follow the header files, WITHOUT actually being able to test it, because I don't have the controllers or motors anymore.
