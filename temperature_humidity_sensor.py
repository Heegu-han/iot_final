import Adafruit_DHT
import time

try:
    while True:
        h,t=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)

        if h is not None and t is not None:
            print(f"Temperature = {t}*C Humidity = {h}%")
        else:
            print("Read error")

        time.sleep(1)

except KeyboardInterrupt:
    print("Terminated by Keyboard")
finally:
    print("End of Program")
