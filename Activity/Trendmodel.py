# -*- coding: utf-8 -*-
from Database.tables import UserImage, TrendImage, User, TrendComment
from Database.models import get_db
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
        trend_comments = get_db().query(TrendComment).filter(TrendComment.TCtid == trend.Tid,TrendComment.TCvalid == 1).all()
        trend_co =[]
        for trend_comment in trend_comments:
            content = trend_comment.TCcontents
            uid = trend_comment.TCuid
            username = get_db().query(User).filter(User.Uid == uid).one()
            trend_item = {'username':username.Ualais,'contents':content}
            trend_co.append(trend_item)


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
        trend_comment=trend_co,
        )
        return tr_simply_info
