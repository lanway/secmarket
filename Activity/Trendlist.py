# -*- coding: utf-8 -*-
from sqlalchemy import desc

from BaseHandlerh import BaseHandler
from Database.tables import Trend


class Trendlist(BaseHandler):

    retjson = {'code':200,'contents':''}

    def post(self):

        trends = self.db.query(Trend).filter(Trend.Tvalid == 1,Trend.Tstatus==0).order_by(desc(Trend.TcreatT)).limit(10).all()
