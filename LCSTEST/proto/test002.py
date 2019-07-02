# -*- coding: utf-8 -*-

from login import *
from client import  Client
from readExcel import  readExcel
import random
from  MyProtoco import  MyProtocol

a=0x0007 & 0x3fffffff
auth = ""
for i in range(0,7):
    current_code = random.randint(0,9)
    auth += str(current_code)

excel=readExcel(r'C:\Users\admin\PycharmProjects\LEA\LCS\proto\test.xlsx')
data=excel.body
d = Proto()
d = [d.Login(),d.Logout()]
t = [login_pb2.GS2C_Login(),
     login_pb2.GS2C_Logout(), error_pb2.GS2C_ERRORCODE()]
result = Client().client(d, t, [])
b = MyProtocol()
b.init(result)
c=b.header.index(a)
print (b.databody[c])


