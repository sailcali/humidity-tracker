import adafruit_dht as dht
import time
from board import D4
sensor = dht.DHT22(D4)

while True:
    print(sensor.humidity)
    quit()
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(5)
