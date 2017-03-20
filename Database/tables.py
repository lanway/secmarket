# -*- coding: utf-8 -*-


from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,ForeignKey,DateTime,Boolean
from sqlalchemy.types import CHAR, Integer, VARCHAR,Boolean,Float
from sqlalchemy.sql.functions import func
from models import Base
import sys
reload(sys)

# from models import engine

# 每个类对应一个表
class User(Base): # 用户表   #添加聊天专用chattoken
    __tablename__ = 'User'

    Uid = Column(Integer, nullable=False, primary_key=True)  # 主键
    Upassword = Column(VARCHAR(64), nullable=False)
    Utel = Column(CHAR(32), nullable=False,unique=True)
    Ualais = Column(VARCHAR(24),nullable=False,unique=True)  # 昵称，可能为微信昵称
    UregistT = Column(DateTime(timezone=True), default=func.now())
    Usex = Column(Integer, nullable=False)
    Usign = Column(VARCHAR(256),default = '') #个人签名
    Uvalid = Column(Integer, nullable=False, default=1)
    Ucollege = Column(VARCHAR(64),nullable=False) #学院名称
    Ucardnum = Column(CHAR(9),nullable=False) #一卡通号
    Ustunum = Column(CHAR(8),nullable=False,default=None)#学号



class Verification(Base):  # 短信验证码及生成用户auth_key时间
    __tablename__ = 'Verification'

    Vphone = Column(CHAR(11),primary_key=True) #
    Vcode = Column(CHAR(6),nullable=False)
    VT = Column(DateTime(timezone=True), default=func.now()) # 待测试是插入数据的时间还是最后一次更新该表的时间 （测试结果为第一次插入时间）



class UserImage(Base):
    __tablename__ = 'UserImage'

    UIuid = Column(Integer,ForeignKey("User.Uid", onupdate="CASCADE"))   #用户id
    UIid = Column(Integer, primary_key=True)
    UIurl = Column(VARCHAR(128))
    UIvalid = Column(Boolean, default=1, nullable=False)
    UIcreatT = Column(DateTime(timezone=True), default=func.now())

class Trend(Base):
    __tablename__ = 'Trend'

    Tid = Column(Integer,primary_key=True)
    Tuid = Column(Integer,ForeignKey("User.Uid", onupdate="CASCADE"))
    TcreatT = Column(DateTime(timezone=True), default=func.now())
    Tconcents = Column(VARCHAR(256),nullable=False) # 内容
    Tprice = Column(Float,default=0.00,nullable=False)   #价格
    Tphone = Column(CHAR(32), nullable=False)   # 电话，可以留不是自己的
    Tvalid = Column(Boolean,default=1, nullable=False) #是否有效
    TlikeN = Column(Integer,default=0,nullable=False)  #点赞数
    TtranN = Column(Integer,default=0,nullable=False)  #转发数
    TcomN = Column(Integer,default=0,nullable=False)   #点赞数
    Ttranid = Column(Integer,ForeignKey("User.Uid", onupdate="CASCADE"))  #从哪个人那里转发的
    Tstatus = Column(Integer,default=0) #0表示交易未完成，1表示交易完成了

class TrendImage(Base):
    __tablename__ = 'TrendImage'

    TIid = Column(Integer,primary_key=True)  #动态图片的ID
    TItid = Column(Integer,ForeignKey("Trend.Tid", onupdate="CASCADE")) #动态ID
    TIcreatT = Column(DateTime(timezone=True), default=func.now()) #时间
    TIurl = Column(VARCHAR(128))
    TIvalid = Column(Boolean, default=1, nullable=False)

class TrendComment(Base):
    __tablename__ = 'TrendCommit'

    TCid = Column(Integer,primary_key=True)
    TCtid = Column(Integer,ForeignKey("Trend.Tid", onupdate="CASCADE")) #动态ID
    TCuid = Column(Integer,ForeignKey("User.Uid", onupdate="CASCADE")) #评论人id
    TCvalid = Column(Boolean, default=1, nullable=False)
    TCcreatT = Column(DateTime(timezone=True), default=func.now()) #时间
    TCcontents = Column(VARCHAR(256),nullable=False)

class TrendTran(Base):
    __tablename__ = 'TrendTran'

    TTid = Column(Integer,primary_key=True)
    TTtid = Column(Integer,ForeignKey("Trend.Tid", onupdate="CASCADE")) #动态ID
    TTuid = Column(Integer,ForeignKey("User.Uid", onupdate="CASCADE")) #转发人id
    TTvalid = Column(Boolean, default=1, nullable=False)
    TTtranT = Column(DateTime(timezone=True), default=func.now())  # 转发时间

