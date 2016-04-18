import PySerial
import Sensor
import Effector

to = 5
bytecount = 32

ser =   serial.Serial('COM4', 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout = to) # Establish the connection on a specific port

class Golgi:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        
        self.connect(ip, port)


