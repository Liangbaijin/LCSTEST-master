# -*- coding: utf-8 -*-
import pymysql
import configparser

class sqlutil():
    """
    建议是单独对于数据库检查单独对增加删除查改写一个modules部分 抽象下
    """
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    uid = conf.getint("uid", "uid")
    host = conf.get("DATABASE", "host")
    port = conf.getint("DATABASE", "port")
    user = conf.get("DATABASE", "username")
    password = conf.get("DATABASE", "password")
    database = conf.get("DATABASE", "database")

    def update_teaminfo(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database, charset='utf8')
        cursor = conn.cursor()
        try:
            sql = 'UPDATE game_team_info set level=100,vip=10,diamond=99999,coin=9999999 where uid="1-%d"' % (self.uid)
            res = cursor.execute(sql)
            if res:
                conn.commit()
            return res
        except Exception as err:
            print(format(err))
        finally:
            conn.close()
            cursor.close()
    def insert_prop(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database, charset='utf8')
        cursor = conn.cursor()
        try:
            sql = 'insert into game_user_property VALUES("1-%d",1076,9999,CURRENT_TIMESTAMP),("1-%d",1031,9999,CURRENT_TIMESTAMP),' \
                  '("1-%d",1078,9999,CURRENT_TIMESTAMP),("1-%d",1079,9999,CURRENT_TIMESTAMP),("1-%d",1080,9999,CURRENT_TIMESTAMP),' \
                  '("1-%d",1081,9999,CURRENT_TIMESTAMP),("1-%d",1082,9999,CURRENT_TIMESTAMP),("1-%d",1083,9998,CURRENT_TIMESTAMP),' \
                  '("1-%d",1084,9999,CURRENT_TIMESTAMP),("1-%d",1085,9999,CURRENT_TIMESTAMP)' % (
                  self.uid, self.uid, self.uid, self.uid, self.uid, self.uid, self.uid, self.uid, self.uid, self.uid)
            res = cursor.execute(sql)
            if res:
                conn.commit()
            return res
        except Exception as err:
            print(format(err))
        finally:
            conn.close()
            cursor.close()


    def query_playerId(self):
        """
        读取uid查询playerId
        :return:
        """
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database, charset='utf8')
        cursor = conn.cursor()
        try:
            sql = 'SELECT player_id from game_player_instance where uid="1-%d" and level>=5'%(self.uid)
            res =cursor.execute(sql)
            if res:
                conn.commit()
                data1 = cursor.fetchall()
                playerId=data1[0][0] #
                if isinstance(playerId,int): #类型检查需要你这边自己改
                    return playerId
        except Exception as err:
            print(format(err))
        finally:
            conn.close()
            cursor.close()

    def query_equipId(self):
        """
        读取uid查询equipId
        :return:
        """
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database, charset='utf8')
        cursor = conn.cursor()
        try:
            sql='SELECT id from game_user_equipment where uid="1-%d" '%(self.uid)
            res =cursor.execute(sql)
            if res:
                conn.commit()
                data2 = cursor.fetchall()
                equipId=data2[0][0] #
                if isinstance(equipId,int): #类型检查需要你这边自己改
                    return equipId
        except Exception as err:
            print(format(err))
        finally:
            conn.close()
            cursor.close()

    def set_player_instance(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database, charset='utf8')
        cursor = conn.cursor()
        try:
            sql='update game_player_instance set level = 50 where uid = "1-%d"'%(self.uid)
            res =cursor.execute(sql)
            if res:
                conn.commit()
            return res
        except Exception as err:
            print(format(err))
        finally:
            conn.close()
            cursor.close()
    #修改公会贡献
    def upd_guild_contribution(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database, charset='utf8')
        cursor = conn.cursor()
        try:
            sql = 'select guild_id from game_user_guild where uid="1-%d"'%(self.uid)
            cursor.execute(sql)
            conn.commit()
            data1 = cursor.fetchall()
            sql = 'update game_guild_info set now_contribution=50000,daily_contribution=50000 where id="%d"' % (
            int(data1[0][0]))
            res=cursor.execute(sql)
            if res:
                conn.commit()
            return res
        except Exception as err:
            print(format(err))
        finally:
            conn.close()
            cursor.close()