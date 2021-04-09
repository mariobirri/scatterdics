#!/usr/bin/env python

#import libraries
import socket
from pcaspy import Driver, SimpleServer
from megapi import *

#global variable of the encoder speed [rps]
rps = 0.0

def megaPiOnRead(value):
	global rps
        rps = float(value)/60
        #print("Encoder motor speed Value:%f" %rps);

prefix = 'X05LA-ES-SCATTERDISC:ROT.'
pvdb = {
    	'VAL' : { 'TYPE' : 'int' },
	'RBV' : { 'TYPE' : 'float' , 'scan' : 0.1 },
	'IP'  : { 'TYPE' : 'char', 'scan' : 10, 'count' : 15 }
	#'IP'  : { 'TYPE' : 'string', 'scan' : 1 }
}


class myDriver(Driver):
    def  __init__(self):
        super(myDriver, self).__init__()
	#ip = socket.gethostbyname(socket.gethostname())
        #self.setParam('IP', ip)

    def write(self, reason, speedval):
        global mot
	status = True

        if reason == 'VAL':  					#if EPICS input VAL
           print ('new speed is'); print (speedval)		#print to Arduino current speed
           mot.encoderMotorRun(1,speedval*60);				#calculation for rps with offset

        if status:
           self.setParam(reason, speedval)

        return status

    def read(self, reason):
	global mot, rps
	if reason == 'RBV':
		mot.encoderMotorSpeed(1,megaPiOnRead)						#if EPICS input RBV (in progress)
   		value=float(rps) #float(mot.encoderMotorSpeed(1,megaPiOnRead))
   		print ('speed is '); print (value)
	elif reason == 'IP':
		value = socket.gethostbyname(socket.gethostname())
		print(value)
	else:
   		value = self.getParam(reason)

	self.setParam(reason, value)
	return value


if __name__ == '__main__':					#create PVs based on prefix and pvdb definition
	global mot
	mot = MegaPi()
	mot.start()

	server = SimpleServer()
    	server.createPV(prefix, pvdb)
    	driver = myDriver()

	while True:
        	server.process(0.1)					# process CA transactions

