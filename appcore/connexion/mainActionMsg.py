# -*- coding: utf-8 -*-
import wx

import appSettings
from appcore.display.mainDisplay import mainDisplay


def mainActionMsg(self, changeInfos):
    action = changeInfos['action']
    user = changeInfos['user']
    nickname = changeInfos['nickname']
    statesUsers = changeInfos['statesUsers']

    appSettings.user01State = statesUsers['user01State']
    appSettings.user02State = statesUsers['user02State']
    appSettings.user03State = statesUsers['user03State']
    appSettings.user04State = statesUsers['user04State']

    if action == "win":
        if appSettings.isLoggedIn:
            msg = nickname + " nous a rejoint"
            self.statusBar.SetStatusText(msg, 0)
        else:
            if appSettings.user == user:
                appSettings.isLoggedIn = True
                msg = "Connecté(e) en tant que: " + nickname
                self.statusBar.SetStatusText(msg, 0)

    mainDisplay(self)
