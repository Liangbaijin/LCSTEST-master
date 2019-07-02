# -*- coding: utf-8 -*-
import struct

sn = 0
headerSize = 8
databody=[]
header=[]


class MyProtocol():
    _data_buffer = bytes()
    def init(self,data):
        self._data_buffer += data

        """Called whenever data is received."""

        while True :

            if len(self._data_buffer) < headerSize:
                return
            # 读取消息头部
            # struct中:!代表Network order，2I代表2个unsigned int数据
            headPack = struct.unpack('!iI', self._data_buffer[:headerSize])
            # 获取消息正文长度
            bodySize = headPack[0]

            # 分包情况处理
            if len(self._data_buffer) < headerSize+bodySize :
                return

            # 读取消息正文的内容
            body = self._data_buffer[headerSize:headerSize+bodySize]
            self.dataHandle(headPack, body)
            self._data_buffer =self._data_buffer[headerSize + bodySize:]

    def datahandle(self,databody,header):
        self.databody=databody
        self.header = header

    def dataHandle(self, headPack, body):
        self.headPack = headPack
        self.body = body
        global sn000000000

        sn += 1
        print("第%s个数据包" % sn)
        print("bodySize:%s, header:%s" % headPack)
        print(body)
        print("")
        if headPack[1] != 381 and headPack[1] != 606 and headPack[0]!=0:
            databody.append(body)
            header.append(headPack[1])
            self.datahandle(databody,header)

        else:
            pass


