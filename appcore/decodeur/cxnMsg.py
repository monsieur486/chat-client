# -*- coding: utf-8 -*-
import appSettings
from appcore.display.mainDisplay import mainDisplay
from appcore.translate import _


def cnxMsg(self, value):
    appSettings.user01State = value['statsInfos']['user01State']
    appSettings.user02State = value['statsInfos']['user02State']
    appSettings.user03State = value['statsInfos']['user03State']
    appSettings.product01 = value['productInfos']['product01']
    appSettings.product02 = value['productInfos']['product02']
    appSettings.product03 = value['productInfos']['product03']
    msg = value['welcomeMsg'] + " - non connecté(e)"
    self.statusBar.SetStatusText(msg, 0)
    mainDisplay(self)
