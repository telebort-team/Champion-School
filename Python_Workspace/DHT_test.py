import Adafruit_DHT as dht

humidity, temperature = dht.read_retry(dht.DHT22, 18)
print('Temperature = {0:0.1f} *C'.format(temperature))
print('Humidity = {0:0.1f} %'.format(humidity))