# -*- coding: utf-8 -*-


import wx
import appSettings
from appcore.display.displayConnectedGame import displayConnectedGame

from controller import PublicPath
from appcore.translate import _


def mainBoardDisplay(self):
    msg = _("Connectez vous à une partie et bonnes cartes.")
    if appSettings.userIsLoggedIn:
        self.cnxTabCnxBtn.Disable()
        self.cnxTabUserEntry.Disable()
        self.cnxTabPasswordEntry.Disable()
        self.m_staticText2.Disable()
        self.m_staticText3.Disable()
        self.cnxTabCheckInfos.Disable()
        self.cnxTabLock.SetBitmap(wx.Bitmap(PublicPath("icons", appSettings.imgLock)))
        self.cnxTabNickName.SetLabel(appSettings.nickName)
        if appSettings.firstConnexion:
            msg = _("Connexion acceptée - Bienvenue et bonnes cartes.")
            if appSettings.profilePremium:
                msg = _("Connexion acceptée - Bienvenue ") + appSettings.nickName + _(" et bonnes cartes.")
            appSettings.firstConnexion = False

    if appSettings.profilePremium:
        if appSettings.userPlay:
            self.cnxTabCreateBtn.Disable()
        else:
            self.cnxTabCreateBtn.Enable()

    self.mainStatusBar.SetStatusText(msg, 0)
    displayConnectedGame(self)
    self.Layout()
