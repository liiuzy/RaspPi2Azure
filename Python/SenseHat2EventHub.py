#!/usr/bin/python 

from time import sleep
import json
import time
from azure.servicebus import ServiceBusService
from sense_hat import SenseHat
from Utility import Utility

senseHat = SenseHat()

sharedAccessKeyName = Utility.GetEventHubSharedAccessKeyName()
sharedAccessKeyVaule = Utility.GetEventHubSharedAccessKeyValue()
eventHubNamespace = Utility.GetEventHubNamespace()
hubName = 'IoT-001'

deviceID = 'LZY-R-301'
os = 'Raspbian' 
deviceModel = 'Raspberry Pi 3'

serviceBusService = ServiceBusService(eventHubNamespace, shared_access_key_name=sharedAccessKeyName, shared_access_key_value=sharedAccessKeyVaule)

for i in range(0, 450):
    temperature = senseHat.get_temperature()
    humidity = senseHat.get_humidity()
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    #tempJson = {'DeviceID':'LZY-R-301', 'Temperature':temperature, 'Humidity':humidity, 'Time':currentTime, 'Device':'Raspberry Pi 3', 'OS':'Raspbian'}
    tempJson = {'DeviceID':deviceID, 'Temperature':temperature, 'Humidity':humidity, 'Time':currentTime, 'DeviceModel':deviceModel, 'OS':os}

    serviceBusService.send_event(hubName, tempJson)

    sleep(2)

print('---the end---')
