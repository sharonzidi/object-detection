#MQTT Demo
# Monitor two MQTT topics for data
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
from sense_hat import SenseHat
#define instances of Sense Hat and MQTT library
sense = SenseHat()
client = mqtt.Client()

# Callback for when client received connection from server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    #Note: by subscribing in on_connect, the subscription is renewed if connection is dropped
    client.subscribe("sharon")
    client.subscribe("sharon")
    
# Callback for when a message is received
def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode())
    
    # Each time a direction message is received, change the x or y variable
    if msg.payload.decode() == "{'id': 1, 'name': 'person'}":
        print('person')

        X = [255, 0, 0]  # Red
        O = [255, 255, 255]  # White

        person = [
        O, O, X, X, X, O, O, O,
        O, O, X, X, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, X, X, X, X, X, O, O,
        O, O, O, X, O, O, O, O,
        O, O, X, O, X, O, O, O,
        O, X, O, O, O, X, O, O,
        X, O, O, O, O, O, X, O
        ]
        sense.set_pixels(person)
        
    if msg.payload.decode() == "{'id': 62, 'name': 'chair'}":
        print('chair')


        sense = SenseHat()
        BR = [121, 68, 59]  # Red
        O = [255, 255, 255]  # White

        chair = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, BR, BR, O, O,
        O, O, O, O, BR, BR, O, O,
        O, O, O, O, BR, BR, O, O,
        O, BR, BR, BR, BR, BR, O, O,
        O, BR, O, O, BR, BR, O, O,
        O, BR, O, O, BR, BR, O, O,
        O, BR, O, O, BR, BR, O, O
        ]
        sense.set_pixels(chair)

    if msg.payload.decode() =="{'id': 77, 'name': 'cell phone'}":
        print('phone')
   
        BL = [0, 0, 0]  # Red
        O = [255, 255, 255]  # White

        phone = [
        O, O, O, O, O, O, O, O,
        O, O, BL, BL, BL, BL, O, O,
        O, O, BL, O, O, BL, O, O,
        O, O, BL, O, O, BL, O, O,
        O, O, BL, O, O, BL, O, O,
        O, O, BL, O, O, BL, O, O,
        O, O, BL, O, O, BL, O, O,
        O, O, BL, BL, BL, BL, O, O
        ]
        sense.set_pixels(phone)

#Create MQTT client and attach routines

client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()
    


    
