# -*- coding: utf-8 -*-


import jsonpickle
import wx.adv
import queue
import appSettings
from appcore.decodeur.ChatMsg import ChatMsg
from appcore.connexion.UserCnx import UserCnx

from appcore.connexion.sendMessageToServer import sendMessageToServer
from appcore.decodeur.decodeMsg import decodeMsg
from appcore.display.mainDisplay import mainDisplay

jobs = queue.Queue()


###########################################################################
# Class AppFrame
###########################################################################

class AppFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"AppPubSub", pos=wx.DefaultPosition,
                          size=wx.Size(348, 548), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.protocol = None

        self.menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.menuChangeMode = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Change Mode", u"Change Mode", wx.ITEM_NORMAL)
        self.m_menu1.Append(self.menuChangeMode)

        self.m_menu1.AppendSeparator()

        self.menuQuit = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Quitter" + u"\t" + u"ctrl-q", u"Quitter l'application",
                                    wx.ITEM_NORMAL)
        self.m_menu1.Append(self.menuQuit)

        self.menubar1.Append(self.m_menu1, u"Menu")

        self.SetMenuBar(self.menubar1)

        mainPage = wx.BoxSizer(wx.VERTICAL)

        appPage = wx.BoxSizer(wx.HORIZONTAL)

        bSizer131 = wx.BoxSizer(wx.VERTICAL)

        self.cnxBtn01 = wx.Button(self, wx.ID_ANY, u"Poste 1", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer131.Add(self.cnxBtn01, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.cnxBtn02 = wx.Button(self, wx.ID_ANY, u"Poste 2", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer131.Add(self.cnxBtn02, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.cnxBtn03 = wx.Button(self, wx.ID_ANY, u"Poste 3", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer131.Add(self.cnxBtn03, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.fullPlace = wx.StaticText(self, wx.ID_ANY, u"no cnx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.fullPlace.Wrap(-1)

        bSizer131.Add(self.fullPlace, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        appPage.Add(bSizer131, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        boardSide = wx.BoxSizer(wx.VERTICAL)

        user01Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.pingUser01Btn = wx.Button(self, wx.ID_ANY, u"Ping", wx.DefaultPosition, wx.DefaultSize, 0)
        user01Infos.Add(self.pingUser01Btn, 0, wx.ALL, 5)

        self.user01Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user01Infos.Add(self.user01Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user01Deno = wx.StaticText(self, wx.ID_ANY, u"Poste 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user01Deno.Wrap(-1)

        user01Infos.Add(self.user01Deno, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide.Add(user01Infos, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        user02Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.pingUser02Btn = wx.Button(self, wx.ID_ANY, u"Ping", wx.DefaultPosition, wx.DefaultSize, 0)
        user02Infos.Add(self.pingUser02Btn, 0, wx.ALL, 5)

        self.user02Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user02Infos.Add(self.user02Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user02Deno = wx.StaticText(self, wx.ID_ANY, u"Poste 2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user02Deno.Wrap(-1)

        user02Infos.Add(self.user02Deno, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide.Add(user02Infos, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        user03Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.pingUser03Btn = wx.Button(self, wx.ID_ANY, u"Ping", wx.DefaultPosition, wx.DefaultSize, 0)
        user03Infos.Add(self.pingUser03Btn, 0, wx.ALL, 5)

        self.user03Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user03Infos.Add(self.user03Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user03Deno = wx.StaticText(self, wx.ID_ANY, u"Poste 3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user03Deno.Wrap(-1)

        user03Infos.Add(self.user03Deno, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide.Add(user03Infos, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.pingBtn = wx.Button(self, wx.ID_ANY, u"Tous", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer141.Add(self.pingBtn, 1, wx.ALL | wx.EXPAND, 5)

        boardSide.Add(bSizer141, 0, wx.EXPAND, 5)

        appPage.Add(boardSide, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.trafficLight = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/icons/feu01.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.trafficLight, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        appPage.Add(bSizer12, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        mainPage.Add(appPage, 0, wx.ALL | wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer13.Add(bSizer14, 0, wx.EXPAND, 5)

        self.chatTxt = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer13.Add(self.chatTxt, 1, wx.ALL | wx.EXPAND, 5)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        self.sendBtn = wx.Button(self, wx.ID_ANY, u"Envoyer", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.sendBtn, 0, wx.ALL, 5)

        self.msgText = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TE_PROCESS_ENTER)
        bSizer15.Add(self.msgText, 1, wx.ALL | wx.EXPAND, 5)

        bSizer13.Add(bSizer15, 0, wx.EXPAND, 5)

        mainPage.Add(bSizer13, 1, wx.ALL | wx.EXPAND, 5)

        self.mailBox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        mainPage.Add(self.mailBox, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(mainPage)
        self.Layout()
        self.statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.onMenuChangeMode, id=self.menuChangeMode.GetId())
        self.Bind(wx.EVT_MENU, self.onMenuQuit, id=self.menuQuit.GetId())
        self.cnxBtn01.Bind(wx.EVT_BUTTON, self.onCnxBtn01)
        self.cnxBtn02.Bind(wx.EVT_BUTTON, self.onCnxBtn02)
        self.cnxBtn03.Bind(wx.EVT_BUTTON, self.onCnxBtn03)
        self.pingUser01Btn.Bind(wx.EVT_BUTTON, self.onPingUser01Btn)
        self.pingUser02Btn.Bind(wx.EVT_BUTTON, self.onPingUser02Btn)
        self.pingUser03Btn.Bind(wx.EVT_BUTTON, self.onPingUser03Btn)
        self.pingBtn.Bind(wx.EVT_BUTTON, self.onPingBtn)
        self.sendBtn.Bind(wx.EVT_BUTTON, self.onSendBtn)
        self.msgText.Bind(wx.EVT_TEXT_ENTER, self.onSendBtn)
        self.mailBox.Bind(wx.EVT_TEXT, self.onImportChange)

        mainDisplay(self)

    def onImportChange(self, event):
        dataBrute = self.mailBox.GetValue()
        task = eval(dataBrute)

        jobs.put(task)

        while not jobs.empty():
            message = jobs.get()
            code = message['code']
            value = False
            if message['value']:
                value = message['value']
            decodeMsg(self, code, value)

        event.Skip()

    def sendMessageToServer(self, msg):
        cnxJSON = jsonpickle.encode(msg, unpicklable=False)
        self.protocol.sendLine(cnxJSON.encode('UTF-8'))

    def onMenuQuit(self, event):
        sendMessageToServer(self, 'userQuit', True)
        event.Skip()

    def onMenuChangeMode(self, event):
        if appSettings.isDemoMode:
            appSettings.isDemoMode = False
        else:
            appSettings.isDemoMode = True
        mainDisplay(self)
        event.Skip()

    def onCnxBtn01(self, event):
        userCnx = "user01"
        appSettings.userID = userCnx
        sendMessageToServer(self, 'userCnx', UserCnx(userCnx, userCnx))
        event.Skip()

    def onCnxBtn02(self, event):
        userCnx = "user02"
        appSettings.userID = userCnx
        sendMessageToServer(self, 'userCnx', UserCnx(userCnx, userCnx))
        event.Skip()

    def onCnxBtn03(self, event):
        userCnx = "user03"
        appSettings.userID = userCnx
        sendMessageToServer(self, 'userCnx', UserCnx(userCnx, userCnx))
        event.Skip()

    def onPingUser01Btn(self, event):
        sendMessageToServer(self, 'pingUser', "user01")
        event.Skip()

    def onPingUser02Btn(self, event):
        sendMessageToServer(self, 'pingUser', "user02")
        event.Skip()

    def onPingUser03Btn(self, event):
        sendMessageToServer(self, 'pingUser', "user03")
        event.Skip()

    def onPingBtn(self, event):
        sendMessageToServer(self, 'pingAll', True)
        event.Skip()

    def onLocalBtn(self, event):
        state = appSettings.bordLed
        state += 1
        if state >= 4:
            state = 1
        appSettings.bordLed = state
        mainDisplay(self)
        event.Skip()

    def onSendBtn(self, event):
        user = appSettings.userID
        nickname = appSettings.nickname
        msgToSend = self.msgText.GetValue()
        if msgToSend:
            sendMessageToServer(self, 'sendMsg', ChatMsg(user, nickname, msgToSend))
            self.msgText.SetValue("")
        event.Skip()
