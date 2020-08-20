# -*- coding: utf-8 -*-


import time
import appSettings
from appcore.display.mainDisplay import mainDisplay


def t():
    return "[" + time.strftime("%H:%M:%S") + "] "


def pingMsg(self, value):
    if appSettings.isLoggedIn:
        state = appSettings.bordLed
        state += 1
        if state >= 4:
            state = 1
        appSettings.bordLed = state
        appSettings.pingNb += 1
        if appSettings.pingNb == 1:
            msg = "1er ping"
        else:
            msg = str(appSettings.pingNb) + "ième ping"
        self.statusBar.SetStatusText(msg, 0)
        mainDisplay(self)
