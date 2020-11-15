# ref: https://www.youtube.com/watch?v=O20Y1XR6g0A&list=PLoVvAgF6geYMb029jpxqMuz5dRDtO0ydM&index=4


import os
from time import sleep

from database import client, save
from adafruit_dht import read


# waiting time (in second) to send next data to be input
SLEEP = int(os.environ.get('SLEEP_TIME', 5))

# measurements/tables
TEMPERATURE = 'temperature'
HUMIDITY    = 'humidity'

# tags/indices
ROOM1  = 'room1'
ROOM2  = 'room2'
ROOM3  = 'room3'
GARDEN = 'garden'

# fields/columns
VALUE = 'value'


# a writable json object as measurement
"""
temperature = [
    {
        "measurement": TEMPERATURE,
        "tags": {
            "place": ROOM1
        },
        "fields": {
            "value": 23.1
        }
    }
]

measurement = TEMPERATURE
tags        = { "place": ROOM1 }
fields      = { "value": 23.1 }
"""


if __name__ == '__main__':

    while True:

        # InfluxDB server
        db_client = client()

        # dht settings
        model = int(os.environ.get('DHT_MODEL', 22))
        pin   = int(os.environ.get('DHT_PIN', 23)) 
 
        # dht sensor data
        temperature = read(model, pin, measure='temperature')
        humidity    = read(model, pin, measure='humidity')

        # take 1 decimal point
        temperature = float("{:.1f}".format(temperature))
        humidity    = float("{:.1f}".format(humidity))

        # json body for temperature
        t_measurement = TEMPERATURE
        t_tags        = { "place": ROOM1 }
        t_fields      = { "value" :  temperature}

        # json body for humidity
        h_measurement = HUMIDITY
        h_tags        = { "place": ROOM1 }
        h_fields      = { "value" :  humidity}

        # save
        #save(db_client, measurement, fields)
        #save(db_client, measurement, fields, tags=None)
        save(db_client, t_measurement, t_fields, tags=t_tags)
        save(db_client, h_measurement, h_fields, tags=h_tags)

        # wait for few moment
        sleep(SLEEP)
