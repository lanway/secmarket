# -*- coding: utf-8 -*-
from Database.models import get_db
from Database.tables import UserImage
from pichandler.Upload import AuthKeyHandler


class TrmodelHandler:
    @classmethod
    def tr_Model_simply(clas,trend,url):
        '''得到简单活动模型
        :return:  retjson
        '''
        user_headimages = get_db().query(UserImage).filter(UserImage.UIuid == trend.Tuid ).all()
        #todo:查找待变更为最新10个
        auth = AuthKeyHandler()
        tr_simply_info = dict(
        Tid = trend.Tid,

        )
        return tr_simply_info
