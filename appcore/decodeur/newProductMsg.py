# -*- coding: utf-8 -*-


import appSettings
from appcore.display.mainDisplay import mainDisplay


def newProductMsg(self, productInfos):
    appSettings.product01 = productInfos['product01']
    appSettings.product02 = productInfos['product02']
    appSettings.product03 = productInfos['product03']
    mainDisplay(self)
