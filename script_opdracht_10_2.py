#script_1002_blu_client

"""
opdracht 10.2 let op u moet ook blu_server draaien op een andere rpi wil dit werken

gemaakt door fabian boshoven
"""

import bluetooth
from gpiozero import LightSensor


serverMACAddress = 'noteer hier mac adress van server '
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
varSensor = LightSensor(18)
bericht = varSensor.value
s.send(bericht)
s.close()