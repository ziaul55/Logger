# ref: https://www.raspberrypi.org/forums/viewtopic.php?t=235179#p1439574

import sys
import Adafruit_DHT


# DHT sensors arguments
models = { '11': Adafruit_DHT.DHT11,
           '22': Adafruit_DHT.DHT22,
           '2302': Adafruit_DHT.AM2302 
         }

def read(sensor, pin, measure='temperature'):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    # return statement
    measurement = None

    if measure == 'temperature':
        measurement = temperature
    elif measure == 'humidity': 
        measurement = humidity

    return measurement


if __name__ == '__main__':
    # get user provided arguments
    srcipt_arg = sys.argv[0]
    sensor_arg = sys.argv[1]
    pin_arg    = sys.argv[2]

    sensor = models[sensor_arg]
    pin    = pin_arg

    # readings
    #temperature = read(sensor, pin)
    temperature = read(sensor, pin, measure='temperature')
    humidity    = read(sensor, pin, measure='humidity')

    print('Temperature={:.1f}*C'.format(temperature))
    print('Humidity={:.1f}%'.format(humidity))
