# -*- coding: utf-8 -*-
"""
veron
This is a temporary script file.
"""

# ! /usr/bin/env python3.6

import socket
import time
from login import *
from  MyProtoco import  MyProtocol
import unittest
import HTMLTestRunner

HOST = '123.207.235.141'
PORT = 8080
result = bytes()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
d = [Proto().Login(),Proto().Get(),Proto().GetLevelPackageAward()]

for i in range(len(d)):
    s.send(d[i])
    r = s.recv(200000)
    result += r
    time.sleep(0.2)

b = MyProtocol()
b.init(result)
target =loginaward_pb2.GS2C_Get()
target.ParseFromString(b.databody[1])

s.send(Proto().ReceivePackage(target.activityPackage[0].id))
r = s.recv(200000)
result += r
time.sleep(0.2)
s.send(Proto().Login())
r = s.recv(200000)
result += r
time.sleep(0.2)

s.shutdown(socket.SHUT_RDWR)
s.close()

