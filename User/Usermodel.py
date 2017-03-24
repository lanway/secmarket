# -*- coding:utf8 -*-
from BaseHandlerh import BaseHandler
from Database.models import get_db
from Database.tables import UserImage
from pichandler.Upload import AuthKeyHandler


class Usermodel(BaseHandler):

    def detail_user_model(clas,user):

        user_img = get_db().query(UserImage).filter(UserImage.UIuid == user.Uid,UserImage.UIvalid == 1).one()
        auth = AuthKeyHandler()
        sex = '男'
        if user.Usex == 0:
            sex = '女'
        respond = dict(
            uid=user.Uid,
            ualais = user.Ualais,
            ucardnum = user.Ucardnum,
            ucollege = user.Ucollege,
            usex = sex,
            utel = user.Utel,
            uimage = auth.download_abb_url(user_img.UIurl),
        )
        return respond
