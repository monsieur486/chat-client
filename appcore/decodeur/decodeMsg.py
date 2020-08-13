# -*- coding: utf-8 -*-


from appcore.connexion.mainActionMsg import mainActionMsg
from appcore.display.cxnMsg import cnxMsg
from appcore.display.errorMsg import errorMsg


def decodeMsg(self, code, value):
    if code == 'error':
        errorMsg(self, value)

    if code == 'cnx':
        cnxMsg(self, value)

    if code == 'cnxOk':
        cnxOkMsg(self, value)

    if code == 'mainAction':
        mainActionMsg(self, value)

