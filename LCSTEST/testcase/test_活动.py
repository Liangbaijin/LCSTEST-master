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

    #等级礼包
    def test_levelpackageaward(self):
        try:
            self.assertEqual(main.result[15].propRespVo[1].propId,1005)
            self.assertEqual(main.result[15].propRespVo[1].propNum, 10)
            print("正确获得等级礼包")
        except Exception as e:
            print("用例执行失败原因:",main.result[15])
            raise e
    #消耗返利
    def test_TakeRechargeRebateReward(self):
        try:
            self.assertEqual(main.result[31].gameTeamInfo.level,100)

            print("消耗返利正确获得礼包")
        except Exception as e:
            print("用例执行失败原因:",main.result[31])
            raise e
    #VIP福利
    def test_ReceiveVipWelfare(self):
        try:
            self.assertEqual(main.result[32].propRespVoList[0].propId, 1002)
            self.assertEqual(main.result[32].propRespVoList[0].propNum,5000)
            print("正确获得VIP福利礼包")
        except Exception as e:
            print("用例执行失败原因:", main.result[32])
            raise e
    #竞猜 购买彩票
    def test_BuyQuizTicket1(self):
        try:
            self.assertEqual(main.result[33].propResp.propId, 1065)
            self.assertEqual(main.result[33].propResp.propNum, 100)
            print("购买彩票成功")
        except Exception as e:
            print("用例执行失败原因:", main.result[33])
            raise e
    # 竞猜 购买彩票扣钻
    def test_BuyQuizTicket2(self):
        try:
            self.assertEqual(main.result[33].gameTeamInfo.diamond+100, main.result[31].gameTeamInfo.diamond)

            print("购买彩票扣除钻石正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[33])
            raise e


