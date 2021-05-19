#script_1002_blu_client
import bluetooth
serverMACAddress = 'noteer hier mac adress van server '
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
bericht = " test Bluetooth"
s.send(bericht)
s.close()