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
        mainDisplay(self)
