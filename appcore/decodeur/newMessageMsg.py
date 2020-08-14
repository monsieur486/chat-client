# -*- coding: utf-8 -*-


import time
import appSettings


def t():
    return "[" + time.strftime("%H:%M:%S") + "] "


def newMessageMsg(self, chatMsg):
    if appSettings.isLoggedIn:
        user = chatMsg['user']
        nickname = chatMsg['nickname']
        msgToSend = chatMsg['msgToSend']

        if appSettings.user == user:
            data = "Vous: " + msgToSend + '\n'
        else:
            data = nickname + ": " + msgToSend + '\n'

        val = self.chatBoard.GetValue()
        self.chatBoard.SetValue(val + t() + data)
        self.chatBoard.SetInsertionPointEnd()
        self.Layout()
