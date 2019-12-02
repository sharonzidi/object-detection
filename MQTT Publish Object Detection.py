# MQTT Publish Demo
# Send joystick instructions to MQTT topic

#import necessary libraries
import paho.mqtt.publish as publish
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep

#define instance of Sense Hat
sense = SenseHat()


#define what to do when joystick pressed in different directions
#each function sends the name of the direction to the test channel on the hivemq broker

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        publish.single("INTD320/test", "up", hostname="broker.hivemq.com")

def pushed_down(event):
    if event.action != ACTION_RELEASED:
        publish.single("INTD320/test", "down", hostname="broker.hivemq.com")

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        publish.single("INTD320/test", "left", hostname="broker.hivemq.com")

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        publish.single("INTD320/test", "right", hostname="broker.hivemq.com")


#call the direction functions when the joystick is pressed
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
pause()
