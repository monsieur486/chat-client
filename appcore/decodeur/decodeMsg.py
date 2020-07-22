# -*- coding: utf-8 -*-


from appcore.connexion.cnxOkMsg import cnxOkMsg
from appcore.connexion.mainActionMsg import mainActionMsg
from appcore.connexion.updateStatsInfosMsg import updateStatsInfosMsg
from appcore.display.cxnMsg import cnxMsg
from appcore.gameMsg.gameActionMsg import gameActionMsg
from appcore.gameMsg.playActionSelectContractMsg import playActionSelectContractMsg


def decodeMsg(self, code, value):
    if code == 'cnx':
        cnxMsg(self, value)

    if code == 'cnxOk':
        cnxOkMsg(self, value)

    if code == 'mainAction':
        mainActionMsg(self, value)

    if code == 'gameAction':
        gameActionMsg(self, value)

    if code == 'updateStatsInfos':
        updateStatsInfosMsg(self, value)

    if code == 'playActionSelectContract':
        playActionSelectContractMsg(self, value)

