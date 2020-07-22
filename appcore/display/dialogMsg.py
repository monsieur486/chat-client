# -*- coding: utf-8 -*-
import wx


def dialogMsg(self, titre, msg):
    dialog = wx.MessageDialog(self, msg, titre, wx.OK | wx.ICON_ERROR)
    dialog.ShowModal()
    dialog.Destroy()
