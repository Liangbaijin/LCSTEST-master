# -*- coding: utf-8 -*-
import  unittest
import  main

class MyTest(unittest.TestCase):#继承unittest.TestCase

    def setUp(self):
        print("正在建立初始化连接......")
        print("")

    def tearDown(self):
        print("")
        print(u"该条用例执行完毕,启动退出程序")

    #球员升级
    def test_PlayerUpgrade(self):
        try:
            self.assertEqual(main.result[16].playerRespVo.instance.level,40)
            print("球员升级无误")
        except Exception as e:
            print("用例执行失败原因:",main.result[16])
            raise e
    #球员升星1:星级
    def test_PlayerUpstar1(self):
        try:
            self.assertEqual(main.result[17].playerRespVo.instance.star, 1)
            print("球员升星 星级无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[17])
            raise e

    # 球员升星2:道具消耗
    def test_PlayerUpstar2(self):
        try:
            self.assertEqual(main.result[17].property.num, 315)
            print("球员升星 道具消耗无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[17])
            raise e

    # 球员升星3:欧元消耗
    def test_PlayerUpstar3(self):
        try:
            self.assertEqual(main.result[17].coin+9000, main.result[13].teamInfoAndPropListRespVo.gameTeamInfo.coin)
            print("球员升星 欧元消耗无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[17])
            raise e
    #装备升级1:装备等级
    def test_EquipUpLevel1(self):
        try:
            self.assertEqual(main.result[18].equipmentRespVo.equipRespVo.level, 2)
            print("装备升级 等级无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[18])
            raise e
    # 装备升级2:装备扣除欧元
    def test_EquipUpLevel2(self):
        try:
            self.assertEqual(main.result[18].equipmentRespVo.gameTeamInfoRespVo.coin+75,main.result[17].coin )
            print("装备升级 扣除欧元无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[18])
            raise e

    #球员特训1：扣除道具
    def test_PlayerTrain1(self):
        try:
            self.assertEqual(main.result[19].gameProperty.num, 9994)
            print("球员特训 扣除道具无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[19])
            raise e

    # 球员特训2：特训数值
    def test_PlayerTrain2(self):
        try:
            self.assertEqual(main.result[19].instance.attr.shemen-2, main.result[17].playerRespVo.attr.shemen)
            print("球员特训 特训数值无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[19])
            raise e
    #默契升级1:默契等级
    def test_UPT1(self):
        try:
            self.assertEqual(main.result[20].totalTacitLevel,2)
            print("球员默契升级无误")
        except Exception as e:
            print("用例执行失败原因:", main.result[20])
            raise e
    #默契升级2：道具消耗
    def test_UPT2(self):
        try:
            self.assertEqual(main.result[20].propRespVo[0].propNum, 9997)
            print("球员默契升级道具消耗无误")
        except Exception as e:
            print("用例执行失败原因:",main.result[20])
            raise e


