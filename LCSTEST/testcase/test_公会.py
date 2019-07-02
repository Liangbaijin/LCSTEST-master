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
    #创建公会
    def test_CreateGuild(self):
        try:
            self.assertEqual(main.result[3].guildBaseInfo.applyVip, 5)
            print("创建公会成功.")
        except Exception as e:
            print("用例执行失败原因:", main.result[7])
            raise e
    #修改公会
    def test_EditTitle(self):
        try:
            self.assertEqual(main.result[4].title, "123456")
            print("修改公会信息成功.")
        except Exception as e:
            print("用例执行失败原因:", main.result[7])
            raise e

    #公会捐赠
    def test_DoDonation(self):
        try:
            self.assertEqual(main.result[7].propRespVo.propNum,1500)
            print("公会捐赠成功.")
        except Exception as e:
            print("用例执行失败原因:",main.result[7])
            raise e
    #公会商城购买物品
    def test_Mall_Buygoods(self):
        try:
            self.assertEqual(main.result[30].teamInfoAndPropListRespVo.propRespVo[0].propId,1004)
            self.assertEqual(main.result[30].teamInfoAndPropListRespVo.propRespVo[0].propNum,1)
            print("公会商城购买获得道具正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[30])
            raise e

