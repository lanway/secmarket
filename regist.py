# coding=utf-8
import json

from BaseHandlerh import BaseHandler
from Database.tables import User, UserImage


def md5(str):  # 加密
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

class regist(BaseHandler):

    retjson = {'code': '', 'contents': u'未处理 ', }

    def post(self):
        ualais = self.get_argument('username')
        upaw = self.get_argument('password')
        usex = self.get_argument('sex')
        ucardnum = self.get_argument('cardnum')
        utel = self.get_argument('phone')
        ucollege = self.get_argument('college')
        try:
            exist = self.db.query(User).filter(User.Utel == utel or User.Ucardnum == ucardnum).one()
            self.retjson['code'] = '10000'
            self.retjson['contents'] = '用户已注册'
        except Exception,e:
            upaw = md5(upaw)
            user = User(
                Upassword=upaw,
                Utel = utel,
                Ualais = ualais,
                Usex = usex,
                Ucollege = ucollege,
                Ucardnum = ucardnum,
                UregistT = '2016-09-09 12:12:12',
            )
            try:
                self.db.merge(user)
                self.db.commit()
                m_id = self.db.query(User.Uid).filter(User.Utel == utel).one()
                userimage = UserImage(
                    UIuid = m_id,
                    UIurl = "user-default-image.jpg",
                )
                self.db.merge(userimage)
                self.db.commit()
                self.retjson['code'] = '10001'
                self.retjson['contents'] = '注册成功'
            except Exception,e:
                print e
                self.retjson['code'] = '10009'
                self.retjson['contents'] = '服务器错误'
        self.write(json.dumps(self.retjson,ensure_ascii=False,indent=2))
