# -*- coding: utf-8 -*-
from login import *
from client import  Client
from readExcel import  readExcel
import random
from sqlutil import sqlutil
import time


auth = ""
for i in range(0,7):
    current_code = random.randint(0,9)
    auth += str(current_code)

#excel=readExcel(r'./test.xlsx')
#data=excel.body
d = Proto()
d1 = [d.Login(), d.GetGuildInfo(), d.SearchGuild(), d.CreateGuild(1,auth, 0, 70, 5, "无敌"),
     d.EditTitle(2,20012,50,2,"123456"), d.GuildUplevel(), d.GuildDonationInfo(), d.DoDonation(3), d.GuildUptech(1),
     d.RecruitPlayer(), d.Mall_Buygoods(1,1,1,1,1),d.BuyVipPackage(), d.Signin(), d.AddSignIn(),d.Get(),d.GetLevelPackageAward(),
     d.PlayerUpgrade(), d.PlayerUpstar(),d.EquipUpLevel(),d.PlayerTrain(),d.UPT(),d.CSP(),d.SFB(),d.USFP(5),d.USFP(4),
     d.USFP(3),d.USFP(2),d.USFP(1),d.BSFP(5),d.BSFP(4),d.Mall_Buygoods(1,1,7,189,5),d.TakeRechargeRebateReward(153,260),
     d.ReceiveVipWelfare(),d.BuyQuizTicket(100),d.GetFacilities(),d.UpgradeFacilities(),d.UpgradeQuicklyFinish(),
     d.BuyCoin(),d.BuyTili(),d.BuyProp(),d.SwitchName(auth),d.Logout()]
t1 = [login_pb2.GS2C_Login(), guild_pb2.GS2C_GetGuildInfo(), guild_pb2.GS2C_SearchGuild(),
     guild_pb2.GS2C_CreateGuild(), guild_pb2.GS2C_EditTitle(), guild_pb2.GS2C_GuildUplevel(),
     guild_pb2.GS2C_GuildDonationInfo(), guild_pb2.GS2C_DoDonation(), guild_pb2.GS2C_GuildUptech(),
     recruit_pb2.GS2C_RecruitPlayer(), mall_pb2.GS2C_BuyGoods(),vip_pb2.GS2C_BuyVipPackage(), signin_pb2.GS2C_SignIn(),
     signin_pb2.GS2C_AddSignIn(),loginaward_pb2.GS2C_Get(), levelpackageaward_pb2.GS2C_GetLevelPackageAward(),
     player_pb2.GS2C_PlayerUpgrade(),player_pb2.GS2C_PlayerUpstar(),equipment_pb2.GS2C_EquipUpLevel(),player_pb2.GS2C_PlayerTrain(),
     player_pb2.GS2C_UpGradePlayerTracitUnderstanding(),springfestivalpreheat_pb2.GS2C_CompleteSpringFestivalTask(),
     springfestivalpreheat_pb2.GS2C_SpringFestivalBlessCombine(), springfestivalpreheat_pb2.GS2C_UnlockSpringFestivalPlayer(),
     springfestivalpreheat_pb2.GS2C_UnlockSpringFestivalPlayer(),springfestivalpreheat_pb2.GS2C_UnlockSpringFestivalPlayer(),
     springfestivalpreheat_pb2.GS2C_UnlockSpringFestivalPlayer(),springfestivalpreheat_pb2.GS2C_UnlockSpringFestivalPlayer(),
     springfestivalpreheat_pb2.GS2C_BuySpringFestivalPlayer(),springfestivalpreheat_pb2.GS2C_BuySpringFestivalPlayer(),
     mall_pb2.GS2C_BuyGoods(),activity_pb2.GS2C_TakeRechargeRebateReward(),vip_pb2.GS2C_ReceiveVipWelfare(),quiz_pb2.GS2C_BuyQuizTicket(),
     footballfacilities_pb2.GS2C_GetFacilities(), footballfacilities_pb2.GS2C_UpgradeFacilities(),footballfacilities_pb2.GS2C_UpgradeQuicklyFinish(),
     teaminfo_pb2.GS2C_BuyCoin(),manager_pb2.GS2C_BuyTili(),manager_pb2.GS2C_BuyProp(),manager_pb2.GS2C_SwitchName(),login_pb2.GS2C_Logout(),
     error_pb2.GS2C_ERRORCODE()]
result = Client().client(d1, t1, [])
