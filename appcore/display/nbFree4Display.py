# -*- coding: utf-8 -*-


import appSettings


from appcore.translate import _


def nbFree4Display(self, game4Free):
    self.cnxTabPlay4.Enable()
    if game4Free < 2:
        self.cnxTabFree4Lbl.SetLabel(_("Partie : ") + str(game4Free))
    else:
        self.cnxTabFree4Lbl.SetLabel(_("Parties : ") + str(game4Free))
    if game4Free == 0 or appSettings.userPlay:
        self.cnxTabPlay4.Disable()
