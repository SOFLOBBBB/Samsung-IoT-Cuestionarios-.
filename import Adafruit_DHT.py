import Adafruit_DHT
import time

print("Ingresando a while")

try:
    while True:
        sensor = Adafruit_DHT.DHT11
        pin = 20
        
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        
        print("Humedad: ", humedad)
        print("Temperatura: ", temperatura)
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Saliendo de while")