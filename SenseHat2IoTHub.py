#!/usr/bin/python 

import time
import iothub_client
import json
from time import sleep
from iothub_client import *
from sense_hat import SenseHat
from Utility import Utility

senseHat = SenseHat()

os = 'Raspbian'
deviceModel = 'Raspberry Pi 3'

deviceID = 'LZY-P-301'
hostName = Utility.GetIoTHubHostName()
sharedAccessKey = Utility.GetIoTHubSharedAccessKeyValue

connectionString = 'HostName=%s;DeviceId=%s;SharedAccessKey=%s' % (hostName, deviceID, sharedAccessKey)
protocol = IoTHubTransportProvider.HTTP

deviceClient = IoTHubClient(connectionString, protocol)

def send_confirmation_callback(message, result, user_context):
    return

for i in range(0, 450):
    temperature = senseHat.get_temperature()
    humidity = senseHat.get_humidity()
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    
    messageString = "{\"DeviceID\":\"LZY-R-301\", \"Temperature\":%f, \"Humidity\":%f, \"Time\":\"%s\", \"OS\":\"%s\", \"DeviceModel\":\"%s\"}" % (temperature, humidity, currentTime, os, deviceModel)
     
    message = IoTHubMessage(messageString)
    
    deviceClient.send_event_async(message, send_confirmation_callback, i)
    
    print('sending data: %s, %s' % (i, messageString))

    sleep(2)

print('---the end---')