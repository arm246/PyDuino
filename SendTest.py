import serial
from time import sleep

to = 5
bytecount = 32

ser =   serial.Serial('COM4', 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout = to) # Establish the connection on a specific port

class Sensor:
    
    def __init__(self, name, arduino,pin):
        self.name = name
        self.arduino = arduino
        self.pin = pin
        
    def read(self,request ):
        ser.write(request)
        sleep(.1)
        message = ser.read(bytecount)
        print message
        
testSensor = Sensor("TestSensor", "Arduino1", 2)

while True:
    testSensor.read("Hello World")