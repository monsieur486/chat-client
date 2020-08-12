# -*- coding: utf-8 -*-


from appcore.translate import _


def errorMsg(self, value):
    msg = ""
    if value == "badcnx":
        msg = "Informations invalides !"
    if value == "duplicate":
        msg = "Déja connecté(e) !"

    self.statusBar.SetStatusText(msg, 0)
    self.Layout()
