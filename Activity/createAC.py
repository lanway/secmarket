# -*- coding: utf-8 -*-
import json

from BaseHandlerh import BaseHandler
from Database.tables import Trend
from pichandler.ImageHandler import ImageHandler
from pichandler.Upload import AuthKeyHandler


class createAC(BaseHandler):

    retjson = {"code": 200, "contents": "ok"}
    def post(self):

        type = self.get_argument('vali')

        if type == '10100':
            m_image = self.get_argument('images')
            print m_image
            print '111'
            m_image_json = json.loads(m_image)
            print m_image_json
            m_image = m_image_json['image']
            print m_image
            image_handler = AuthKeyHandler()
            image_tokens = image_handler.generateToken(m_image)
            self.retjson['code'] = '10101'
            self.retjson['contents'] = image_tokens

        if type == '10200':
            uid = self.get_argument('uid')
            content = self.get_argument('content')
            price = self.get_argument('price')
            phone = self.get_argument('phone')
            images = self.get_argument('images')
            my_trend = Trend(
                Tuid=uid,
                Tconcents=content,
                Tprice=price,
                Tphone=phone,
                Ttranid=uid,
            )
            self.db.merge(my_trend)
            try:
                self.db.commit()
                trend = self.db.query(Trend).filter(Trend.Tconcents == content,Trend.Tuid == uid).all()
                imagehandler = ImageHandler()
                image_list = json.loads(images)
                if imagehandler.insert_trand_image(image_list,trend[len(trend)-1].Tid):
                    self.retjson["code"] = '10202'
                    self.retjson['contents'] = '创建交易成功'
                else:
                    self.retjson["code"] = '10203'
                    self.retjson['contents'] = '服务器内部错误,创建失败'
            except Exception,e:
                print e
                self.retjson["code"] = '10201'
                self.retjson['contents'] = '服务器内部错误，创建失败'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))