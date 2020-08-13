# -*- coding: utf-8 -*-


import appSettings


def mainDisplay(self):
    if appSettings.isLoggedIn:
        self.userIcon.Hide()
        self.userLogin.Hide()
        self.pwdIcon.Hide()
        self.userPwd.Hide()
        self.cnxBtn.Hide()

        self.user01Led.Show()
        self.user02Led.Show()
        self.user03Led.Show()
        self.user04Led.Show()

        self.user01Deno.Show()
        self.user02Deno.Show()
        self.user03Deno.Show()
        self.user04Deno.Show()

        self.sendBtn.Enable()
        self.sendText.Enable()
        self.afkBtn.Show()
        self.chatView.Enable()

    else:
        self.userIcon.Show()
        self.userLogin.Show()
        self.pwdIcon.Show()
        self.userPwd.Show()
        self.cnxBtn.Show()

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

        #self.sendBtn.Disable()
        self.sendText.Disable()
        self.afkBtn.Hide()
        self.chatView.Disable()

    self.Layout()
