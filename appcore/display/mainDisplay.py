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
        self.productList.Enable()
        self.productNbr.Enable()
        self.collectBtn.Enable()
    else:
        self.pingBtn.Disable()
        self.sendBtn.Disable()
        self.msgText.Disable()
        self.fullPlace.SetLabel("no cnx")
        self.pingUser01Btn.Disable()
        self.pingUser02Btn.Disable()
        self.pingUser03Btn.Disable()
        self.productList.Disable()
        self.productNbr.Disable()
        self.collectBtn.Disable()

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

    totalProduct = appSettings.product01 + appSettings.product02 + appSettings.product03

    print("PDT:" + str(totalProduct))

    if totalProduct == 0:
        txProduct01 = 0
        txProduct02 = 0
        txProduct03 = 0
    else:
        txProduct01 = round(appSettings.product01 / totalProduct * 100)
        txProduct02 = round(appSettings.product02 / totalProduct * 100)
        txProduct03 = round(appSettings.product03 / totalProduct * 100)
        
    self.pdt01Deno.SetLabel(u"PDT01 (" + str(appSettings.product01) + u")")
    self.gaugePdt01.SetValue(txProduct01)
    self.gaugePdt01.SetToolTip(str(txProduct01)+u"%")
    
    self.pdt02Deno.SetLabel(u"PDT02 (" + str(appSettings.product02) + u")")
    self.gaugePdt02.SetValue(txProduct02)
    self.gaugePdt02.SetToolTip(str(txProduct02)+u"%")
    
    self.pdt03Deno.SetLabel(u"PDT03 (" + str(appSettings.product03) + u")")
    self.gaugePdt03.SetValue(txProduct03)
    self.gaugePdt03.SetToolTip(str(txProduct03)+u"%")

    self.Layout()
