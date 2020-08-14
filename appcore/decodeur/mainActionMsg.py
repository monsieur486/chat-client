# -*- coding: utf-8 -*-


import appSettings
import time

from appcore.display.mainDisplay import mainDisplay


def t():
    return "[" + time.strftime("%H:%M:%S") + "] "


def mainActionMsg(self, changeInfos):
    action = changeInfos['action']
    user = changeInfos['user']
    nickname = changeInfos['nickname']
    statesUsers = changeInfos['statesUsers']

    appSettings.user01State = statesUsers['user01State']
    appSettings.user02State = statesUsers['user02State']
    appSettings.user03State = statesUsers['user03State']
    appSettings.user04State = statesUsers['user04State']

    msg = ""

    if action == "win":
        if appSettings.isLoggedIn:
            msg = nickname + " nous a rejoint"
            self.statusBar.SetStatusText(msg, 0)
        else:
            if appSettings.user == user:
                appSettings.isLoggedIn = True
                msg = "Connecté(e) en tant que: " + nickname
                appSettings.nickname = nickname
                self.statusBar.SetStatusText(msg, 0)
                if user == "user01":
                    self.user01Deno.SetLabel("Vous")
                if user == "user02":
                    self.user02Deno.SetLabel("Vous")
                if user == "user03":
                    self.user03Deno.SetLabel("Vous")
                if user == "user04":
                    self.user04Deno.SetLabel("Vous")

    if action == "loose":
        if appSettings.isLoggedIn:
            msg = nickname + " nous a quitté"
            self.statusBar.SetStatusText(msg, 0)

    if action == "pause":
        if appSettings.isLoggedIn:
            if appSettings.user == user:
                appSettings.isDispo = False
                msg = "Vous partez en pause"
            else:
                msg = nickname + " est en pause"

            self.statusBar.SetStatusText(msg, 0)

    if action == "dispo":
        if appSettings.isLoggedIn:
            if appSettings.user == user:
                appSettings.isDispo = True
                msg = "Vous êtes disponible"
            else:
                msg = nickname + " est disponible"

            self.statusBar.SetStatusText(msg, 0)

    val = self.chatBoard.GetValue()
    self.chatBoard.SetValue(val + t() + msg + '\n')
    self.chatBoard.SetInsertionPointEnd()

    mainDisplay(self)
