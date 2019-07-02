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

    #招募返回数值 第一个为登录返回钻石 第二个为招募返回钻石
    def test_RecruitPlayer1(self):
        try:
            self.assertEqual(main.result[0].gameTeamInfoRespVo.diamond-1600,main.result[9].recruitClickRespVo.diamond)
            print("招募钻石正确")
        except Exception as e:
            print("用例执行失败原因:",main.result[9])
            raise e

    # 招募返回数值 获得兑换券
    def test_RecruitPlayer2(self):
        try:
            self.assertEqual(main.result[9].exchangeCard.propNum,10)
            self.assertEqual(main.result[9].exchangeCard.propId,1045)
            print("招募获得兑换券正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[9])
            raise e
     # 招募返回数值 获得球员
    def test_RecruitPlayer3(self):
        try:
            self.assertEqual(main.result[9].recruitClickRespVo.playerList[0].instance.tineng, 100)

            print("招募正确获得球员")
        except Exception as e:
            print("用例执行失败原因:", main.result[9])
            raise e
