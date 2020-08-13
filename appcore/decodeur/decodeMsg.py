# -*- coding: utf-8 -*-


from appcore.decodeur.mainActionMsg import mainActionMsg
from appcore.decodeur.cxnMsg import cnxMsg
from appcore.decodeur.errorMsg import errorMsg
from appcore.decodeur.newMessageMsg import newMessageMsg


def decodeMsg(self, code, value):
    if code == 'error':
        errorMsg(self, value)

    if code == 'cnx':
        cnxMsg(self, value)

    if code == 'mainAction':
        mainActionMsg(self, value)

    if code == 'newMessage':
        newMessageMsg(self, value)

