# -*- coding: utf-8 -*-
import wx

import appSettings


def mainActionMsg(self, statsInfos):

    change = statsInfos['change']
    user = statsInfos['user']
    user01State = statsInfos['user01State']
    user02State = statsInfos['user02State']
    user03State = statsInfos['user03State']
    user04State = statsInfos['user04State']

    if appSettings.user == user:
        appSettings.userIsLoggedIn = True

    self.Layout()
