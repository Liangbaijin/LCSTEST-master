# -*- coding: utf-8 -*-
from login import *
import unittest
import  main


class MyTest(unittest.TestCase):#继承unittest.TestCase

    def setUp(self):
        print("正在建立初始化连接......")
        print("")

    def tearDown(self):
        print("")
        print(u"该条用例执行完毕,启动退出程序")

    #春节活动：领取礼包
    def test_CSP(self):
        try:
            self.assertEqual(main.result[21].propRespVo[0].propId,1078)
            self.assertEqual(main.result[21].propRespVo[0].propNum, 5)
            print("正确获得春节礼包1")
        except Exception as e:
            print("用例执行失败原因:",main.result[21])
            raise e
    #春节活动：合成祝福
    def test_SFB1(self):
        try:
            self.assertEqual(main.result[22].propRespVo.propId,1083)
            self.assertEqual(main.result[22].propRespVo.propNum, 1)
            print("正确合成祝福")
        except Exception as e:
            print("用例执行失败原因:",main.result[22])
            raise e
    #春节活动：合成祝福道具消耗
    def test_SFB2(self):
        try:
            self.assertEqual(main.result[22].gameProperty[0].num,10002)

            print("合成祝福消耗道具正确")
        except Exception as e:
            print("用例执行失败原因:",main.result[22])
            raise e
    # 春节活动：解锁球员
    def test_USFP(self):
        try:
            self.assertEqual(main.result[23].gameProperty[2].num, 9997)

            print("解锁球员消耗球员祝福正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[23])
            raise e
    # 春节活动：获得第一个免费球员
    def test_BSFP1(self):
        try:
            self.assertEqual(main.result[28].propRespVo.gamePlayerInstance.instance.commonPlayerId, 10001269)

            print("正确获得第一个春节球员")
        except Exception as e:
            print("用例执行失败原因:", main.result[28])
            raise e
    # 春节活动：获得第二个球员
    def test_BSFP2(self):
        try:
            self.assertEqual(main.result[29].propRespVo.gamePlayerInstance.instance.commonPlayerId, 10001270)

            print("正确获得第二个春节球员")
        except Exception as e:
            print("用例执行失败原因:", main.result[29])
            raise e
    # 春节活动：购买第二个球员 消耗钻石正确
    def test_BSFP3(self):
        try:
            self.assertEqual(main.result[29].gameTeamInfo.diamond+1500,main.result[21].gameTeamInfo.diamond)

            print("正确消耗1500钻石获得第二个春节球员")
        except Exception as e:
            print("用例执行失败原因:", main.result[29])
            raise e