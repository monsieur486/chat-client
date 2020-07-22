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


class ChienDialog(wx.Dialog):
    def __init__(self, parent, title):
        super(ChienDialog, self).__init__(parent, title=title, size=(680, 300))
        bSizer138 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText224 = wx.StaticText(self, wx.ID_ANY, _(u"LE CHIEN"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText224.Wrap(-1)

        bSizer138.Add(self.m_staticText224, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer139 = wx.BoxSizer(wx.HORIZONTAL)

        self.gameTabNordCard = wx.StaticBitmap(self, wx.ID_ANY,
                                               wx.Bitmap(u"public/bigsCards/0_0.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer139.Add(self.gameTabNordCard, 0, wx.ALL, 5)

        self.gameTabNordCard1 = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/bigsCards/0_0.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.gameTabNordCard1, 0, wx.ALL, 5)

        self.gameTabNordCard2 = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/bigsCards/0_0.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.gameTabNordCard2, 0, wx.ALL, 5)

        self.gameTabNordCard3 = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/bigsCards/0_0.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.gameTabNordCard3, 0, wx.ALL, 5)

        self.gameTabNordCard4 = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/bigsCards/0_0.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.gameTabNordCard4, 0, wx.ALL, 5)

        self.gameTabNordCard5 = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/bigsCards/0_0.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.gameTabNordCard5, 0, wx.ALL, 5)

        bSizer138.Add(bSizer139, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_button67 = wx.Button(self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer138.Add(self.m_button67, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer138)

        self.m_staticText224.SetLabel(appSettings.user)


###########################################################################
# Class AppFrame
###########################################################################

class AppFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=_(u"Le Tarot des Copains"),
                          pos=wx.DefaultPosition,
                          size=wx.Size(1200, 900),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.protocol = None

        frame_size = self.GetSize()
        appSettings.card_H = round(frame_size[1] / appSettings.card_C)
        appSettings.card_L = round(appSettings.card_H / 1.875)
        appSettings.card_CL = round(appSettings.card_H / 3)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, _(u"Quitter") + u"\t" + u"ctrl-q",
                                       _(u"Quitter l'application"), wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem1)

        self.m_menubar1.Append(self.m_menu1, _(u"Menu"))

        self.SetMenuBar(self.m_menubar1)

        self.mainStatusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.connexionTab = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer612 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer99 = wx.BoxSizer(wx.VERTICAL)

        sbSizer39 = wx.StaticBoxSizer(wx.StaticBox(self.connexionTab, wx.ID_ANY, _(u"Connexion")), wx.VERTICAL)

        bSizer63 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"Utilisateur"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer63.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabUserEntry = wx.TextCtrl(sbSizer39.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer63.Add(self.cnxTabUserEntry, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer39.Add(bSizer63, 0, wx.ALL | wx.EXPAND, 5)

        bSizer62 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"Mot de passe"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer62.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabPasswordEntry = wx.TextCtrl(sbSizer39.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        bSizer62.Add(self.cnxTabPasswordEntry, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabCheckInfos = wx.CheckBox(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"Mémoriser"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bSizer62.Add(self.cnxTabCheckInfos, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer39.Add(bSizer62, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        self.cnxTabCnxBtn = wx.Button(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"Connexion"), wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer5.Add(self.cnxTabCnxBtn, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabLock = wx.StaticBitmap(sbSizer39.GetStaticBox(), wx.ID_ANY,
                                          wx.Bitmap(u"public/icons/disconnected.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.cnxTabLock, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText54 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"Pseudo :"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)

        bSizer5.Add(self.m_staticText54, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabNickName = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.cnxTabNickName.Wrap(-1)

        bSizer5.Add(self.cnxTabNickName, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer39.Add(bSizer5, 0, 0, 5)

        bSizer703 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer871 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabPremiumValidity = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"Premium jusqu'au :"),
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.cnxTabPremiumValidity.Wrap(-1)

        bSizer871.Add(self.cnxTabPremiumValidity, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText112 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText112.Wrap(-1)

        bSizer871.Add(self.m_staticText112, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer703.Add(bSizer871, 1, wx.EXPAND, 5)

        bSizer881 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink1 = wx.adv.HyperlinkCtrl(sbSizer39.GetStaticBox(), wx.ID_ANY, _(u"Plus d'infos"),
                                                 u"https://tarot.mr486.com/fr/tarot/", wx.DefaultPosition,
                                                 wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        bSizer881.Add(self.m_hyperlink1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer703.Add(bSizer881, 1, wx.EXPAND, 5)

        sbSizer39.Add(bSizer703, 0, wx.EXPAND, 5)

        bSizer99.Add(sbSizer39, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer22 = wx.StaticBoxSizer(wx.StaticBox(self.connexionTab, wx.ID_ANY, _(u"Rejoindre une partie")),
                                      wx.VERTICAL)

        bSizer72 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer222 = wx.StaticBoxSizer(wx.StaticBox(sbSizer22.GetStaticBox(), wx.ID_ANY, _(u"4 joueurs")), wx.VERTICAL)

        bSizer67 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFree4Lbl = wx.StaticText(sbSizer222.GetStaticBox(), wx.ID_ANY, _(u"Partie libre :"),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.cnxTabFree4Lbl.Wrap(-1)

        bSizer67.Add(self.cnxTabFree4Lbl, 0, wx.ALL, 5)

        sbSizer222.Add(bSizer67, 1, wx.EXPAND, 5)

        self.cnxTabPlay4 = wx.Button(sbSizer222.GetStaticBox(), wx.ID_ANY, _(u"Jouer"), wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        sbSizer222.Add(self.cnxTabPlay4, 0, wx.ALL | wx.EXPAND, 5)

        bSizer72.Add(sbSizer222, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer2221 = wx.StaticBoxSizer(wx.StaticBox(sbSizer22.GetStaticBox(), wx.ID_ANY, _(u"5 joueurs")), wx.VERTICAL)

        bSizer671 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFree5Lbl = wx.StaticText(sbSizer2221.GetStaticBox(), wx.ID_ANY, _(u"Partie libre :"),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.cnxTabFree5Lbl.Wrap(-1)

        bSizer671.Add(self.cnxTabFree5Lbl, 0, wx.ALL, 5)

        sbSizer2221.Add(bSizer671, 1, wx.EXPAND, 5)

        self.cnxTabPlay5 = wx.Button(sbSizer2221.GetStaticBox(), wx.ID_ANY, _(u"Jouer"), wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        sbSizer2221.Add(self.cnxTabPlay5, 0, wx.ALL | wx.EXPAND, 5)

        bSizer72.Add(sbSizer2221, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer22.Add(bSizer72, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer21 = wx.StaticBoxSizer(wx.StaticBox(sbSizer22.GetStaticBox(), wx.ID_ANY, _(u"Parties Privées")),
                                      wx.VERTICAL)

        bSizer74 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1101 = wx.StaticText(sbSizer21.GetStaticBox(), wx.ID_ANY, _(u"Dénomination :"),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1101.Wrap(-1)

        bSizer74.Add(self.m_staticText1101, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabPrivateTitle = wx.StaticText(sbSizer21.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.cnxTabPrivateTitle.Wrap(-1)

        bSizer74.Add(self.cnxTabPrivateTitle, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer21.Add(bSizer74, 0, wx.ALL | wx.EXPAND, 5)

        bSizer82 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText42 = wx.StaticText(sbSizer21.GetStaticBox(), wx.ID_ANY, _(u"Mot de passe :"),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText42.Wrap(-1)

        bSizer82.Add(self.m_staticText42, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabSearchPwd = wx.TextCtrl(sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PASSWORD)
        bSizer82.Add(self.cnxTabSearchPwd, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabJoinBtn = wx.Button(sbSizer21.GetStaticBox(), wx.ID_ANY, _(u"Rejoindre"), wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer82.Add(self.cnxTabJoinBtn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer21.Add(bSizer82, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer22.Add(sbSizer21, 0, wx.ALL | wx.EXPAND, 5)

        self.cnxTabGamesList = wx.ListCtrl(sbSizer22.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           style=wx.LC_REPORT |
                                                 wx.BORDER_SUNKEN |
                                                 wx.LC_SORT_ASCENDING |
                                                 wx.LC_SINGLE_SEL)

        self.cnxTabGamesList.InsertColumn(0, "#")
        self.cnxTabGamesList.InsertColumn(1, _("Joueurs"))
        self.cnxTabGamesList.InsertColumn(2, _("Nom"))
        self.cnxTabGamesList.SetColumnWidth(0, 0)
        self.cnxTabGamesList.SetColumnWidth(1, 80)
        self.cnxTabGamesList.SetColumnWidth(2, 350)

        sbSizer22.Add(self.cnxTabGamesList, 1, wx.ALL | wx.EXPAND, 5)

        bSizer75 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabNbPlayersLbl = wx.StaticText(sbSizer22.GetStaticBox(), wx.ID_ANY, _(u"Joueur connecté :"),
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.cnxTabNbPlayersLbl.Wrap(-1)

        bSizer75.Add(self.cnxTabNbPlayersLbl, 1, wx.ALL, 5)

        self.cnxTabNbGamesLbl = wx.StaticText(sbSizer22.GetStaticBox(), wx.ID_ANY, _(u"Partie :"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.cnxTabNbGamesLbl.Wrap(-1)

        bSizer75.Add(self.cnxTabNbGamesLbl, 1, wx.ALL, 5)

        sbSizer22.Add(bSizer75, 0, wx.ALL | wx.EXPAND, 5)

        bSizer99.Add(sbSizer22, 1, wx.ALL | wx.EXPAND, 5)

        bSizer612.Add(bSizer99, 1, wx.ALL | wx.EXPAND, 5)

        bSizer98 = wx.BoxSizer(wx.VERTICAL)

        sbSizer221 = wx.StaticBoxSizer(wx.StaticBox(self.connexionTab, wx.ID_ANY, _(u"Créer une partie")), wx.VERTICAL)

        bSizer721 = wx.BoxSizer(wx.HORIZONTAL)

        cnxTabCreateChoicePlayersChoices = [_(u"4"), _(u"5")]
        self.cnxTabCreateChoicePlayers = wx.RadioBox(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Joueurs"),
                                                     wx.DefaultPosition, wx.DefaultSize,
                                                     cnxTabCreateChoicePlayersChoices, 1, wx.RA_SPECIFY_COLS)
        self.cnxTabCreateChoicePlayers.SetSelection(0)
        bSizer721.Add(self.cnxTabCreateChoicePlayers, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabCreateBtn = wx.Button(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Créer"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer721.Add(self.cnxTabCreateBtn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer44 = wx.StaticBoxSizer(wx.StaticBox(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Compte Premium")),
                                      wx.VERTICAL)

        bSizer821 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText107 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, _(u"Dénomination"),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText107.Wrap(-1)

        bSizer821.Add(self.m_staticText107, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabCreateDenomination = wx.TextCtrl(sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer821.Add(self.cnxTabCreateDenomination, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer44.Add(bSizer821, 0, wx.ALL | wx.EXPAND, 5)

        bSizer100 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabCreatePrivate = wx.CheckBox(sbSizer44.GetStaticBox(), wx.ID_ANY, _(u"Privé"), wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer100.Add(self.cnxTabCreatePrivate, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText110 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, _(u"Mot de passe"),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText110.Wrap(-1)

        bSizer100.Add(self.m_staticText110, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabCreatePassword = wx.TextCtrl(sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        bSizer100.Add(self.cnxTabCreatePassword, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer44.Add(bSizer100, 1, wx.EXPAND, 5)

        bSizer721.Add(sbSizer44, 1, wx.EXPAND, 5)

        sbSizer221.Add(bSizer721, 0, wx.ALL | wx.EXPAND, 5)

        bSizer76 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer24 = wx.StaticBoxSizer(wx.StaticBox(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Options")), wx.VERTICAL)

        self.cnxTabOptionsSA = wx.CheckBox(sbSizer24.GetStaticBox(), wx.ID_ANY, _(u"Sans Annonce"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sbSizer24.Add(self.cnxTabOptionsSA, 0, wx.ALL, 5)

        self.cnxTabOptionsAR = wx.CheckBox(sbSizer24.GetStaticBox(), wx.ID_ANY, _(u"Avec Relance"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sbSizer24.Add(self.cnxTabOptionsAR, 0, wx.ALL, 5)

        self.cnxTabOptionsSC = wx.CheckBox(sbSizer24.GetStaticBox(), wx.ID_ANY, _(u"Sans Chat"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sbSizer24.Add(self.cnxTabOptionsSC, 0, wx.ALL, 5)

        self.cnxTabOptionsArrondi = wx.CheckBox(sbSizer24.GetStaticBox(), wx.ID_ANY, _(u"Arrondir les scores"),
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer24.Add(self.cnxTabOptionsArrondi, 0, wx.ALL, 5)

        self.cnxTabOptionsAB = wx.CheckBox(sbSizer24.GetStaticBox(), wx.ID_ANY, _(u"Belge"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sbSizer24.Add(self.cnxTabOptionsAB, 0, wx.ALL, 5)

        bSizer76.Add(sbSizer24, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer25 = wx.StaticBoxSizer(wx.StaticBox(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Contrats")), wx.VERTICAL)

        self.cnxTabOptionsPetie = wx.CheckBox(sbSizer25.GetStaticBox(), wx.ID_ANY, _(u"Petite"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.cnxTabOptionsPetie.SetValue(True)
        sbSizer25.Add(self.cnxTabOptionsPetie, 0, wx.ALL, 5)

        self.cnxTabOptionsGarde = wx.CheckBox(sbSizer25.GetStaticBox(), wx.ID_ANY, _(u"Garde"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.cnxTabOptionsGarde.SetValue(True)
        sbSizer25.Add(self.cnxTabOptionsGarde, 0, wx.ALL, 5)

        self.cnxTabOptionsGardeSans = wx.CheckBox(sbSizer25.GetStaticBox(), wx.ID_ANY, _(u"Garde Sans"),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.cnxTabOptionsGardeSans.SetValue(True)
        sbSizer25.Add(self.cnxTabOptionsGardeSans, 0, wx.ALL, 5)

        self.m_checkBox111 = wx.CheckBox(sbSizer25.GetStaticBox(), wx.ID_ANY, _(u"Garde Contre"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.m_checkBox111.SetValue(True)
        self.m_checkBox111.Enable(False)

        sbSizer25.Add(self.m_checkBox111, 0, wx.ALL, 5)

        self.m_checkBox1111 = wx.CheckBox(sbSizer25.GetStaticBox(), wx.ID_ANY, _(u"Chelem"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.m_checkBox1111.SetValue(True)
        self.m_checkBox1111.Enable(False)

        sbSizer25.Add(self.m_checkBox1111, 0, wx.ALL, 5)

        bSizer76.Add(sbSizer25, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer221.Add(bSizer76, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer821 = wx.StaticBoxSizer(wx.StaticBox(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Etat")), wx.VERTICAL)

        self.cnxTabFicheGameState = wx.StaticText(sbSizer821.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                  wx.Size(300, -1), 0)
        self.cnxTabFicheGameState.Wrap(-1)

        sbSizer821.Add(self.cnxTabFicheGameState, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer221.Add(sbSizer821, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer81 = wx.StaticBoxSizer(wx.StaticBox(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Joueurs")), wx.VERTICAL)

        bSizer823 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer83 = wx.BoxSizer(wx.VERTICAL)

        bSizer1741 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFichePly1Led = wx.StaticBitmap(sbSizer81.GetStaticBox(), wx.ID_ANY,
                                                  wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1741.Add(self.cnxTabFichePly1Led, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cnxTabFichePly1Nickname = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                     wx.Size(-1, -1), 0)
        self.cnxTabFichePly1Nickname.Wrap(-1)

        bSizer1741.Add(self.cnxTabFichePly1Nickname, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer83.Add(bSizer1741, 0, wx.ALL, 5)

        bSizer171 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFichePly2Led = wx.StaticBitmap(sbSizer81.GetStaticBox(), wx.ID_ANY,
                                                  wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer171.Add(self.cnxTabFichePly2Led, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cnxTabFichePly2Nickname = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                     wx.Size(-1, -1), 0)
        self.cnxTabFichePly2Nickname.Wrap(-1)

        bSizer171.Add(self.cnxTabFichePly2Nickname, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer83.Add(bSizer171, 0, wx.ALL, 5)

        bSizer172 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFichePly3Led = wx.StaticBitmap(sbSizer81.GetStaticBox(), wx.ID_ANY,
                                                  wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer172.Add(self.cnxTabFichePly3Led, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cnxTabFichePly3Nickname = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                     wx.Size(-1, -1), 0)
        self.cnxTabFichePly3Nickname.Wrap(-1)

        bSizer172.Add(self.cnxTabFichePly3Nickname, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer83.Add(bSizer172, 0, wx.ALL, 5)

        bSizer173 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFichePly4Led = wx.StaticBitmap(sbSizer81.GetStaticBox(), wx.ID_ANY,
                                                  wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer173.Add(self.cnxTabFichePly4Led, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cnxTabFichePly4Nickname = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                     wx.Size(-1, -1), 0)
        self.cnxTabFichePly4Nickname.Wrap(-1)

        bSizer173.Add(self.cnxTabFichePly4Nickname, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer83.Add(bSizer173, 0, wx.ALL, 5)

        bSizer174 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFichePly5Led = wx.StaticBitmap(sbSizer81.GetStaticBox(), wx.ID_ANY,
                                                  wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer174.Add(self.cnxTabFichePly5Led, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cnxTabFichePly5Nickname = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                     wx.Size(-1, -1), 0)
        self.cnxTabFichePly5Nickname.Wrap(-1)

        bSizer174.Add(self.cnxTabFichePly5Nickname, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer83.Add(bSizer174, 0, wx.ALL, 5)

        bSizer823.Add(bSizer83, 1, wx.EXPAND, 5)

        bSizer84 = wx.BoxSizer(wx.VERTICAL)

        self.cnxTabPly1Change = wx.Button(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"Remplacer"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer84.Add(self.cnxTabPly1Change, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabPly2Change = wx.Button(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"Remplacer"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer84.Add(self.cnxTabPly2Change, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabPly3Change = wx.Button(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"Remplacer"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer84.Add(self.cnxTabPly3Change, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabPly4Change = wx.Button(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"Remplacer"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer84.Add(self.cnxTabPly4Change, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabPly5Change = wx.Button(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"Remplacer"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer84.Add(self.cnxTabPly5Change, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer823.Add(bSizer84, 1, wx.EXPAND, 5)

        sbSizer81.Add(bSizer823, 1, wx.EXPAND, 5)

        bSizer89 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer135 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabCaptainLed = wx.StaticBitmap(sbSizer81.GetStaticBox(), wx.ID_ANY,
                                                wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer135.Add(self.cnxTabCaptainLed, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText1121 = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"Captain"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1121.Wrap(-1)

        bSizer135.Add(self.m_staticText1121, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer89.Add(bSizer135, 1, wx.EXPAND, 5)

        bSizer136 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText223 = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"Joueurs : "), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText223.Wrap(-1)

        bSizer136.Add(self.m_staticText223, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabFicheGameInfos = wx.StaticText(sbSizer81.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.cnxTabFicheGameInfos.Wrap(-1)

        bSizer136.Add(self.cnxTabFicheGameInfos, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer89.Add(bSizer136, 1, wx.EXPAND, 5)

        sbSizer81.Add(bSizer89, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer221.Add(sbSizer81, 0, wx.ALL | wx.EXPAND, 5)

        bSizer102 = wx.BoxSizer(wx.VERTICAL)

        self.cnxTabLeave = wx.Button(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Quitter la partie"), wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizer102.Add(self.cnxTabLeave, 1, wx.ALL | wx.EXPAND, 5)

        self.cnxTabFicheGameStart = wx.Button(sbSizer221.GetStaticBox(), wx.ID_ANY, _(u"Démarer la Partie"),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer102.Add(self.cnxTabFicheGameStart, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer221.Add(bSizer102, 0, wx.EXPAND, 5)

        bSizer98.Add(sbSizer221, 1, wx.ALL | wx.EXPAND, 5)

        bSizer612.Add(bSizer98, 1, wx.ALL | wx.EXPAND, 5)

        self.connexionTab.SetSizer(bSizer612)
        self.connexionTab.Layout()
        bSizer612.Fit(self.connexionTab)
        self.m_notebook1.AddPage(self.connexionTab, _(u"Connexion"), True)
        self.settingsTab = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        bSizer49 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer45 = wx.StaticBoxSizer(wx.StaticBox(self.settingsTab, wx.ID_ANY, _(u"Langues")), wx.HORIZONTAL)

        sbSizer45.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_bpButton142 = wx.BitmapButton(sbSizer45.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                             wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton142.SetBitmap(wx.Bitmap(u"public/flags/flag_fr.png", wx.BITMAP_TYPE_ANY))
        sbSizer45.Add(self.m_bpButton142, 0, wx.ALL, 5)

        self.m_bpButton1421 = wx.BitmapButton(sbSizer45.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton1421.SetBitmap(wx.Bitmap(u"public/flags/flag_en.png", wx.BITMAP_TYPE_ANY))
        sbSizer45.Add(self.m_bpButton1421, 0, wx.ALL, 5)

        self.m_bpButton1422 = wx.BitmapButton(sbSizer45.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton1422.SetBitmap(wx.Bitmap(u"public/flags/flag_de.png", wx.BITMAP_TYPE_ANY))
        sbSizer45.Add(self.m_bpButton1422, 0, wx.ALL, 5)

        self.m_bpButton1423 = wx.BitmapButton(sbSizer45.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton1423.SetBitmap(wx.Bitmap(u"public/flags/flag_nl.png", wx.BITMAP_TYPE_ANY))
        sbSizer45.Add(self.m_bpButton1423, 0, wx.ALL, 5)

        self.m_bpButton1424 = wx.BitmapButton(sbSizer45.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton1424.SetBitmap(wx.Bitmap(u"public/flags/flag_es.png", wx.BITMAP_TYPE_ANY))
        sbSizer45.Add(self.m_bpButton1424, 0, wx.ALL, 5)

        self.m_bpButton1425 = wx.BitmapButton(sbSizer45.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton1425.SetBitmap(wx.Bitmap(u"public/flags/flag_it.png", wx.BITMAP_TYPE_ANY))
        sbSizer45.Add(self.m_bpButton1425, 0, wx.ALL, 5)

        self.m_bpButton1426 = wx.BitmapButton(sbSizer45.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton1426.SetBitmap(wx.Bitmap(u"public/flags/flag_pt.png", wx.BITMAP_TYPE_ANY))
        sbSizer45.Add(self.m_bpButton1426, 0, wx.ALL, 5)

        sbSizer45.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer49.Add(sbSizer45, 0, wx.EXPAND, 5)

        bSizer49.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer31.Add(bSizer49, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 20)

        bSizer50 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer50.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer161 = wx.StaticBoxSizer(wx.StaticBox(self.settingsTab, wx.ID_ANY, _(u"Arrengements des cartes")),
                                       wx.HORIZONTAL)

        sbSizer161.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer171 = wx.StaticBoxSizer(wx.StaticBox(sbSizer161.GetStaticBox(), wx.ID_ANY, _(u"Pos 1")), wx.VERTICAL)

        self.m_bpButton11 = wx.BitmapButton(sbSizer171.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                            wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton11.SetBitmap(wx.Bitmap(u"public/cards/1_0.png", wx.BITMAP_TYPE_ANY))
        sbSizer171.Add(self.m_bpButton11, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer321 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button151 = wx.Button(sbSizer171.GetStaticBox(), wx.ID_ANY, _(u">"), wx.DefaultPosition, wx.DefaultSize,
                                     0)
        bSizer321.Add(self.m_button151, 0, wx.ALL, 2)

        sbSizer171.Add(bSizer321, 1, wx.EXPAND, 5)

        sbSizer161.Add(sbSizer171, 0, wx.ALL, 5)

        sbSizer172 = wx.StaticBoxSizer(wx.StaticBox(sbSizer161.GetStaticBox(), wx.ID_ANY, _(u"Pos 2")), wx.VERTICAL)

        self.m_bpButton12 = wx.BitmapButton(sbSizer172.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                            wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton12.SetBitmap(wx.Bitmap(u"public/cards/2_0.png", wx.BITMAP_TYPE_ANY))
        sbSizer172.Add(self.m_bpButton12, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer322 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1422 = wx.Button(sbSizer172.GetStaticBox(), wx.ID_ANY, _(u"<"), wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bSizer322.Add(self.m_button1422, 0, wx.ALL, 2)

        self.m_button152 = wx.Button(sbSizer172.GetStaticBox(), wx.ID_ANY, _(u">"), wx.DefaultPosition, wx.DefaultSize,
                                     0)
        bSizer322.Add(self.m_button152, 0, wx.ALL, 2)

        sbSizer172.Add(bSizer322, 1, wx.EXPAND, 5)

        sbSizer161.Add(sbSizer172, 0, wx.ALL, 5)

        sbSizer173 = wx.StaticBoxSizer(wx.StaticBox(sbSizer161.GetStaticBox(), wx.ID_ANY, _(u"Pos 3")), wx.VERTICAL)

        self.m_bpButton13 = wx.BitmapButton(sbSizer173.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                            wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton13.SetBitmap(wx.Bitmap(u"public/cards/3_0.png", wx.BITMAP_TYPE_ANY))
        sbSizer173.Add(self.m_bpButton13, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer323 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1423 = wx.Button(sbSizer173.GetStaticBox(), wx.ID_ANY, _(u"<"), wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bSizer323.Add(self.m_button1423, 0, wx.ALL, 2)

        self.m_button153 = wx.Button(sbSizer173.GetStaticBox(), wx.ID_ANY, _(u">"), wx.DefaultPosition, wx.DefaultSize,
                                     0)
        bSizer323.Add(self.m_button153, 0, wx.ALL, 2)

        sbSizer173.Add(bSizer323, 1, wx.EXPAND, 5)

        sbSizer161.Add(sbSizer173, 0, wx.ALL, 5)

        sbSizer174 = wx.StaticBoxSizer(wx.StaticBox(sbSizer161.GetStaticBox(), wx.ID_ANY, _(u"Pos 4")), wx.VERTICAL)

        self.m_bpButton14 = wx.BitmapButton(sbSizer174.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                            wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton14.SetBitmap(wx.Bitmap(u"public/cards/4_0.png", wx.BITMAP_TYPE_ANY))
        sbSizer174.Add(self.m_bpButton14, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer324 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1424 = wx.Button(sbSizer174.GetStaticBox(), wx.ID_ANY, _(u"<"), wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bSizer324.Add(self.m_button1424, 0, wx.ALL, 2)

        self.m_button154 = wx.Button(sbSizer174.GetStaticBox(), wx.ID_ANY, _(u">"), wx.DefaultPosition, wx.DefaultSize,
                                     0)
        bSizer324.Add(self.m_button154, 0, wx.ALL, 2)

        sbSizer174.Add(bSizer324, 1, wx.EXPAND, 5)

        sbSizer161.Add(sbSizer174, 0, wx.ALL, 5)

        sbSizer1741 = wx.StaticBoxSizer(wx.StaticBox(sbSizer161.GetStaticBox(), wx.ID_ANY, _(u"Pos 5")), wx.VERTICAL)

        self.m_bpButton141 = wx.BitmapButton(sbSizer1741.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                             wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton141.SetBitmap(wx.Bitmap(u"public/cards/6_0.png", wx.BITMAP_TYPE_ANY))
        sbSizer1741.Add(self.m_bpButton141, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer3241 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button14241 = wx.Button(sbSizer1741.GetStaticBox(), wx.ID_ANY, _(u"<"), wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer3241.Add(self.m_button14241, 0, wx.ALL, 2)

        self.m_button1541 = wx.Button(sbSizer1741.GetStaticBox(), wx.ID_ANY, _(u">"), wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer3241.Add(self.m_button1541, 0, wx.ALL, 2)

        sbSizer1741.Add(bSizer3241, 1, wx.EXPAND, 5)

        sbSizer161.Add(sbSizer1741, 0, wx.ALL, 5)

        sbSizer17411 = wx.StaticBoxSizer(wx.StaticBox(sbSizer161.GetStaticBox(), wx.ID_ANY, _(u"Pos 6")), wx.VERTICAL)

        self.m_bpButton1411 = wx.BitmapButton(sbSizer17411.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, wx.BU_AUTODRAW | 0)

        self.m_bpButton1411.SetBitmap(wx.Bitmap(u"public/cards/5_0.png", wx.BITMAP_TYPE_ANY))
        sbSizer17411.Add(self.m_bpButton1411, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer32411 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button142411 = wx.Button(sbSizer17411.GetStaticBox(), wx.ID_ANY, _(u"<"), wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer32411.Add(self.m_button142411, 0, wx.ALL, 2)

        sbSizer17411.Add(bSizer32411, 1, wx.EXPAND, 5)

        sbSizer161.Add(sbSizer17411, 0, wx.ALL, 5)

        sbSizer161.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer50.Add(sbSizer161, 0, wx.EXPAND, 5)

        bSizer50.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer31.Add(bSizer50, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 20)

        self.m_staticText36 = wx.StaticText(self.settingsTab, wx.ID_ANY, _(
            u"En cliquant sur une couleur on change l'odre d'affichage : de l'As au roi ou inversement"),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText36.Wrap(-1)

        bSizer31.Add(self.m_staticText36, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer45 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer45.Add((0, 0), 1, wx.EXPAND, 5)

        m_radioBox9Choices = [_(u"Anti-Horaire"), _(u"Horaire")]
        self.m_radioBox9 = wx.RadioBox(self.settingsTab, wx.ID_ANY, _(u"Sens du jeu"), wx.DefaultPosition,
                                       wx.Size(300, -1), m_radioBox9Choices, 1, wx.RA_SPECIFY_COLS)
        self.m_radioBox9.SetSelection(0)
        bSizer45.Add(self.m_radioBox9, 0, wx.ALL, 5)

        bSizer45.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer37 = wx.StaticBoxSizer(wx.StaticBox(self.settingsTab, wx.ID_ANY, _(u"Location")), wx.VERTICAL)

        self.m_textCtrl16 = wx.TextCtrl(sbSizer37.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        sbSizer37.Add(self.m_textCtrl16, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button26 = wx.Button(sbSizer37.GetStaticBox(), wx.ID_ANY, _(u"Enregistrer"), wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        sbSizer37.Add(self.m_button26, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer45.Add(sbSizer37, 1, wx.ALL | wx.EXPAND, 5)

        bSizer45.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer31.Add(bSizer45, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 20)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self.settingsTab, wx.ID_ANY, _(u"Tableau de bord")), wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer61 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.Add(bSizer61, 1, wx.EXPAND, 5)

        sbSizer27 = wx.StaticBoxSizer(wx.StaticBox(sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Stats")), wx.HORIZONTAL)

        bSizer70 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText52 = wx.StaticText(sbSizer27.GetStaticBox(), wx.ID_ANY, _(u"Donnes"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText52.Wrap(-1)

        bSizer70.Add(self.m_staticText52, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText53 = wx.StaticText(sbSizer27.GetStaticBox(), wx.ID_ANY, _(u"4 Joueurs"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText53.Wrap(-1)

        bSizer70.Add(self.m_staticText53, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText511 = wx.StaticText(sbSizer27.GetStaticBox(), wx.ID_ANY, _(u"5 joueurs"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText511.Wrap(-1)

        bSizer70.Add(self.m_staticText511, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer27.Add(bSizer70, 0, wx.ALL | wx.EXPAND, 5)

        bSizer701 = wx.BoxSizer(wx.VERTICAL)

        self.statsGames = wx.StaticText(sbSizer27.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.statsGames.Wrap(-1)

        bSizer701.Add(self.statsGames, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.statsGames4 = wx.StaticText(sbSizer27.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.statsGames4.Wrap(-1)

        bSizer701.Add(self.statsGames4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.statsGames5 = wx.StaticText(sbSizer27.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.statsGames5.Wrap(-1)

        bSizer701.Add(self.statsGames5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer27.Add(bSizer701, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(sbSizer27, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer271 = wx.StaticBoxSizer(wx.StaticBox(sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Gagné")), wx.HORIZONTAL)

        bSizer702 = wx.BoxSizer(wx.VERTICAL)

        self.vide03 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.vide03.Wrap(-1)

        bSizer702.Add(self.vide03, 0, wx.ALL, 5)

        self.m_staticText513 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"Petites"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText513.Wrap(-1)

        bSizer702.Add(self.m_staticText513, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText522 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"Gardes"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText522.Wrap(-1)

        bSizer702.Add(self.m_staticText522, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText532 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"Gardes Sans"),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText532.Wrap(-1)

        bSizer702.Add(self.m_staticText532, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5112 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"Gardes Contre"),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5112.Wrap(-1)

        bSizer702.Add(self.m_staticText5112, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText81 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"Chelems"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)

        bSizer702.Add(self.m_staticText81, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer271.Add(bSizer702, 0, wx.ALL | wx.EXPAND, 5)

        bSizer7011 = wx.BoxSizer(wx.VERTICAL)

        self.vide04 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.vide04.Wrap(-1)

        bSizer7011.Add(self.vide04, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winPetites = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.winPetites.Wrap(-1)

        bSizer7011.Add(self.winPetites, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardes = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.winGardes.Wrap(-1)

        bSizer7011.Add(self.winGardes, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardesSans = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.winGardesSans.Wrap(-1)

        bSizer7011.Add(self.winGardesSans, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardesContre = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.winGardesContre.Wrap(-1)

        bSizer7011.Add(self.winGardesContre, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winChelems = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.winChelems.Wrap(-1)

        bSizer7011.Add(self.winChelems, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer271.Add(bSizer7011, 0, wx.ALL | wx.EXPAND, 5)

        bSizer70112 = wx.BoxSizer(wx.VERTICAL)

        self.win4j = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"4J"), wx.DefaultPosition, wx.DefaultSize,
                                   0)
        self.win4j.Wrap(-1)

        bSizer70112.Add(self.win4j, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winPetites4 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.winPetites4.Wrap(-1)

        bSizer70112.Add(self.winPetites4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardes4 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.winGardes4.Wrap(-1)

        bSizer70112.Add(self.winGardes4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardesSans4 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.winGardesSans4.Wrap(-1)

        bSizer70112.Add(self.winGardesSans4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardesContre4 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.winGardesContre4.Wrap(-1)

        bSizer70112.Add(self.winGardesContre4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winChelems4 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.winChelems4.Wrap(-1)

        bSizer70112.Add(self.winChelems4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer271.Add(bSizer70112, 0, wx.ALL | wx.EXPAND, 5)

        bSizer70113 = wx.BoxSizer(wx.VERTICAL)

        self.win5j = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"5J"), wx.DefaultPosition, wx.DefaultSize,
                                   0)
        self.win5j.Wrap(-1)

        bSizer70113.Add(self.win5j, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winPetites5 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.winPetites5.Wrap(-1)

        bSizer70113.Add(self.winPetites5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardes5 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.winGardes5.Wrap(-1)

        bSizer70113.Add(self.winGardes5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardesSans5 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.winGardesSans5.Wrap(-1)

        bSizer70113.Add(self.winGardesSans5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winGardesContre5 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.winGardesContre5.Wrap(-1)

        bSizer70113.Add(self.winGardesContre5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.winChelems5 = wx.StaticText(sbSizer271.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.winChelems5.Wrap(-1)

        bSizer70113.Add(self.winChelems5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer271.Add(bSizer70113, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(sbSizer271, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer2711 = wx.StaticBoxSizer(wx.StaticBox(sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Perdu")), wx.HORIZONTAL)

        bSizer7021 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText51321 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51321.Wrap(-1)

        bSizer7021.Add(self.m_staticText51321, 0, wx.ALL, 5)

        self.m_staticText5131 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"Petites"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText5131.Wrap(-1)

        bSizer7021.Add(self.m_staticText5131, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5221 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"Gardes"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText5221.Wrap(-1)

        bSizer7021.Add(self.m_staticText5221, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5321 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"Gardes Sans"),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5321.Wrap(-1)

        bSizer7021.Add(self.m_staticText5321, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText51121 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"Gardes Contre"),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51121.Wrap(-1)

        bSizer7021.Add(self.m_staticText51121, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText811 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"Chelems"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText811.Wrap(-1)

        bSizer7021.Add(self.m_staticText811, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer2711.Add(bSizer7021, 0, wx.ALL | wx.EXPAND, 5)

        bSizer70111 = wx.BoxSizer(wx.VERTICAL)

        self.winPetite3 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.winPetite3.Wrap(-1)

        bSizer70111.Add(self.winPetite3, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.loosePetites = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.loosePetites.Wrap(-1)

        bSizer70111.Add(self.loosePetites, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardes = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.looseGardes.Wrap(-1)

        bSizer70111.Add(self.looseGardes, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardesSans = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.looseGardesSans.Wrap(-1)

        bSizer70111.Add(self.looseGardesSans, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardesContre = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.looseGardesContre.Wrap(-1)

        bSizer70111.Add(self.looseGardesContre, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseChelems = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.looseChelems.Wrap(-1)

        bSizer70111.Add(self.looseChelems, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer2711.Add(bSizer70111, 0, wx.ALL | wx.EXPAND, 5)

        bSizer701121 = wx.BoxSizer(wx.VERTICAL)

        self.loose4j = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"4J"), wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.loose4j.Wrap(-1)

        bSizer701121.Add(self.loose4j, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.loosePetites4 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.loosePetites4.Wrap(-1)

        bSizer701121.Add(self.loosePetites4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardes4 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.looseGardes4.Wrap(-1)

        bSizer701121.Add(self.looseGardes4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardesSans4 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.looseGardesSans4.Wrap(-1)

        bSizer701121.Add(self.looseGardesSans4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardesContre4 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.looseGardesContre4.Wrap(-1)

        bSizer701121.Add(self.looseGardesContre4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseChelems4 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.looseChelems4.Wrap(-1)

        bSizer701121.Add(self.looseChelems4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer2711.Add(bSizer701121, 0, wx.ALL | wx.EXPAND, 5)

        bSizer701131 = wx.BoxSizer(wx.VERTICAL)

        self.loose5j = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"5J"), wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.loose5j.Wrap(-1)

        bSizer701131.Add(self.loose5j, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.loosePetites5 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.loosePetites5.Wrap(-1)

        bSizer701131.Add(self.loosePetites5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardes5 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.looseGardes5.Wrap(-1)

        bSizer701131.Add(self.looseGardes5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardesSans5 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.looseGardesSans5.Wrap(-1)

        bSizer701131.Add(self.looseGardesSans5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseGardesContre5 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.looseGardesContre5.Wrap(-1)

        bSizer701131.Add(self.looseGardesContre5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.looseChelems5 = wx.StaticText(sbSizer2711.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.looseChelems5.Wrap(-1)

        bSizer701131.Add(self.looseChelems5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer2711.Add(bSizer701131, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(sbSizer2711, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer2.Add(bSizer4, 0, wx.ALL | wx.EXPAND, 5)

        bSizer31.Add(sbSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.settingsTab.SetSizer(bSizer31)
        self.settingsTab.Layout()
        bSizer31.Fit(self.settingsTab)
        self.m_notebook1.AddPage(self.settingsTab, _(u"Paramètres"), False)

        bSizer1.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.mailBox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer1.Add(self.mailBox, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.onMenuQuit, id=self.m_menuItem1.GetId())
        self.cnxTabPasswordEntry.Bind(wx.EVT_TEXT_ENTER, self.cnxTabOnCnxBtn)
        self.cnxTabCnxBtn.Bind(wx.EVT_BUTTON, self.cnxTabOnCnxBtn)
        self.cnxTabPlay4.Bind(wx.EVT_BUTTON, self.onCnxTabPlay4)
        self.cnxTabPlay5.Bind(wx.EVT_BUTTON, self.onCnxTabPlay5)
        self.cnxTabJoinBtn.Bind(wx.EVT_BUTTON, self.onCnxTabJoinBtn)
        self.cnxTabGamesList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onGameSelect)
        self.cnxTabCreateBtn.Bind(wx.EVT_BUTTON, self.onCnxTabCreateBtn)
        self.cnxTabCreatePrivate.Bind(wx.EVT_CHECKBOX, self.onCnxTabCreatePrivate)
        self.cnxTabPly1Change.Bind(wx.EVT_BUTTON, self.onCnxTabPly1Change)
        self.cnxTabPly2Change.Bind(wx.EVT_BUTTON, self.onCnxTabPly2Change)
        self.cnxTabPly3Change.Bind(wx.EVT_BUTTON, self.onCnxTabPly3Change)
        self.cnxTabPly4Change.Bind(wx.EVT_BUTTON, self.onCnxTabPly4Change)
        self.cnxTabPly5Change.Bind(wx.EVT_BUTTON, self.onCnxTabPly5Change)
        self.cnxTabLeave.Bind(wx.EVT_BUTTON, self.onCnxTabLeave)
        self.cnxTabFicheGameStart.Bind(wx.EVT_BUTTON, self.onCnxTabFicheGameStart)
        self.mailBox.Bind(wx.EVT_TEXT, self.onImportChange)

        firstDisplay(self)

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

    def cnxTabOnCnxBtn(self, event):
        userCnx = self.cnxTabUserEntry.GetValue()
        passwordCnx = self.cnxTabPasswordEntry.GetValue()
        appSettings.user = userCnx
        appSettings.password = passwordCnx
        sendMessageToServer(self, 'userCnx', UserCnx(userCnx, passwordCnx))
        event.Skip()

    def onGameSelect(self, event):
        choice = self.cnxTabGamesList.GetFirstSelected()
        item = self.cnxTabGamesList.GetItem(itemIdx=choice, col=0)
        appSettings.private_game_select = item.GetText()
        item = self.cnxTabGamesList.GetItem(itemIdx=choice, col=2)
        self.cnxTabPrivateTitle.SetLabel(item.GetText())
        self.cnxTabSearchPwd.Enable()
        self.cnxTabJoinBtn.Enable()
        for x in range(0, self.cnxTabGamesList.GetItemCount(), 1):
            self.cnxTabGamesList.Select(x, on=0)
        self.Layout()
        event.Skip()

    def onCnxTabCreateBtn(self, event):
        user = appSettings.user
        nickname = appSettings.nickName
        denomination = self.cnxTabCreateDenomination.GetValue()
        password = self.cnxTabCreatePassword.GetValue()
        if self.cnxTabCreateChoicePlayers.GetStringSelection() == '5':
            maxPlayers = 5
        else:
            maxPlayers = 4
        private = self.cnxTabCreatePrivate.GetValue()

        if private:
            if len(password) < 3:
                dialogMsg(self, _("Erreur"), _("Le mot de passe doit comporter au moins 3 caractères"))
            else:
                isWithAnnonce = self.cnxTabOptionsSA.GetValue()
                isWithRelance = self.cnxTabOptionsAR.GetValue()
                isWithChat = self.cnxTabOptionsSC.GetValue()
                isWithBelge = self.cnxTabOptionsAB.GetValue()
                isWithPetite = self.cnxTabOptionsPetie.GetValue()
                isWithGarde = self.cnxTabOptionsGarde.GetValue()
                isWithGardeSans = self.cnxTabOptionsGardeSans.GetValue()
                isWithRound = self.cnxTabOptionsArrondi.GetValue()

                msg = GameCreateMsg(denomination,
                                    private,
                                    password,
                                    maxPlayers,
                                    isWithChat,
                                    isWithRelance,
                                    isWithAnnonce,
                                    isWithRound,
                                    isWithBelge,
                                    isWithPetite,
                                    isWithGarde,
                                    isWithGardeSans,
                                    user,
                                    nickname
                                    )
                sendMessageToServer(self, 'createGame', msg)
        else:
            private = False
            password = None
            isWithAnnonce = False
            isWithRelance = False
            isWithChat = False
            isWithBelge = False
            isWithPetite = True
            isWithGarde = True
            isWithGardeSans = True
            isWithRound = False

            msg = GameCreateMsg(denomination,
                                private,
                                password,
                                maxPlayers,
                                isWithChat,
                                isWithRelance,
                                isWithAnnonce,
                                isWithRound,
                                isWithBelge,
                                isWithPetite,
                                isWithGarde,
                                isWithGardeSans,
                                user,
                                nickname
                                )
            sendMessageToServer(self, 'createGame', msg)
        event.Skip()

    def onCnxTabPlay4(self, event):
        event.Skip()

    def onCnxTabPlay5(self, event):
        event.Skip()

    def onCnxTabJoinBtn(self, event):
        gameId = appSettings.private_game_select
        password = self.cnxTabSearchPwd.GetValue()
        value = SelectPrivateGame(gameId, password)
        self.sendMessageToServer(MessageToServer('privateGameCnx', value))
        event.Skip()

    def onCnxTabLeave(self, event):
        gameId = appSettings.userPlay
        user = appSettings.user
        value = DeconnectGameInfos(gameId, user)
        self.sendMessageToServer(MessageToServer('playerLogout', value))
        playerLogoutDisplay(self)
        self.Layout()
        event.Skip()

    def onCnxTabCreatePrivate(self, event):
        if self.cnxTabCreatePrivate.GetValue():
            self.cnxTabOptionsSA.Enable()
            self.cnxTabOptionsAR.Enable()
            self.cnxTabOptionsSC.Enable()
            self.cnxTabOptionsArrondi.Enable()
            self.cnxTabOptionsAB.Enable()
            self.cnxTabOptionsPetie.Enable()
            self.cnxTabOptionsGarde.Enable()
            self.cnxTabOptionsGardeSans.Enable()
            self.cnxTabCreatePassword.Enable()
            self.m_staticText110.Enable()
        else:
            self.cnxTabOptionsSA.Disable()
            self.cnxTabOptionsSA.SetValue(False)
            self.cnxTabOptionsAR.Disable()
            self.cnxTabOptionsAR.SetValue(False)
            self.cnxTabOptionsSC.Disable()
            self.cnxTabOptionsSC.SetValue(False)
            self.cnxTabOptionsArrondi.Disable()
            self.cnxTabOptionsArrondi.SetValue(False)
            self.cnxTabOptionsAB.Disable()
            self.cnxTabOptionsAB.SetValue(False)
            self.cnxTabOptionsPetie.Disable()
            self.cnxTabOptionsPetie.SetValue(True)
            self.cnxTabOptionsGarde.Disable()
            self.cnxTabOptionsGarde.SetValue(True)
            self.cnxTabOptionsGardeSans.Disable()
            self.cnxTabOptionsGardeSans.SetValue(True)
            self.cnxTabCreatePassword.Disable()
            self.cnxTabCreatePassword.SetValue('')
            self.m_staticText110.Disable()
        event.Skip()

    def onCnxTabFicheGameStart(self, event):
        sendMessageToServer(self, 'startGame', appSettings.userPlay)
        event.Skip()

    def onCnxTabPly1Change(self, event):
        event.Skip()

    def onCnxTabPly2Change(self, event):
        event.Skip()

    def onCnxTabPly3Change(self, event):
        event.Skip()

    def onCnxTabPly4Change(self, event):
        event.Skip()

    def onCnxTabPly5Change(self, event):
        event.Skip()

    def onGameTabNordSound(self, event):
        event.Skip()

    def onGameTabNord2Sound(self, event):
        event.Skip()

    def onGameTabOuestSound(self, event):
        event.Skip()

    def onGameTabVu(self, event):
        event.Skip()

    def onGameTabEstSound(self, event):
        event.Skip()

    def onGameTabPassBtn(self, event):
        event.Skip()

    def onGameTabContratBtn(self, event):
        event.Skip()

    def onGameTabNordSound(self, event):
        event.Skip()

    def onGameTabNord2Sound(self, event):
        event.Skip()

    def onGameTabOuestSound(self, event):
        event.Skip()

    def onGameTabVu(self, event):
        event.Skip()

    def onGameTabEstSound(self, event):
        event.Skip()

    def onGameTabPassBtn(self, event):
        event.Skip()

    def onGameTabContratBtn(self, event):
        event.Skip()

    def onGameTabChat(self, event):
        event.Skip()

    def onGameTabChienOk(self, event):
        event.Skip()

    def onChien(self, event):
        event.Skip()

    def onDeck(self, event):
        event.Skip()
