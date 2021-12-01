import adafruit_dht as dht
import time
from board import D4
sensor = dht.DHT22(D4)

while True:
    if sensor.humidity is not None and sensor.temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(sensor.temperature, sensor.humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(5)
