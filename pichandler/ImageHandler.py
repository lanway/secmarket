# -*- coding: utf-8 -*-

from Database.tables import TrendImage
from Database.models import get_db


class ImageHandler(object):

    def insert_trand_image(self,lists,uid):

        for list in lists:
            trend_img = TrendImage(
                TItid=uid,
                TIurl=list,
            )
            db = get_db()
            db.merge(trend_img)
            try:
                db.commit()
            except Exception,e:
                print e
                return False
        return True

