import PySerial

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
        
    def read(self ):
        ser.write(request)
        sleep(.1)
        ser.read(bytecount)