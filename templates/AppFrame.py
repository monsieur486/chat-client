# -*- coding: utf-8 -*-


import jsonpickle
import wx.adv
import queue

from appcore.connexion.sendMessageToServer import sendMessageToServer
from appcore.decodeur.decodeMsg import decodeMsg

jobs = queue.Queue()


###########################################################################
# Class AppFrame
###########################################################################

class AppFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"AppPubSub", pos=wx.DefaultPosition,
                          size=wx.Size(262, 305), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.protocol = None

        self.menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Quitter" + u"\t" + u"ctrl-q",
                                       u"Quitter l'application", wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem1)

        self.menubar1.Append(self.m_menu1, u"Menu")

        self.SetMenuBar(self.menubar1)

        mainPage = wx.BoxSizer(wx.VERTICAL)

        mainPage.Add((0, 0), 1, wx.EXPAND, 5)

        appPage = wx.BoxSizer(wx.HORIZONTAL)

        connexionSide = wx.BoxSizer(wx.VERTICAL)

        self.userIcon = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/icons/16x16_user.png", wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.userIcon, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.userLogin = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.userLogin, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.pwdIcon = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/icons/16x16_key.png", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.pwdIcon, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.userPwd = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        connexionSide.Add(self.userPwd, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxBtn = wx.Button(self, wx.ID_ANY, u"Connexion", wx.DefaultPosition, wx.DefaultSize, 0)
        connexionSide.Add(self.cnxBtn, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        appPage.Add(connexionSide, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        boardSide = wx.BoxSizer(wx.VERTICAL)

        user01Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user01Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user01Infos.Add(self.user01Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user01Deno = wx.StaticText(self, wx.ID_ANY, u"User01", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user01Deno.Wrap(-1)

        user01Infos.Add(self.user01Deno, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        boardSide.Add(user01Infos, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        user02Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user02Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user02Infos.Add(self.user02Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user02Deno = wx.StaticText(self, wx.ID_ANY, u"User02", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user02Deno.Wrap(-1)

        user02Infos.Add(self.user02Deno, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        boardSide.Add(user02Infos, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        user03Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user03Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user03Infos.Add(self.user03Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user03Deno = wx.StaticText(self, wx.ID_ANY, u"User03", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user03Deno.Wrap(-1)

        user03Infos.Add(self.user03Deno, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        boardSide.Add(user03Infos, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        user04Infos = wx.BoxSizer(wx.HORIZONTAL)

        self.user04Led = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        user04Infos.Add(self.user04Led, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.user04Deno = wx.StaticText(self, wx.ID_ANY, u"User04", wx.DefaultPosition, wx.DefaultSize, 0)
        self.user04Deno.Wrap(-1)

        user04Infos.Add(self.user04Deno, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        boardSide.Add(user04Infos, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.dispoBtn = wx.Button(self, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0)
        boardSide.Add(self.dispoBtn, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        appPage.Add(boardSide, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        mainPage.Add(appPage, 0, wx.ALL | wx.EXPAND, 5)

        mainPage.Add((0, 0), 1, wx.EXPAND, 5)

        self.mailBox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        mainPage.Add(self.mailBox, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(mainPage)
        self.Layout()
        self.statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.onMenuQuit, id=self.m_menuItem1.GetId())
        self.userPwd.Bind(wx.EVT_TEXT_ENTER, self.cnxCnxBtn)
        self.cnxBtn.Bind(wx.EVT_BUTTON, self.cnxCnxBtn)
        self.dispoBtn.Bind(wx.EVT_BUTTON, self.onDispoBtn)
        self.mailBox.Bind(wx.EVT_TEXT, self.onImportChange)

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
        sendMessageToServer(self, 'userDecnx', True)
        event.Skip()

    def cnxCnxBtn(self, event):
        event.Skip()

    def onDispoBtn(self, event):
        event.Skip()
