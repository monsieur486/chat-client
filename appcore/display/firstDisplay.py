# -*- coding: utf-8 -*-


import appSettings


def mainDisplay(self):
    if appSettings.isLoggedIn:
        self.sendBtn.Enable()
        self.sendText.Enable()
        self.afkBtn.Enable()
    else:
        self.user01Kick.Hide()
        self.user02Kick.Hide()
        self.user03Kick.Hide()

        self.user01Led.Hide()
        self.user02Led.Hide()
        self.user03Led.Hide()
        self.user04Led.Hide()

        self.user01Deno.Hide()
        self.user02Deno.Hide()
        self.user03Deno.Hide()
        self.user04Deno.Hide()

        self.sendBtn.Disable()
        self.sendText.Disable()
        self.afkBtn.Disable()
        self.chatView.Disable()

    self.Layout()
