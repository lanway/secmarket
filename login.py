# -*- coding:utf-8 -*-
'''
@author :lanwei
@datatime :2017-3-9
'''
import json

from BaseHandlerh import BaseHandler
from Database.tables import User


def my_md5(str):  # 加密
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

class Login(BaseHandler):

    retjson = {"code": 200, "contents": "ok"}


    def post(self):
        u_username = self.get_argument("username")
        u_passwd = self.get_argument("password")
        try:
            data = self.db.query(User).filter(User.Ualais == u_username).one()
            if data.Upassword == my_md5(u_passwd):
                self.retjson['code'] =  '10010'
                self.retjson['contents'] = '登录成功'
            else:
                self.retjson['code'] = '10011'
                self.retjson['contents'] = '密码错误'
        except Exception,e:
            print e
            try:
                data = self.db.query(User).filter(User.Utel == u_username).one()
                if data.Upassword == my_md5(u_passwd):
                    self.retjson['code'] = '10010'
                    self.retjson['contents'] = '登录成功'
                else:
                    self.retjson['code'] = '10011'
                    self.retjson['contents'] = '密码错误'
            except Exception,e:
                print e
                try:
                    data = self.db.query(User).filter(User.Ucardnum == u_username).one()
                    if data.Upassword == my_md5(u_passwd):
                        self.retjson['code'] = '10010'
                        self.retjson['contents'] = '登录成功'
                    else:
                        self.retjson['code'] = '10011'
                        self.retjson['contents'] = '密码错误'
                except Exception,e:
                    print e
                    self.retjson['code'] = '10012'
                    self.retjson['contents'] = '该用户不存在，请先注册'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))
