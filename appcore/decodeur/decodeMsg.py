# -*- coding: utf-8 -*-


from appcore.connexion.cnxOkMsg import cnxOkMsg
from appcore.connexion.mainActionMsg import mainActionMsg
from appcore.display.cxnMsg import cnxMsg


def decodeMsg(self, code, value):
    if code == 'cnx':
        cnxMsg(self, value)

    if code == 'cnxOk':
        cnxOkMsg(self, value)

    if code == 'mainAction':
        mainActionMsg(self, value)
