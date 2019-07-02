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


    #购买商城返回数值  第二个为购买商品后返回数值
    def test_Mall_Buygoods1(self):
        try:
            self.assertEqual(main.result[9].recruitClickRespVo.diamond-10,main.result[10].teamInfoAndPropListRespVo.gameTeamInfo.diamond)
            print("商城购买消耗钻石正确")
        except Exception as e:
            print("用例执行失败原因:",main.result[10])
            raise e

    # 购买商城返回数值  第二个为购买商品后返回数值
    def test_Mall_Buygoods2(self):
        try:
            self.assertEqual(main.result[10].teamInfoAndPropListRespVo.propRespVo[0].propId,1004)
            self.assertEqual(main.result[10].teamInfoAndPropListRespVo.propRespVo[0].propNum,1)
            print("商城购买获得道具正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[10])
            raise e

    #VIP礼包购买  888钻
    def test_BuyVipPackage1(self):
        try:
            self.assertEqual(main.result[10].teamInfoAndPropListRespVo.gameTeamInfo.diamond - 888,
                             main.result[11].gameTeamInfo.diamond)
            print("VIP礼包扣除钻石正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[11])
            raise e

    # VIP礼包购买  道具
    def test_BuyVipPackage2(self):
        try:
            self.assertEqual(main.result[11].propRespVoList[1].propId,1002)
            self.assertEqual(main.result[11].propRespVoList[1].propNum,200000)
            print("VIP礼包获得礼包正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[11])
            raise e
