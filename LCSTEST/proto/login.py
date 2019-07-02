# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

# ! /usr/bin/env python3.6
import struct
import login_pb2,story_pb2,recruit_pb2,mall_pb2,vip_pb2,signin_pb2,levelpackageaward_pb2,loginaward_pb2,\
    match_pb2,error_pb2,player_pb2,equipment_pb2,guild_pb2,springfestivalpreheat_pb2,activity_pb2,quiz_pb2,friends_pb2,\
    footballfacilities_pb2,teaminfo_pb2,manager_pb2
from GZIP import  Gzip
import time
import requests
import configparser
from sqlutil import sqlutil

conf = configparser.ConfigParser()
conf.read("config.ini")
body=bytes()
uid=conf.getint("uid","uid")
r  = requests.get('http://test.account.91fifa.com:81/checkToken?uid=%s'%(uid))
token=r.json()[ 'token']

sql=sqlutil()
sql.update_teaminfo()
sql.insert_prop()
playerId=sql.query_playerId()
equipId=sql.query_equipId()
sql.set_player_instance()


class Proto(object):
    def __init__(self):
        pass

    def datahandle(self,serial,header):
        self.serial=serial
        self.header=header
        serial=self.serial.SerializeToString()
        G_data = Gzip.gzip_compress(serial)
        data_header = struct.pack('!iI', len(G_data), self.header)
        body = data_header + G_data
        self.dataHandle(body)

    def dataHandle(self, body):
        self.body = body

   # 登录接口#
    def Login(self):
        G = login_pb2.C2GS_Login()
        G.channel=0
        G.deviceId="c6fc18bbcac85899658c6c813bb18dfe"
        G.deviceType="Xiaomi Redmi 5"
        G.md5="d68b539ea8a1071b9237d1fa38405815"
        G.token=token
        G.uid="1-%d" %(uid)
        G.imei="863252031867123"
        header= 0x80000000 | 0x0006
        self.datahandle(G,header)
        return self.body

    #登出接口
    def Logout(self):
        G=login_pb2.C2GS_Logout()
        header= 0x80000000 | 0x0013E
        self.datahandle(G, header)
        return self.body

   #生涯接口#
    def story(self):
        G = story_pb2.C2GS_Challenge()
        G.id = 1
        header = 0x80000000 | 0x009D
        self.datahandle(G, header)
        return self.body

    def PushFlow(self,matchId):
        self.matchId=matchId
        G=match_pb2.C2GS_PushFlow()
        G.matchType=204
        G.uid="1-%d" %(uid)
        G.matchId=matchId
        header = 0x80000000 | 0x0015E
        self.datahandle(G,header)
        return self.body

    #球员招募
    def RecruitPlayer(self):
        G = recruit_pb2.C2GS_RecruitPlayer()
        G.count = 1
        G.id = 2
        G.type = 2
        header = 0x80000000 | 0x001D
        self.datahandle(G, header)
        return self.body

   # 商城购买
    def Mall_Buygoods(self,field,goodsNum,mallId,goodsId,mallType):
        G = mall_pb2.C2GS_BuyGoods()
        G.field = field
        G.goodsNum = goodsNum
        G.mallId = mallId
        G.goodsId = goodsId
        G.mallType = mallType
        header = 0x80000000 | 0x00ED
        self.datahandle(G, header)
        return self.body

    #vip礼包购买
    def BuyVipPackage(self):
        G = vip_pb2.C2GS_BuyVipPackage()
        G.id = 136
        header = 0x80000000 | 0x00144
        self.datahandle(G, header)
        return self.body

    #签到
    def Signin(self):
        G=signin_pb2.C2GS_SignIn()
        header = 0x80000000 | 0x00B5
        self.datahandle(G, header)
        return self.body

    #补签
    def AddSignIn(self):
        G=signin_pb2.C2GS_AddSignIn()
        header = 0x80000000 | 0x00B7
        self.datahandle(G, header)
        return self.body

    #get 活动
    def Get(self):
        G=loginaward_pb2.C2GS_Get()
        header= 0x80000000 | 0x00C7
        self.datahandle(G,header)
        return self.body

    #活动：等级礼包
    def GetLevelPackageAward(self):
        G=levelpackageaward_pb2.C2GS_GetLevelPackageAward()
        G.awardId=159
        header = 0x80000000 | 0x0017E
        self.datahandle(G, header)
        return self.body

    #活动：登录奖励
    def ReceivePackage(self,awardId):
        self.awardId=awardId
        G=loginaward_pb2.C2GS_ReceivePackage()
        G.awardId=awardId
        header=0x80000000 | 0x00C9
        self.datahandle(G, header)
        return self.body

    #球员升级
    def PlayerUpgrade(self):

        G=player_pb2.C2GS_PlayerUpgrade()
        G.playerId=playerId
        mydata1=G.propertyList.add()
        mydata1.num=1
        mydata1.propertyId=1003
        mydata2 = G.propertyList.add()
        mydata2.num = 1
        mydata2.propertyId = 1004
    # propertyListList=[{"num":1,"propertyId":1003},{"num":0,"propertyId":1004},{"num":0,"propertyId":1005},{"num":0,"propertyId":1006}]
        header=0x80000000 | 0x000F
        self.datahandle(G, header)
        return self.body

    #球员升星
    def PlayerUpstar(self):
        G=player_pb2.C2GS_PlayerUpstar()
        G.playerId=playerId
        header = 0x80000000 | 0x0011
        self.datahandle(G, header)
        return self.body

    #球员强化
    def PlayerGradation(self):
        G=player_pb2.C2GS_PlayerGradation()
        G.playerId=playerId
        G.itemUse=False
        G.consumePlayerIds.append(104160)
        G.consumePlayerIds.append(104159)
        header = 0x80000000 | 0x0018D
        self.datahandle(G, header)
        return self.body
    #默契升级
    def UPT(self):
        G=player_pb2.C2GS_UpGradePlayerTracitUnderstanding()
        G.playerId=playerId
        G.type=1
        mydata = G.propRespVo.add()
        mydata.propId=1031
        mydata.propNum=2
        mydata.propType=5
        header = 0x80000000 | 0x00D7
        self.datahandle(G, header)
        return self.body

    #装备强化
    def EquipUpLevel(self):
        G=equipment_pb2.C2GS_EquipUpLevel()
        G.equipId=equipId
        G.upLevel=1
        G.playerId=0
        header = 0x80000000 | 0x001F
        self.datahandle(G, header)
        return self.body

    #公会：获取公会信息
    def GetGuildInfo(self):
        G=guild_pb2.C2GS_GetGuildInfo()
        header = 0x80000000 | 0x0026F
        self.datahandle(G, header)
        return self.body

    #刷新公会列表
    def SearchGuild(self):
        G=guild_pb2.C2GS_SearchGuild()
        G.key=""
        header = 0x80000000 | 0x00271
        self.datahandle(G, header)
        return self.body

    #申请加入公会
    def ApplyToJoinGuild(self):
        G=guild_pb2.C2GS_ApplyToJoinGuild()
        mydata1 = G.guildIdList.add()
        mydata1.guildIdListList=1000019
        header = 0x80000000 | 0x00273
        self.datahandle(G, header)
        return self.body

    #退出公会
    def ExitGuild(self):
        G=guild_pb2.C2GS_ExitGuild()
        header = 0x80000000 | 0x00275
        self.datahandle(G, header)
        return self.body

    #创建公会
    def CreateGuild(self,label,name,club,level,vip,title):
        G=guild_pb2.C2GS_CreateGuild()
        G.label=label
        G.name=name
        G.applyClub=club
        G.applyLevel=level
        G.applyVip=vip
        G.title=title
        header = 0x80000000 | 0x00277
        self.datahandle(G, header)
        return self.body

    #修改公会信息
    def EditTitle(self,label,club,level,vip,title):
        G=guild_pb2.C2GS_EditTitle()
        G.title=title
        G.applyClub=club
        G.applyLevel=level
        G.applyVip=vip
        G.label=label
        header = 0x80000000 | 0x00279
        self.datahandle(G, header)
        return self.body

    #公会升级
    def GuildUplevel(self):
        G=guild_pb2.C2GS_GuildUplevel()
        header = 0x80000000 | 0x0027B
        self.datahandle(G, header)
        return self.body

    #获取用户列表
    def GetGuildMemberInfo(self,i):
        G=guild_pb2.C2GS_GetGuildMemberInfo()
       #i=1
        G.type=i
        header = 0x80000000 | 0x0027D
        self.datahandle(G, header)
        return self.body

    #会员管理
    def ManagerMember(self,i):
        G=guild_pb2.C2GS_ManagerMember()
        G.uid="1-%d" %(uid)
        #i=2
        G.type=i
        header = 0x80000000 | 0x0027F
        self.datahandle(G, header)
        return self.body

    #进入公会捐赠页面
    def GuildDonationInfo(self):
        G=guild_pb2.C2GS_GuildDonationInfo()
        header = 0x80000000 | 0x00281
        self.datahandle(G, header)
        return self.body

    #进行捐赠
    def DoDonation(self,i):
        G=guild_pb2.C2GS_DoDonation()
        #i=3
        G.donationType=i

        header = 0x80000000 | 0x00283
        self.datahandle(G, header)
        return self.body

    #领取每日总贡献礼包
    def ReceiveGuildDailyPackage(self,i):
        G=guild_pb2.C2GS_ReceiveGuildDailyPackage()
        #i=1
        G.id=i
        header = 0x80000000 | 0x00285
        self.datahandle(G, header)
        return self.body

    #公会建设-科技升级
    def GuildUptech(self,i):
        G=guild_pb2.C2GS_GuildUptech()
        #i=1
        G.type=i
        header = 0x80000000 | 0x00287
        self.datahandle(G, header)
        return self.body

    #球员特训
    def PlayerTrain(self):
        G=player_pb2.C2GS_PlayerTrain()
        G.playerId=playerId
        G.attrId=1
        G.type=2
        header=0x80000000 | 0x002CD
        self.datahandle(G, header)
        return self.body
    #春节活动：CompleteSpringFestivalTask 领取
    def CSP(self):
        G=springfestivalpreheat_pb2.C2GS_CompleteSpringFestivalTask()
        G.taskId=1
        header = 0x80000000 | 0x002E0
        self.datahandle(G, header)
        return self.body
    #春节活动：SpringFestivalBlessCombine 合成祝福
    def SFB(self):
        G=springfestivalpreheat_pb2.C2GS_SpringFestivalBlessCombine()
        G.cloth=2
        G.shoes=2
        G.trousers=2
        header = 0x80000000 | 0x002DE
        self.datahandle(G, header)
        return self.body
    #春节活动：UnlockSpringFestivalPlayer 解锁球员
    def USFP(self,i):
        G=springfestivalpreheat_pb2.C2GS_UnlockSpringFestivalPlayer()
        G.rewardId=i
        header = 0x80000000 | 0x002E2
        self.datahandle(G, header)
        return self.body

    # 春节活动：BuySpringFestivalPlaye 购买球员
    def BSFP(self,i):
        G = springfestivalpreheat_pb2.C2GS_BuySpringFestivalPlayer()
        G.rewardId = i
        header = 0x80000000 | 0x002E4
        self.datahandle(G, header)
        return self.body
    #消耗返利
    def TakeRechargeRebateReward(self,a,b):
        G=activity_pb2.C2GS_TakeRechargeRebateReward()
        G.id=a
        G.actId=b
        header = 0x80000000 | 0x00225
        self.datahandle(G, header)
        return self.body
    #VIP福利
    def ReceiveVipWelfare(self):
        G=vip_pb2.C2GS_ReceiveVipWelfare()
        header = 0x80000000 | 0x00246
        self.datahandle(G, header)
        return self.body
    #购买彩票
    def BuyQuizTicket(self,i):
        G=quiz_pb2.C2GS_BuyQuizTicket()
        G.num=i
        header = 0x80000000 | 0x002BE
        self.datahandle(G, header)
        return self.body
    #添加好友
    def Search(self):
        G=friends_pb2.C2GS_Search()
        header = 0x80000000 | 0x0076
        self.datahandle(G, header)
        return self.body
    #进入球场
    def GetFacilities(self):
        G=footballfacilities_pb2.C2GS_GetFacilities()
        header = 0x80000000 | 0x001DC
        self.datahandle(G, header)
        return self.body
    #升级球场
    def UpgradeFacilities(self):
        G=footballfacilities_pb2.C2GS_UpgradeFacilities()
        G.type=1
        header = 0x80000000 | 0x001E0
        self.datahandle(G, header)
        return self.body
    #快速升级球场
    def UpgradeQuicklyFinish(self):
        G=footballfacilities_pb2.C2GS_UpgradeQuicklyFinish()
        G.type=1
        header = 0x80000000 | 0x001E2
        self.datahandle(G, header)
        return self.body
    #欧元购买
    def BuyCoin(self):
        G=teaminfo_pb2.C2GS_BuyCoin()
        header = 0x80000000 | 0x00119
        self.datahandle(G, header)
        return self.body
    #体力购买
    def BuyTili(self):
        G=manager_pb2.C2GS_BuyTili()
        header = 0x80000000 | 0x0011D
        self.datahandle(G, header)
        return self.body
    #改名卡
    def BuyProp(self):
        G=manager_pb2.C2GS_BuyProp()
        G.propId=1037
        G.propNum=1
        header = 0x80000000 | 0x0044
        self.datahandle(G, header)
        return self.body
    #改名
    def SwitchName(self,i):
        G=manager_pb2.C2GS_SwitchName()
        G.newName="%s"%i
        header = 0x80000000 | 0x0046
        self.datahandle(G, header)
        return self.body


conf.set("uid","uid",str(uid+1))
conf.write(open('config.ini','w'))


















