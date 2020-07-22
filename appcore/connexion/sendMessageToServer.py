# -*- coding: utf-8 -*-


import jsonpickle

from appcore.connexion.MessageToServer import MessageToServer


def sendMessageToServer(self, code, value):
    msg = MessageToServer(code, value)
    cnxJSON = jsonpickle.encode(msg, unpicklable=False)
    self.protocol.sendLine(cnxJSON.encode('UTF-8'))
