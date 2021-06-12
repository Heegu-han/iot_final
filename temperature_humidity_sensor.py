import Adafruit_DHT
import time
import urllib.request
import datetime

try:
    while True:
        h,t=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
        ctm = datetime.datetime.now().strftime("%y-m%m-%d-%H%M%S")
        if h is not None and t is not None:
            urllib.request.urlopen(f'http://54.180.124.122:5000/temp_hum?tm={ctm},temp={t}&hum={h}')
        else:
            print("Read error")

        time.sleep(1)

except KeyboardInterrupt:
    print("Terminated by Keyboard")
finally:
    print("End of Program")
