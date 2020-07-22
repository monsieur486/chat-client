# -*- coding: utf-8 -*-


import json
import sys
import jsonpickle
import wx.adv

if 'twisted.internet.reactor' in sys.modules:
    del sys.modules['twisted.internet.reactor']

from appcore.initialization.initialization import initialization

initialization()

import appSettings
from templates.AppFrame import AppFrame
from twisted.internet import wxreactor

wxreactor.install()

from twisted.internet import reactor, protocol
from twisted.protocols import basic


class DataForwardingProtocol(basic.LineReceiver):

    def lineReceived(self, line):
        pass

    def rawDataReceived(self, data):
        pass

    def __init__(self):
        self.output = None

    def dataReceived(self, data):
        msgJSONData = json.dumps(data.decode("UTF-8"))
        msgJSON = jsonpickle.decode(msgJSONData)
        message = json.loads(msgJSON)
        frame.mailBox.SetValue(str(message))
        gui = self.factory.gui
        gui.protocol = self

    def connectionMade(self):
        pass


class AppFactory(protocol.ClientFactory):
    def __init__(self, gui):
        self.gui = gui
        self.protocol = DataForwardingProtocol

    def clientConnectionLost(self, transport, reason):
        reactor.stop()

    def clientConnectionFailed(self, transport, reason):
        reactor.stop()


if __name__ == '__main__':
    app = wx.App(False)
    frame = AppFrame(None)
    frame.Show()
    reactor.registerWxApp(app)
    reactor.connectTCP(appSettings.HOST_GAME, appSettings.PORT_GAME, AppFactory(frame))
    reactor.run()
