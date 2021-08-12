#!/usr/bin/env python

import serial, time                           #import libraries
from pcaspy import Driver, SimpleServer
ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=5)    #open serial port for communication with Ar-duino

prefix = 'X05LA-ES-SCATTERDISC:ROT.'
pvdb = {
    'VAL' : {
    'TYPE': 'int'
    },'RBV': {
    'TYPE':'float'
    },
}

class myDriver(Driver):
    def  __init__(self):
        super(myDriver, self).__init__()

    def write(self, reason, speedval):
        status = True

        if reason == 'VAL':                      #if EPICS input VAL
           print ('new speed is'); print (speedval)        #print to Arduino current speed
           x = str((speedval+0.2)*60)                #calculation for rps with offset
           ser.write (x)                        #send value for speed to Arduino

        if status:
           self.setParam(reason, speedval)

        return status

    def read(self, reason):
        if reason == 'RBV':                        #if EPICS input RBV (in progress)
            ser.write("speed")
            time.sleep(0.01)
            value=float(ser.readline())
            self.setParam(reason, value)
            print ('speed is '); print (value)
        else:
            value = self.getParam(reason)
        return value


if __name__ == '__main__':                    #create PVs based on prefix and pvdb definition
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = myDriver()

    while True:
        server.process(0.1)                    # process CA transactions

