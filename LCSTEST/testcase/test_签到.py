# -*- coding: utf-8 -*-
"""
veron
This is a temporary script file.
"""

# ! /usr/bin/env python3.6

from login import *
import  unittest
import  main

class MyTest(unittest.TestCase):#继承unittest.TestCase

    def setUp(self):
        print("正在建立初始化连接......")
        print("")

    def tearDown(self):
        print("")
        print(u"该条用例执行完毕,启动退出程序")

    #第一天签到获得1W欧元 VIP双倍
    def test_Signin(self):
        try:
            self.assertEquals(main.result[11].gameTeamInfo.coin+10000,main.result[12].teamInfoAndPropListRespVo.gameTeamInfo.coin)
        except Exception as e:
            print("用例执行失败原因:",main.result[12])
            raise e
    #补签获得80钻石
    def test_AddSignin(self):
        try:
            self.assertEquals(main.result[12].teamInfoAndPropListRespVo.gameTeamInfo.diamond + 80,main.result[13].teamInfoAndPropListRespVo.gameTeamInfo.diamond)
        except Exception as e:
            print("用例执行失败原因:",main.result[13])
            raise e



