# -*- coding: utf-8 -*-
"""
veron
This is a temporary script file.
"""

# ! /usr/bin/env python3.6

import socket
import  time
from  MyProtoco import  MyProtocol
import configparser

conf = configparser.ConfigParser()
conf.read("config.ini")
HOST=conf.get("HTTP","host")
PORT= int(conf.get("HTTP","port"))


class Client(object):

    def __init__(self):
        pass
    def client(self,data,t,target):
        self.data=data
        self.target=target
        self.t=t

       # global  result
        result = bytes()
        if self.target==[]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            for i in range(len(self.data)):
                s.send(self.data[i])
                r = s.recv(200000)
                result += r
                time.sleep(0.2)
            b = MyProtocol()
            b.init(result)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            time.sleep(0.2)
          #  return result

        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            for i in range(len(self.data)):
                s.send(self.data[i])
                r = s.recv(200000)
                result += r
                time.sleep(0.2)
            b = MyProtocol()
            b.init(result)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            time.sleep(0.2)

            self.t[-2].ParseFromString(b.databody[-1])
            s.send(self.target(self.t[-2].matchId))

        all = []
        for i in range(len(b.header)):
            if b.header[i]!=1:
                self.t[i].ParseFromString(b.databody[i])
                all.append(self.t[i])
            else:
                self.t[-1].ParseFromString(b.databody[i])
                all.append(self.t[-1].message)
        for i in range(len(all)):
            print ("第%s个数据包返回数据" % (i + 1), all[i])
            print("")

        return all

