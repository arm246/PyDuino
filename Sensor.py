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