# -*- coding: utf-8 -*-
from Database import UserImage, TrendImage, User
from Database import get_db
from pichandler.Upload import AuthKeyHandler


class TrmodelHandler:
    @classmethod
    def tr_Model_simply(clas,trend):
        '''得到简单活动模型
        :return:  retjson
        '''
        user_headimage_url = get_db().query(UserImage).filter(UserImage.UIuid == trend.Tuid ).all()
        use = get_db().query(User).filter(User.Uid == trend.Tuid).one()
        usename = use.Ualais
        #todo:查找待变更为最新10个
        auth = AuthKeyHandler()
        user_headimage = auth.download_abb_url(user_headimage_url[0].UIurl)
        trend_images_urls = get_db().query(TrendImage).filter(TrendImage.TItid == trend.Tid,TrendImage.TIvalid == 1).all()
        trend_images = []
        for trend_images_url in trend_images_urls:
            trend_images.append(auth.download_url(trend_images_url.TIurl))

        tr_simply_info = dict(
        Tid = trend.Tid,
        TcreatT=trend.TcreatT.strftime('%Y-%m-%d %H:%M'),
        Tconcents=trend.Tconcents,
        Tprice=trend.Tprice,
        Tphone=trend.Tphone,
        TlikeN=trend.TlikeN,
        TcomN=trend.TcomN,
        Tuid=trend.Tuid,
        user_image= user_headimage,
        ualais=usename,
        trend_image=trend_images,
        )
        return tr_simply_info
