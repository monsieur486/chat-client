# -*- coding: utf-8 -*-


import appSettings


from appcore.translate import _


def nbFree5Display(self, game5Free):
    self.cnxTabPlay5.Enable()
    if game5Free < 2:
        self.cnxTabFree5Lbl.SetLabel(_("Partie : ") + str(game5Free))
    else:
        self.cnxTabFree5Lbl.SetLabel(_("Parties : ") + str(game5Free))
    if game5Free == 0 or appSettings.userPlay:
        self.cnxTabPlay5.Disable()
