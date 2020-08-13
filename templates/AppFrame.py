# -*- coding: utf-8 -*-


import jsonpickle
import wx.adv
import queue
import appSettings
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
                          size=wx.Size(235, 324), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        connexionSide = wx.BoxSizer(wx.VERTICAL)

        self.userIcon = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/icons/16x16_user.png", wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.userIcon, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.userLogin = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.userLogin.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        connexionSide.Add(self.userLogin, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND,
                          5)

        self.pwdIcon = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/icons/16x16_key.png", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.pwdIcon, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.userPwd = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.userPwd.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        connexionSide.Add(self.userPwd, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND,
                          5)

        self.cnxBtn = wx.Button(self, wx.ID_ANY, u"Connexion", wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.cnxBtn, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.dispoBtn = wx.Button(self, wx.ID_ANY, u"Disponible", wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.dispoBtn, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.afkBtn = wx.Button(self, wx.ID_ANY, u"En Pause", wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.afkBtn, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        appPage.Add(connexionSide, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide = wx.BoxSizer(wx.VERTICAL)

        user01Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user01Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user01Infos.Add(self.user01Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user01Deno = wx.StaticText(self, wx.ID_ANY, u"Poste 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user01Deno.Wrap(-1)

        user01Infos.Add(self.user01Deno, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide.Add(user01Infos, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        user02Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user02Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user02Infos.Add(self.user02Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user02Deno = wx.StaticText(self, wx.ID_ANY, u"Poste 2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user02Deno.Wrap(-1)

        user02Infos.Add(self.user02Deno, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide.Add(user02Infos, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        user03Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user03Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user03Infos.Add(self.user03Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user03Deno = wx.StaticText(self, wx.ID_ANY, u"Poste 3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user03Deno.Wrap(-1)

        user03Infos.Add(self.user03Deno, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide.Add(user03Infos, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        user04Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user04Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user04Infos.Add(self.user04Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user04Deno = wx.StaticText(self, wx.ID_ANY, u"Poste 4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user04Deno.Wrap(-1)

        user04Infos.Add(self.user04Deno, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide.Add(user04Infos, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        appPage.Add(boardSide, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        mainPage.Add(appPage, 1, wx.ALL | wx.EXPAND, 5)

        self.mailBox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        mainPage.Add(self.mailBox, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(mainPage)
        self.Layout()
        self.statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.onMenuChangeMode, id=self.menuChangeMode.GetId())
        self.Bind(wx.EVT_MENU, self.onMenuQuit, id=self.menuQuit.GetId())
        self.userPwd.Bind(wx.EVT_TEXT_ENTER, self.onCnxBtn)
        self.cnxBtn.Bind(wx.EVT_BUTTON, self.onCnxBtn)
        self.dispoBtn.Bind(wx.EVT_BUTTON, self.onDispoBtn)
        self.afkBtn.Bind(wx.EVT_BUTTON, self.onAfkBtn)
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

    def onCnxBtn(self, event):
        userCnx = self.userLogin.GetValue()
        passwordCnx = self.userPwd.GetValue()
        appSettings.user = userCnx
        sendMessageToServer(self, 'userCnx', UserCnx(userCnx, passwordCnx))
        event.Skip()

    def onAfkBtn(self, event):
        sendMessageToServer(self, 'userPause', appSettings.user)
        event.Skip()

    def onDispoBtn(self, event):
        sendMessageToServer(self, 'userDispo', appSettings.user)
        event.Skip()
