# -*- coding: utf-8 -*-


import wx
import appSettings


def mainDisplay(self):
    if appSettings.isDemoMode:
        self.mailBox.Show()
    else:
        self.mailBox.Hide()

    if appSettings.isLoggedIn:
        self.pingBtn.Enable()
        self.sendBtn.Enable()
        self.msgText.Enable()
    else:
        self.pingBtn.Disable()
        self.sendBtn.Disable()
        self.msgText.Disable()
        self.fullPlace.SetLabel("no cnx")
        self.pingUser01Btn.Disable()
        self.pingUser02Btn.Disable()
        self.pingUser03Btn.Disable()

    self.cnxBtn01.Disable()
    self.cnxBtn02.Disable()
    self.cnxBtn03.Disable()

    if appSettings.user01State:
        self.user01Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
        self.user01Deno.SetLabel("Poste 1")
        if appSettings.isLoggedIn:
            self.pingUser01Btn.Enable()
            self.cnxBtn02.Disable()
            self.cnxBtn03.Disable()
            if appSettings.userID == "user01":
                self.user01Deno.SetLabel("Moi")
                self.user01Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))
                self.fullPlace.SetLabel("Cnx P01")
    else:
        self.user01Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY))
        self.pingUser01Btn.Disable()
        self.user01Deno.SetLabel("Poste 1")
        if not appSettings.isLoggedIn:
            self.cnxBtn01.Enable()

    if appSettings.user02State:
        self.user02Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
        self.user02Deno.SetLabel("Poste 2")
        if appSettings.isLoggedIn:
            self.pingUser02Btn.Enable()
            self.cnxBtn02.Disable()
            self.cnxBtn03.Disable()
            if appSettings.userID == "user02":
                self.user02Deno.SetLabel("Moi")
                self.user02Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))
                self.fullPlace.SetLabel("Cnx P02")
    else:
        self.user02Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY))
        self.pingUser02Btn.Disable()
        self.user02Deno.SetLabel("Poste 2")
        if not appSettings.isLoggedIn:
            self.cnxBtn02.Enable()

    if appSettings.user03State:
        self.user03Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
        self.user03Deno.SetLabel("Poste 3")
        if appSettings.isLoggedIn:
            self.pingUser03Btn.Enable()
            self.cnxBtn02.Disable()
            self.cnxBtn03.Disable()
            if appSettings.userID == "user03":
                self.user03Deno.SetLabel("Moi")
                self.user03Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))
                self.fullPlace.SetLabel("Cnx P03")
    else:
        self.user03Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY))
        self.pingUser03Btn.Disable()
        self.user03Deno.SetLabel("Poste 3")
        if not appSettings.isLoggedIn:
            self.cnxBtn03.Enable()

    if appSettings.bordLed == 1:
        self.trafficLight.SetBitmap(wx.Bitmap(u"public/icons/feu01.png", wx.BITMAP_TYPE_ANY))

    if appSettings.bordLed == 2:
        self.trafficLight.SetBitmap(wx.Bitmap(u"public/icons/feu02.png", wx.BITMAP_TYPE_ANY))

    if appSettings.bordLed == 3:
        self.trafficLight.SetBitmap(wx.Bitmap(u"public/icons/feu03.png", wx.BITMAP_TYPE_ANY))

    self.Layout()
