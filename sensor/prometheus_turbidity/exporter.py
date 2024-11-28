#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge
import io
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

def get_float(text):
    match = re.search(r"[-+]?\d*\.\d+", text)
    if match:
        float_value = float(match.group())
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
       
def get_ph():
    delaytime = 1.5 # seconds
    device_list = get_devices()
    last_value_of_first_device = 0
    for dev in device_list:
        dev.write("R")
    time.sleep(delaytime)
    for dev in device_list:
        last_value_of_first_device = get_float(dev.read())
        break
    return last_value_of_first_device

def register_prometheus_gauges():
    PH = Gauge(
        'ph',
        'pH reading from Atlas Scientific',
        ["Sensor_ID"]
    )
    PH.labels(str("Atlas Scientific #1")).set_function(get_ph)

if __name__ == "__main__":
    start_http_server(5000)
    register_prometheus_gauges()
    while True:
        time.sleep(10000)
