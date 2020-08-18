# -*- coding: utf-8 -*-
import appSettings
from appcore.display.mainDisplay import mainDisplay
from appcore.translate import _


def cnxMsg(self, statsInfos):
    appSettings.user01State = statsInfos['user01State']
    appSettings.user02State = statsInfos['user02State']
    appSettings.user03State = statsInfos['user03State']
    msg = _("Bienvenue - Non connecté(e)")
    self.statusBar.SetStatusText(msg, 0)
    mainDisplay(self)
