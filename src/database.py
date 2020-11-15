# ref: https://www.youtube.com/watch?v=O20Y1XR6g0A&list=PLoVvAgF6geYMb029jpxqMuz5dRDtO0ydM&index=4


import os
from influxdb import InfluxDBClient


# InfluxDB credentials
HOST     = os.environ.get('INFLUXDB_HOST', 'localhost')
PORT     = os.environ.get('INFLUXDB_PORT', 8086)
USERNAME = os.environ.get('INFLUXDB_USER', 'admin')
PASSWORD = os.environ.get('INFLUXDB_USER_PASSWORD', 'admin')
DATABASE = os.environ.get('INFLUXDB_DB', 'strawberry_factory')


def client():
    # InfluxDB client setup
    client = InfluxDBClient(host=HOST, port=int(PORT), username=USERNAME, password=PASSWORD)

    # databases
    #client.get_list_database()

    # create a database
    client.create_database(DATABASE)

    # use a database
    client.switch_database(DATABASE)

    # measurements/tables
    #client.get_list_measurements()

    return client

def save(db_client, measurement, fields, tags=None):
    # json data
    """
    json_body = {}
    json_body['measurement'] = measurement
    
    if tags != None:
        json_body['tags'] = tags

    json_body['fields'] = fields

    # make list
    json_body = [json_body]
    """

    # alternatively
    json_body = [{'measurement': measurement, 'tags': tags, 'fields': fields}]

    # write / save into a row
    db_client.write_points(json_body)
