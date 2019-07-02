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

    #进入球场
    def test_GetFacilities(self):
        try:
            self.assertEqual(main.result[34].facilities[0].level,0)

            print("正确进入球场界面")
        except Exception as e:
            print("用例执行失败原因:",main.result[34])
            raise e
    #升级球场
    def test_UpgradeFacilities1(self):
        try:
            self.assertEqual(main.result[35].facility.upgradeEndTime, 600)

            print("正确升级球场")
        except Exception as e:
            print("用例执行失败原因:", main.result[35])
            raise e
    # 升级球场消耗
    def test_UpgradeFacilities2(self):
        try:
            self.assertEqual(main.result[35].gameTeamInfo.coin+100000, main.result[33].gameTeamInfo.coin)

            print("升级球场消耗欧元正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[35])
            raise e
    #快速升级球场
    def test_UpgradeQuicklyFinish1(self):
        try:
            self.assertEqual(main.result[36].facility.upgradeEndTime, 0)
            self.assertEqual(main.result[36].facility.level, 1)
            self.assertEqual(main.result[36].facility.type, 1)
            print("正确升级球场")
        except Exception as e:
            print("用例执行失败原因:", main.result[36])
            raise e
    #快速升级球场消耗正确
    def test_UpgradeQuicklyFinish2(self):
        try:
            self.assertEqual(main.result[36].gameTeamInfo.diamond+100,main.result[35].gameTeamInfo.diamond )

            print("快速升级球场消耗正确")
        except Exception as e:
            print("用例执行失败原因:", main.result[36])
            raise e