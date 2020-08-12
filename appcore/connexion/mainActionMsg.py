# -*- coding: utf-8 -*-
import wx

import appSettings


def mainActionMsg(self, changeInfos):
    action = changeInfos['action']
    user = changeInfos['user']
    nickname = changeInfos['nickname']
    statesUsers = changeInfos['statesUsers']

    user01State = statesUsers['user01State']
    user02State = statesUsers['user02State']
    user03State = statesUsers['user03State']
    user04State = statesUsers['user04State']

    if appSettings.user == user:
        appSettings.userIsLoggedIn = True

    self.Layout()
