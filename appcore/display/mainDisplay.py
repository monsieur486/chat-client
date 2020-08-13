# -*- coding: utf-8 -*-


import wx
import appSettings


def mainDisplay(self):
    if appSettings.isDemoMode:
        self.mailBox.Show()
    else:
        self.mailBox.Hide()

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

        if appSettings.isDispo:
            self.afkBtn.Show()
            self.dispoBtn.Hide()
        else:
            self.afkBtn.Hide()
            self.dispoBtn.Show()

        if appSettings.user01State == 0:
            self.user01Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user01State == 1:
            self.user01Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user01State == 2:
            self.user01Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user02State == 0:
            self.user02Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user02State == 1:
            self.user02Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user02State == 2:
            self.user02Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user03State == 0:
            self.user03Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user03State == 1:
            self.user03Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user03State == 2:
            self.user03Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user04State == 0:
            self.user04Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user04State == 1:
            self.user04Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))

        if appSettings.user04State == 2:
            self.user04Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

        self.sendBtn.Enable()
        self.textMsg.Enable()

    else:
        self.afkBtn.Hide()
        self.dispoBtn.Hide()
        self.userIcon.Show()
        self.userLogin.Show()
        self.pwdIcon.Show()
        self.userPwd.Show()
        self.cnxBtn.Show()

        self.user01Led.Hide()
        self.user02Led.Hide()
        self.user03Led.Hide()
        self.user04Led.Hide()

        self.user01Deno.Hide()
        self.user02Deno.Hide()
        self.user03Deno.Hide()
        self.user04Deno.Hide()

        self.sendBtn.Disable()
        self.textMsg.Disable()

    self.Layout()
