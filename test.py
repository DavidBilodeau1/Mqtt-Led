from led import LED
import time
import paho.mqtt.client as mqtt

broker_address="192.168.0.136"

def on_message(client, userdata, message):
    if message.payload.decode("utf-8") == "1":
        bleu.on()
    elif message.payload.decode("utf-8") == "0":
        bleu.off()

client = mqtt.Client("P1")
client.on_message=on_message
client.connect(broker_address)
client.loop_start()
client.subscribe("home/lights")
bleu = LED(18)

