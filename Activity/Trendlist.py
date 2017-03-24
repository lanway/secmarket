# -*- coding: utf-8 -*-
import json

from sqlalchemy import desc

from Activity.Trendmodel import TrmodelHandler
from BaseHandlerh import BaseHandler
from Database.tables import Trend


class Trendlist(BaseHandler):

    retjson = {'code':200,'contents':''}

    def post(self):

        trends = self.db.query(Trend).filter(Trend.Tvalid == 1,Trend.Tstatus==0).order_by(desc(Trend.TcreatT)).limit(10).all()
        trend_info = []
        auth = TrmodelHandler()
        for trend in trends:
            trend_info.append(auth.tr_Model_simply(trend))
        self.retjson['code'] = '10300'
        self.retjson['contents'] = trend_info
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))

