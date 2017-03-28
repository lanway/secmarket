# -*- coding: utf-8 -*-
import json

from BaseHandlerh import BaseHandler
from Database.tables import TrendComment


class Trendcomment(BaseHandler):

    retjson = {'code': '', 'contents': u'未处理 ',}
    def post(self):
        uid = self.get_argument('uid')
        tid = self.get_argument('tid')
        content = self.get_argument('content')

        item = TrendComment(
            TCtid=tid,
            TCuid=uid,
            TCcontents=content
        )
        self.db.merge(item)
        try:
            self.db.commit()
            self.retjson['code'] = '10400'
            self.retjson['contents'] = '评论成功'
        except Exception,e:
            print e
            self.retjson['code'] = '10401'
            self.retjson['contents'] = '评论失败'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))

