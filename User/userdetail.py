# -*- coding:utf8 -*-
from BaseHandlerh import BaseHandler
from Database.tables import User


class Userdetail(BaseHandler):


    retsjon = {'code':'200',"contents":"ok"}
    def post(self):

        uid = self.get_argument('uid')
        try:
            user = self.db.query(User).filter(User.Uid == uid,User.Uvalid == 1).one()
        except Exception,e:
            print e
            self
