# -*- coding: utf-8 -*-
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

    #购买赞助商
    def test_BuyCoin1(self):
        try:
            self.assertNotEqual(main.result[37].gameTeamInfo.coin,main.result[36].gameTeamInfo.coin)

            print("购买赞助商正确获得欧元")
        except Exception as e:
            print("用例执行失败原因:",main.result[37])
            raise e
    #购买赞助商
    def test_BuyCoin2(self):
        try:
            self.assertEqual(main.result[37].gameTeamInfo.diamond+50,main.result[36].gameTeamInfo.diamond)

            print("购买赞助商正确消耗钻石")
        except Exception as e:
            print("用例执行失败原因:",main.result[37])
            raise e
    #购买体力
    def test_BuyTili1(self):
        try:
            self.assertEqual(main.result[38].gameTeamInfo.tili,282)

            print("购买正确获得体力")
        except Exception as e:
            print("用例执行失败原因:",main.result[38])
            raise e
    #购买体力
    def test_BuyTili2(self):
        try:
            self.assertEqual(main.result[38].gameTeamInfo.diamond+50,main.result[37].gameTeamInfo.diamond)

            print("购买体力消耗钻石正确")
        except Exception as e:
            print("用例执行失败原因:",main.result[38])
            raise e
    #购买改名卡
    def test_BuyProp(self):
        try:
            self.assertEqual(main.result[39].diamond + 100, main.result[38].gameTeamInfo.diamond)

            print("购买改名卡成功")
        except Exception as e:
            print("用例执行失败原因:", main.result[39])
            raise e
    #改名
    def test_SwitchName(self):
        try:
            self.assertEqual(main.result[40].updateCode, 200)

            print("改名成功")
        except Exception as e:
            print("用例执行失败原因:", main.result[40])
            raise e