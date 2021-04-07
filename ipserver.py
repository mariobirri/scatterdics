#!/usr/bin/env python

import socket
from pcaspy import Driver, SimpleServer

prefix = 'X05LA-ES-SCATTERDISC:ROT.'
pvdb = {
    'IP' : {
        'type' : 'str',
    },
}


class myDriver(Driver):
    def  __init__(self):
        super(myDriver, self).__init__()
        ip = socket.gethostbyname(socket.gethostname())
        self.setParam('IP', ip)


if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = myDriver()

    # process CA transactions
    while True:
        server.process(0.1)
