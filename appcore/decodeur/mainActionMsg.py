# -*- coding: utf-8 -*-


import appSettings
import time

from appcore.display.mainDisplay import mainDisplay


def t():
    return "[" + time.strftime("%H:%M:%S") + "] "


def mainActionMsg(self, changeInfos):
    action = changeInfos['action']
    user = changeInfos['userID']
    nickname = changeInfos['nickname']
    statesUsers = changeInfos['statesUsers']

    appSettings.user01State = statesUsers['user01State']
    appSettings.user02State = statesUsers['user02State']
    appSettings.user03State = statesUsers['user03State']

    if action == "win":
        if appSettings.isLoggedIn:
            msg = nickname + " nous a rejoint"
            self.statusBar.SetStatusText(msg, 0)
        else:
            if appSettings.userID == user:
                appSettings.isLoggedIn = True
                msg = "Connecté(e) en tant que: " + nickname
                appSettings.nickname = nickname
                self.statusBar.SetStatusText(msg, 0)

    if action == "loose":
        if appSettings.isLoggedIn:
            msg = nickname + " nous a quitté"
            self.statusBar.SetStatusText(msg, 0)

    mainDisplay(self)
