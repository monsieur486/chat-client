# -*- coding: utf-8 -*-


import time
import appSettings


def t():
    return "[" + time.strftime("%H:%M:%S") + "] "


def newMessageMsg(self, chatMsg):
    if appSettings.isLoggedIn:
        userID = chatMsg['userID']
        nickname = chatMsg['nickname']
        msgToSend = chatMsg['msgToSend']

        if appSettings.userID == userID:
            data = "Vous: " + msgToSend + '\n'
        else:
            data = nickname + ": " + msgToSend + '\n'

        val = self.chatTxt.GetValue()
        self.chatTxt.SetValue(val + t() + data)
        self.chatTxt.SetInsertionPointEnd()
        self.Layout()
