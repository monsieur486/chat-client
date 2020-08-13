# -*- coding: utf-8 -*-


from appcore.translate import _


def cnxMsg(self, value):
    msg = value + _(" - Non connecté(e)")
    self.statusBar.SetStatusText(msg, 0)
    self.Layout()
