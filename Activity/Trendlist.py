# -*- coding: utf-8 -*-
import json

from sqlalchemy import desc

from Activity.Trendmodel import TrmodelHandler
from BaseHandlerh import BaseHandler
from Database.tables import Trend


class Trendlist(BaseHandler):

    retjson = {'code':200,'contents':''}

    def get(self):

        trends = self.db.query(Trend).filter(Trend.Tvalid == 1,Trend.Tstatus==0).order_by(desc(Trend.TcreatT)).limit(20).all()
        trend_info = []
        auth = TrmodelHandler()
        for trend in trends:
            trend_info.append(auth.tr_Model_simply(trend))
        self.retjson['code'] = '10300'
        self.retjson['contents'] = trend_info
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))
    def post(self):
        uid = self.get_argument("uid")
        trends = self.db.query(Trend).filter(Trend.Tvalid == 1,Trend.Tstatus==0,Trend.Tuid == uid).order_by(desc(Trend.TcreatT)).limit(20).all()
        trend_info = []
        auth = TrmodelHandler()
        for trend in trends:
            trend_info.append(auth.tr_Model_simply(trend))
        self.retjson['code'] = '10300'
        self.retjson['contents'] = trend_info
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))