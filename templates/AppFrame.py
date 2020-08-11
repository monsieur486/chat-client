# -*- coding: utf-8 -*-


import jsonpickle
import wx.adv
import appSettings
import queue

from appcore.connexion.MessageToServer import MessageToServer
from appcore.connexion.UserCnx import UserCnx
from appcore.connexion.sendMessageToServer import sendMessageToServer
from appcore.decodeur.decodeMsg import decodeMsg
from appcore.display.firstDisplay import firstDisplay
from appcore.display.dialogMsg import dialogMsg
from appcore.display.playerLogoutDisplay import playerLogoutDisplay
from appcore.gameMsg.DeconnectGameInfos import DeconnectGameInfos
from appcore.gameMsg.GameCreateMsg import GameCreateMsg
from appcore.gameMsg.SelectPrivateGame import SelectPrivateGame
from appcore.translate import _

jobs = queue.Queue()


###########################################################################
# Class AppFrame
###########################################################################

class AppFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"AppPubSub", pos=wx.DefaultPosition,
                          size=wx.Size(262, 369), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Quitter" + u"\t" + u"ctrl-q",
                                       u"Quitter l'application", wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem1)

        self.m_menubar1.Append(self.m_menu1, u"Menu")

        self.SetMenuBar(self.m_menubar1)

        self.mainStatusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.connexionTab = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer45 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer46 = wx.BoxSizer(wx.VERTICAL)

        self.cnxTabLock1 = wx.StaticBitmap(self.connexionTab, wx.ID_ANY,
                                           wx.Bitmap(u"public/icons/16x16_user.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer46.Add(self.cnxTabLock1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabUserEntry = wx.TextCtrl(self.connexionTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer46.Add(self.cnxTabUserEntry, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabLock11 = wx.StaticBitmap(self.connexionTab, wx.ID_ANY,
                                            wx.Bitmap(u"public/icons/16x16_key.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer46.Add(self.cnxTabLock11, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabPasswordEntry = wx.TextCtrl(self.connexionTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        bSizer46.Add(self.cnxTabPasswordEntry, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabCnxBtn = wx.Button(self.connexionTab, wx.ID_ANY, u"Connexion", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer46.Add(self.cnxTabCnxBtn, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabCnxBtn1 = wx.Button(self.connexionTab, wx.ID_ANY, u"Déconnexion", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        bSizer46.Add(self.cnxTabCnxBtn1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer45.Add(bSizer46, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer50 = wx.BoxSizer(wx.VERTICAL)

        bSizer51 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabLock1111 = wx.StaticBitmap(self.connexionTab, wx.ID_ANY,
                                              wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer51.Add(self.cnxTabLock1111, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText451 = wx.StaticText(self.connexionTab, wx.ID_ANY, u"Poste 1", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText451.Wrap(-1)

        bSizer51.Add(self.m_staticText451, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer50.Add(bSizer51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer511 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabLock11111 = wx.StaticBitmap(self.connexionTab, wx.ID_ANY,
                                               wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer511.Add(self.cnxTabLock11111, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText4511 = wx.StaticText(self.connexionTab, wx.ID_ANY, u"Poste 2", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText4511.Wrap(-1)

        bSizer511.Add(self.m_staticText4511, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer50.Add(bSizer511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer513 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabLock11113 = wx.StaticBitmap(self.connexionTab, wx.ID_ANY,
                                               wx.Bitmap(u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer513.Add(self.cnxTabLock11113, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText4513 = wx.StaticText(self.connexionTab, wx.ID_ANY, u"Poste 3", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText4513.Wrap(-1)

        bSizer513.Add(self.m_staticText4513, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer50.Add(bSizer513, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_radioBox3Choices = [u"Actif", u"En Pause"]
        self.m_radioBox3 = wx.RadioBox(self.connexionTab, wx.ID_ANY, u"Disponibilité", wx.DefaultPosition,
                                       wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS)
        self.m_radioBox3.SetSelection(0)
        bSizer50.Add(self.m_radioBox3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        m_radioBox31Choices = [u"Production", u"Debug"]
        self.m_radioBox31 = wx.RadioBox(self.connexionTab, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize,
                                        m_radioBox31Choices, 1, wx.RA_SPECIFY_COLS)
        self.m_radioBox31.SetSelection(0)
        bSizer50.Add(self.m_radioBox31, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        bSizer45.Add(bSizer50, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.connexionTab.SetSizer(bSizer45)
        self.connexionTab.Layout()
        bSizer45.Fit(self.connexionTab)
        bSizer1.Add(self.connexionTab, 1, wx.EXPAND | wx.ALL, 5)

        self.mailBox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer1.Add(self.mailBox, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.onMenuQuit, id=self.m_menuItem1.GetId())
        self.cnxTabPasswordEntry.Bind(wx.EVT_TEXT_ENTER, self.cnxTabOnCnxBtn)
        self.cnxTabCnxBtn.Bind(wx.EVT_BUTTON, self.cnxTabOnCnxBtn)
        self.cnxTabCnxBtn1.Bind(wx.EVT_BUTTON, self.cnxTabOnCnxBtn)
        self.mailBox.Bind(wx.EVT_TEXT, self.onImportChange)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onMenuQuit(self, event):
        event.Skip()

    def cnxTabOnCnxBtn(self, event):
        event.Skip()

    def onImportChange(self, event):
        event.Skip()
