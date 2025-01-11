#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge
import io
import random
import re
import signal
import socket
import sys
import fcntl
import time
import copy
import string
from AtlasI2C import (
  AtlasI2C
)

PH_SENSOR_INDEX = 0

def get_float(text):
    # match = re.search(r"[-+]?\d*\.\d+", text)
    match = re.search(r"Success.*(\d+\.\d+)", text)
    if match:
        float_value = float(match.group(1))
        return float_value

def get_devices():
    device = AtlasI2C()
    device_address_list = device.list_i2c_devices()
    device_list = []
    
    for i in device_address_list:
        device.set_i2c_address(i)
        response = device.query("I")
        try:
            moduletype = response.split(",")[1] 
            response = device.query("name,?").split(",")[1]
        except IndexError:
            print(">> WARNING: device at I2C address " + str(i) + " has not been identified as an EZO device, and will not be queried") 
            continue
        device_list.append(AtlasI2C(address = i, moduletype = moduletype, name = response))
    return device_list 
       
def read_sensor_at(index):
    delaytime = 1.5 # seconds
    device_list = get_devices()
    device_list[index].write("R")
    time.sleep(delaytime)
    return get_float(device_list[index].read())

def read_sensor_at_random(lower_range=1, upper_range=10):
    return random.randint(lower_range, upper_range)

def get_ph():
    return read_sensor_at(PH_SENSOR_INDEX)

def get_temperature_f():
    return read_sensor_at_random(50,80)

def get_dissolved_oxygen_f():
    return read_sensor_at_random(0,10)

def register_prometheus_gauges():
    PH = Gauge(
        'ph',
        'pH reading from Atlas Scientific',
        ["id"]
    )
    PH.labels(str("Atlas Scientific ph")).set_function(get_ph)

    TEMP_F = Gauge(
        'temperature',
        'temperature reading from Atlas Scientific',
        ["id", "unit"]
    )
    TEMP_F.labels(id='Atlas Scientific temp', unit='fahrenheit').set_function(get_temperature_f)

    TEMP_F = Gauge(
        'dissolved oxygen',
        'dissolved oxygen reading from Atlas Scientific',
        ["id", "unit"]
    )
    TEMP_F.labels(id='Atlas Scientific DO', unit='mg/L').set_function(get_dissolved_oxygen_f)
  
if __name__ == "__main__":
    start_http_server(5000)
    register_prometheus_gauges()
    while True:
        time.sleep(10000)
