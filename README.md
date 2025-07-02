# Arduino Radar

This project applies programming in C and Python, along with Arduino hardware, a servo motor, and 
an ultrasonic senser module to create a radar sensor.

The viewing screen is made with Python and the Matplotlib library, and the backend is programmed with 
Arduino C. 

For the hardware, the servo is set to move back and forth for 180 degrees, with the ultrasonic
sensor attatched to the top. THe ultrasonic sensor sends out a high pitched sound, and if it bounces
back it can display the distance between the sensor and the object. It is only displayed if it is 
within 35 centimeters.
