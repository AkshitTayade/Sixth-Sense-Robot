# Sixth-Sense-Robot
<p align='center'>
     <img alt="GIF" src="https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/main_video.gif" width="800" height="500" />
     <img alt="GIF" src="https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/Screenshot%202020-01-03%20at%207.54.24%20PM.png" width=800/>
</p>

## Arduino Programming
* Define the Pins assosicate with motor driver
* Take input as Serially
* Define the motion of the motors for forward, backwards, left, right, stop
* Then flash in the code into the arduino
* Work of arduino is done here !
> Code can be found [here](https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/Motor_Driver_SerialPort.ino)

<p align="center">
  <img alt="GIF" src="https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/Screenshot%202020-01-03%20at%207.53.56%20PM.png" width=800/>
  <img alt="GIF" src="https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/Screenshot%202020-01-03%20at%207.53.13%20PM.png" width=800/>
</p>

## Python Programming

> Pipeline for Tracking the coloured object :
1. Smoothen the Image
2. Define 3x3 matrix to track object within itself
3. Define the Region of Interest, by method of masking within defined matrix
4. Thresholding the image to only see coloured object
5. Find contours of ROI
6. Once largest index of contour is found, bound it using an rectangle
7. Declare a pointer (ie circle) which tracks the co-ordinate system of object during motion
8. Then compare these co-ordinates with 3x3 matrix, and hence define required movements for the robot
> Code can be found [here](https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/Final%20program.py)

<p align="center">
  <img alt="GIF" src="https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/Screenshot%202020-01-03%20at%207.54.43%20PM.png" width=800/>
  <img alt="GIF" src="https://github.com/AkshitTayade/Sixth-Sense-Robot/blob/master/Screenshot%202020-01-03%20at%207.54.54%20PM.png" width=800/>
</p>

## Few Tricks in Windows/macOS for configuring Arduino Uno
* In Windows, Ardunio IDE has direct visibility of the port name.
* In macOS, As you'll have to put the serial port of arduino into the python programming, you can face a problem of not getting the port name.
* So type this command in terminal:**ls -1 /dev/tty** - Using this you can find the serial port name!

### Required Libraries in Python:
 1. OpenCV
 2. Numpy
 3. Serial
 4. Time

> Once the arduino code in flashed in, close your arduino IDE and run your python file.
