# -*- coding:utf8 -*-
import json

from BaseHandlerh import BaseHandler
from Database.tables import User
from User.Usermodel import Usermodel


class userdetail(BaseHandler):


    retjson = {'code':'200',"contents":"ok"}
    def post(self):

        uid = self.get_argument('uid')
        try:
            user = self.db.query(User).filter(User.Uid == uid,User.Uvalid == 1).one()
            usehandler = Usermodel()
            retdata = usehandler.detail_user_model(user)
            self.retjson['code'] = '10501'
            self.retjson['contents'] = retdata
        except Exception,e:
            print e
            self.retjson['code'] = '10500'
            self.retjson['contents'] = '未查找到此用户'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))