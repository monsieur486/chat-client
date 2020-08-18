# -*- coding: utf-8 -*-


import wx
import appSettings


def mainDisplay(self):
    if appSettings.isDemoMode:
        self.mailBox.Show()
    else:
        self.mailBox.Hide()

    self.Layout()
