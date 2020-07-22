# -*- coding: utf-8 -*-


import wx

import appSettings
from appcore.translate import _


class Game4(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(1400, 900), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        frame_size = parent.GetSize()
        appSettings.card_H = round(frame_size[1] / appSettings.card_C)
        appSettings.card_L = round(appSettings.card_H / 1.875)
        appSettings.card_CL = round(appSettings.card_H / 3)

        cards = 'Frame:' + str(frame_size[1]) + ' H:' + str(appSettings.card_H) + 'L:' + str(appSettings.card_L) + ' CL:' + str(
            appSettings.card_CL)
        print(cards)

        bSizer4211 = wx.BoxSizer(wx.VERTICAL)

        bSizer1921 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4411 = wx.BoxSizer(wx.VERTICAL)

        bSizer451221 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer6421 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer72221 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabGameDonneLbl = wx.StaticText(self, wx.ID_ANY, _(u"Donne"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabGameDonneLbl.Wrap(-1)

        bSizer72221.Add(self.gameTabGameDonneLbl, 0, wx.ALL, 5)

        self.gameTabGameContratLbl = wx.StaticText(self, wx.ID_ANY, _(u"Contrat"), wx.DefaultPosition, wx.DefaultSize,
                                                   0)
        self.gameTabGameContratLbl.Wrap(-1)

        bSizer72221.Add(self.gameTabGameContratLbl, 0, wx.ALL, 5)

        self.meTabGamePreneurLbl = wx.StaticText(self, wx.ID_ANY, _(u"Preneur"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.meTabGamePreneurLbl.Wrap(-1)

        bSizer72221.Add(self.meTabGamePreneurLbl, 0, wx.ALL, 5)

        self.gameTabGameTourLbl = wx.StaticText(self, wx.ID_ANY, _(u"Tour"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabGameTourLbl.Wrap(-1)

        bSizer72221.Add(self.gameTabGameTourLbl, 0, wx.ALL, 5)

        bSizer6421.Add(bSizer72221, 0, wx.EXPAND, 5)

        bSizer722111 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabGameDonne = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.Size(175, -1), 0)
        self.gameTabGameDonne.Wrap(-1)

        bSizer722111.Add(self.gameTabGameDonne, 0, wx.ALL, 5)

        self.gameTabGameContrat = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabGameContrat.Wrap(-1)

        bSizer722111.Add(self.gameTabGameContrat, 0, wx.ALL, 5)

        self.gameTabGamePreneur = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabGamePreneur.Wrap(-1)

        bSizer722111.Add(self.gameTabGamePreneur, 0, wx.ALL, 5)

        self.gameTabGameTour = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabGameTour.Wrap(-1)

        bSizer722111.Add(self.gameTabGameTour, 0, wx.ALL, 5)

        bSizer6421.Add(bSizer722111, 0, wx.EXPAND, 5)

        bSizer451221.Add(bSizer6421, 0, wx.EXPAND, 5)

        bSizer451221.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer7331 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabNordLed = wx.StaticBitmap(self, wx.ID_ANY,
                                              wx.Bitmap(u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7331.Add(self.gameTabNordLed, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.gameTabNordStatus = wx.StaticBitmap(self, wx.ID_ANY,
                                                 wx.Bitmap(u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY),
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7331.Add(self.gameTabNordStatus, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.gameTabNordDealer = wx.StaticBitmap(self, wx.ID_ANY,
                                                 wx.Bitmap(u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY),
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7331.Add(self.gameTabNordDealer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.gameTabNordSound = wx.ToggleButton(self, wx.ID_ANY, _(u"On"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7331.Add(self.gameTabNordSound, 0, 0, 5)

        bSizer451221.Add(bSizer7331, 0, wx.EXPAND, 5)

        bSizer49141 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabNordCard = wx.StaticBitmap(self, wx.ID_ANY,
                                               wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer49141.Add(self.gameTabNordCard, 0, wx.ALL, 5)

        bSizer451221.Add(bSizer49141, 0, wx.EXPAND, 5)

        bSizer2814 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabNord = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.Size(175, -1), 0)
        self.gameTabNord.Wrap(-1)

        self.gameTabNord.SetToolTip(_(u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0"))

        bSizer2814.Add(self.gameTabNord, 0, wx.ALL, 5)

        self.gameTabNordAction = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabNordAction.Wrap(-1)

        bSizer2814.Add(self.gameTabNordAction, 0, wx.ALL, 5)

        bSizer451221.Add(bSizer2814, 0, wx.ALL, 5)

        bSizer451221.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer64111 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabChat = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1),
                                       wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer64111.Add(self.gameTabChat, 1, wx.ALL | wx.EXPAND, 5)

        bSizer451221.Add(bSizer64111, 1, wx.EXPAND, 5)

        bSizer4411.Add(bSizer451221, 0, wx.EXPAND, 0)

        bSizer4411.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer451121 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer451121.Add((0, 0), 0, wx.LEFT, 15)

        bSizer73231 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabOuestLed = wx.StaticBitmap(self, wx.ID_ANY,
                                               wx.Bitmap(u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer73231.Add(self.gameTabOuestLed, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.gameTabOuestStatus = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer73231.Add(self.gameTabOuestStatus, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.gameTabOuestDealer = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer73231.Add(self.gameTabOuestDealer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.gameTabOuestSound = wx.ToggleButton(self, wx.ID_ANY, _(u"On"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer73231.Add(self.gameTabOuestSound, 0, 0, 5)

        bSizer451121.Add(bSizer73231, 0, wx.EXPAND, 5)

        bSizer491111 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabOuestCard = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer491111.Add(self.gameTabOuestCard, 0, wx.ALL, 5)

        bSizer451121.Add(bSizer491111, 0, wx.EXPAND, 5)

        bSizer28131 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabOuest = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.Size(175, -1), 0)
        self.gameTabOuest.Wrap(-1)

        self.gameTabOuest.SetToolTip(_(u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0"))

        bSizer28131.Add(self.gameTabOuest, 0, wx.ALL, 5)

        self.gameTabOuestAction = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabOuestAction.Wrap(-1)

        bSizer28131.Add(self.gameTabOuestAction, 0, wx.ALL, 5)

        bSizer451121.Add(bSizer28131, 0, wx.EXPAND, 5)

        bSizer451121.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer7811 = wx.BoxSizer(wx.VERTICAL)

        bSizer1291 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1281 = wx.BoxSizer(wx.HORIZONTAL)

        self.gameTabChien1 = wx.StaticBitmap(self, 201, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer1281.Add(self.gameTabChien1, 0, wx.ALL, 5)

        self.gameTabChien2 = wx.StaticBitmap(self, 202, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer1281.Add(self.gameTabChien2, 0, wx.ALL, 5)

        self.gameTabChien3 = wx.StaticBitmap(self, 203, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer1281.Add(self.gameTabChien3, 0, wx.ALL, 5)

        self.gameTabChien4 = wx.StaticBitmap(self, 204, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer1281.Add(self.gameTabChien4, 0, wx.ALL, 5)

        self.gameTabChien5 = wx.StaticBitmap(self, 205, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer1281.Add(self.gameTabChien5, 0, wx.ALL, 5)

        self.gameTabChien6 = wx.StaticBitmap(self, 206, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer1281.Add(self.gameTabChien6, 0, wx.ALL, 5)

        bSizer1291.Add(bSizer1281, 0, wx.EXPAND, 5)

        bSizer7811.Add(bSizer1291, 1, wx.EXPAND, 5)

        bSizer279 = wx.BoxSizer(wx.HORIZONTAL)

        self.gameTabChienOk = wx.Button(self, wx.ID_ANY, _(u"Valider"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer279.Add(self.gameTabChienOk, 0, wx.ALL, 5)

        self.gameTabCroupier = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabCroupier.Wrap(-1)

        self.gameTabCroupier.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer279.Add(self.gameTabCroupier, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer7811.Add(bSizer279, 0, wx.EXPAND, 5)

        bSizer451121.Add(bSizer7811, 0, 0, 5)

        bSizer451121.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer732111 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabEstLed = wx.StaticBitmap(self, wx.ID_ANY,
                                             wx.Bitmap(u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer732111.Add(self.gameTabEstLed, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.gameTabEstStatus = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer732111.Add(self.gameTabEstStatus, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.gameTabEstDealer = wx.StaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer732111.Add(self.gameTabEstDealer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.gameTabEstSound = wx.ToggleButton(self, wx.ID_ANY, _(u"On"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer732111.Add(self.gameTabEstSound, 0, 0, 5)

        bSizer451121.Add(bSizer732111, 0, wx.EXPAND, 5)

        bSizer491311 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabEstCard = wx.StaticBitmap(self, wx.ID_ANY,
                                              wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                              wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer491311.Add(self.gameTabEstCard, 0, wx.ALL, 5)

        bSizer451121.Add(bSizer491311, 0, wx.EXPAND, 5)

        bSizer28121 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabEst = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.Size(175, -1), 0)
        self.gameTabEst.Wrap(-1)

        self.gameTabEst.SetToolTip(_(u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0"))

        bSizer28121.Add(self.gameTabEst, 0, wx.ALL, 5)

        self.gameTabEstAction = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabEstAction.Wrap(-1)

        bSizer28121.Add(self.gameTabEstAction, 0, wx.ALL, 5)

        bSizer451121.Add(bSizer28121, 0, wx.EXPAND, 5)

        bSizer451121.Add((0, 0), 0, wx.RIGHT, 15)

        bSizer4411.Add(bSizer451121, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 10)

        bSizer4411.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer4512111 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4512111.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer732211 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabUserLed = wx.StaticBitmap(self, wx.ID_ANY,
                                              wx.Bitmap(u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer732211.Add(self.gameTabUserLed, 0, wx.ALL, 5)

        self.gameTabUserStatus = wx.StaticBitmap(self, wx.ID_ANY,
                                                 wx.Bitmap(u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY),
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer732211.Add(self.gameTabUserStatus, 0, wx.ALL, 5)

        self.gameTabUserDealer = wx.StaticBitmap(self, wx.ID_ANY,
                                                 wx.Bitmap(u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY),
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer732211.Add(self.gameTabUserDealer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer4512111.Add(bSizer732211, 0, wx.EXPAND, 5)

        self.gameTabUserCardSelect = wx.StaticBitmap(self, wx.ID_ANY,
                                                     wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                                     wx.DefaultPosition,
                                                     wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer4512111.Add(self.gameTabUserCardSelect, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        bSizer281321 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabUser = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.Size(175, -1), 0)
        self.gameTabUser.Wrap(-1)

        self.gameTabUser.SetToolTip(_(u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0"))

        bSizer281321.Add(self.gameTabUser, 0, wx.ALL, 5)

        self.gameTabUserAction = wx.StaticText(self, wx.ID_ANY, _(u"--"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabUserAction.Wrap(-1)

        bSizer281321.Add(self.gameTabUserAction, 0, wx.ALL, 5)

        self.gameTabPlayCardBtn = wx.Button(self, wx.ID_ANY, _(u"Jouer cette carte"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bSizer281321.Add(self.gameTabPlayCardBtn, 0, wx.ALL, 5)

        self.gameTabVote = wx.Button(self, wx.ID_ANY, _(u"Vu"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer281321.Add(self.gameTabVote, 0, wx.ALL, 5)

        bSizer4512111.Add(bSizer281321, 0, 0, 5)

        bSizer4512111.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer10311 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer82221 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabContratPasse = wx.Button(self, wx.ID_ANY, _(u"Je passe"), wx.DefaultPosition, wx.Size(120, -1), 0)
        bSizer82221.Add(self.gameTabContratPasse, 0, wx.ALL, 5)

        self.gameTabContratPetite = wx.Button(self, wx.ID_ANY, _(u"Petite"), wx.DefaultPosition, wx.Size(120, -1), 0)
        bSizer82221.Add(self.gameTabContratPetite, 0, wx.ALL, 5)

        self.gameTabContratGarde = wx.Button(self, wx.ID_ANY, _(u"Garde"), wx.DefaultPosition, wx.Size(120, -1), 0)
        bSizer82221.Add(self.gameTabContratGarde, 0, wx.ALL, 5)

        bSizer10311.Add(bSizer82221, 0, wx.EXPAND, 5)

        bSizer822111 = wx.BoxSizer(wx.VERTICAL)

        self.gameTabContratGardeSans = wx.Button(self, wx.ID_ANY, _(u"Garde Sans"), wx.DefaultPosition,
                                                 wx.Size(120, -1), 0)
        bSizer822111.Add(self.gameTabContratGardeSans, 0, wx.ALL, 5)

        self.gameTabContratGardecontre = wx.Button(self, wx.ID_ANY, _(u"Garde Contre"), wx.DefaultPosition,
                                                   wx.Size(120, -1), 0)
        bSizer822111.Add(self.gameTabContratGardecontre, 0, wx.ALL, 5)

        self.gameTabChelem = wx.CheckBox(self, wx.ID_ANY, _(u"Chelem"), wx.DefaultPosition, wx.Size(120, -1), 0)
        bSizer822111.Add(self.gameTabChelem, 0, wx.ALL, 5)

        bSizer10311.Add(bSizer822111, 0, wx.EXPAND, 5)

        bSizer4512111.Add(bSizer10311, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4411.Add(bSizer4512111, 0, wx.EXPAND, 0)

        bSizer1921.Add(bSizer4411, 1, wx.EXPAND, 5)

        sbSizer231 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"Fiche de Match")), wx.VERTICAL)

        sbSizer83 = wx.StaticBoxSizer(wx.StaticBox(sbSizer231.GetStaticBox(), wx.ID_ANY, _(u"Partie")), wx.VERTICAL)

        bSizer7611 = wx.BoxSizer(wx.HORIZONTAL)

        self.cnxTabFicheGameIsPlayable = wx.StaticBitmap(sbSizer83.GetStaticBox(), wx.ID_ANY,
                                                         wx.Bitmap(u"public/icons/16x16_led_red.png",
                                                                   wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                         wx.DefaultSize, 0)
        bSizer7611.Add(self.cnxTabFicheGameIsPlayable, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cnxTabFicheGameName = wx.StaticText(sbSizer83.GetStaticBox(), wx.ID_ANY, _(u"--"), wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.cnxTabFicheGameName.Wrap(-1)

        bSizer7611.Add(self.cnxTabFicheGameName, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer83.Add(bSizer7611, 1, wx.EXPAND, 5)

        sbSizer231.Add(sbSizer83, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer8121 = wx.StaticBoxSizer(wx.StaticBox(sbSizer231.GetStaticBox(), wx.ID_ANY, _(u"Scores et Positions")),
                                        wx.HORIZONTAL)

        bSizer1542 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2374 = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"-1-"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2374.Wrap(-1)

        bSizer1542.Add(self.m_staticText2374, 0, wx.ALL, 5)

        self.m_staticText23711 = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"-2-"), wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText23711.Wrap(-1)

        bSizer1542.Add(self.m_staticText23711, 0, wx.ALL, 5)

        self.m_staticText23721 = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"-3-"), wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText23721.Wrap(-1)

        bSizer1542.Add(self.m_staticText23721, 0, wx.ALL, 5)

        self.m_staticText23731 = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"-4-"), wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText23731.Wrap(-1)

        bSizer1542.Add(self.m_staticText23731, 0, wx.ALL, 5)

        sbSizer8121.Add(bSizer1542, 0, wx.ALL, 5)

        bSizer15412 = wx.BoxSizer(wx.VERTICAL)

        self.cnxTabFichePos1Nickname = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"--"),
                                                     wx.DefaultPosition, wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.cnxTabFichePos1Nickname.Wrap(-1)

        bSizer15412.Add(self.cnxTabFichePos1Nickname, 0, wx.ALL | wx.EXPAND, 5)

        self.cnxTabFichePos2Nickname = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"--"),
                                                     wx.DefaultPosition, wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.cnxTabFichePos2Nickname.Wrap(-1)

        bSizer15412.Add(self.cnxTabFichePos2Nickname, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabFichePos3Nickname = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"--"),
                                                     wx.DefaultPosition, wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.cnxTabFichePos3Nickname.Wrap(-1)

        bSizer15412.Add(self.cnxTabFichePos3Nickname, 0, wx.ALL | wx.EXPAND, 5)

        self.cnxTabFichePos4Nickname = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"--"),
                                                     wx.DefaultPosition, wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.cnxTabFichePos4Nickname.Wrap(-1)

        bSizer15412.Add(self.cnxTabFichePos4Nickname, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer8121.Add(bSizer15412, 1, wx.ALL, 5)

        bSizer154111 = wx.BoxSizer(wx.VERTICAL)

        self.cnxTabFichePos1Score = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                                  wx.Size(-1, -1), 0)
        self.cnxTabFichePos1Score.Wrap(-1)

        bSizer154111.Add(self.cnxTabFichePos1Score, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabFichePos2Score = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.cnxTabFichePos2Score.Wrap(-1)

        bSizer154111.Add(self.cnxTabFichePos2Score, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabFichePos3Score = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.cnxTabFichePos3Score.Wrap(-1)

        bSizer154111.Add(self.cnxTabFichePos3Score, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.cnxTabFichePos4Score = wx.StaticText(sbSizer8121.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                                  wx.Size(-1, -1), 0)
        self.cnxTabFichePos4Score.Wrap(-1)

        bSizer154111.Add(self.cnxTabFichePos4Score, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sbSizer8121.Add(bSizer154111, 0, wx.ALL, 5)

        sbSizer231.Add(sbSizer8121, 0, wx.ALL | wx.EXPAND, 5)

        self.cnxTabGameDetail = wx.ListCtrl(sbSizer231.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LC_ICON)
        sbSizer231.Add(self.cnxTabGameDetail, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1921.Add(sbSizer231, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4211.Add(bSizer1921, 1, wx.EXPAND, 5)

        bSizer4511111 = wx.BoxSizer(wx.HORIZONTAL)

        self.gameTabLastTurn = wx.CheckBox(self, wx.ID_ANY, _(u"Dernière Donne"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4511111.Add(self.gameTabLastTurn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer4511111.Add((0, 0), 1, wx.EXPAND, 5)

        self.deck01 = wx.StaticBitmap(self, 101, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck01, 0, 0, 5)

        self.deck02 = wx.StaticBitmap(self, 102, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck02, 0, 0, 5)

        self.deck03 = wx.StaticBitmap(self, 103, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck03, 0, 0, 5)

        self.deck04 = wx.StaticBitmap(self, 104, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck04, 0, 0, 5)

        self.deck05 = wx.StaticBitmap(self, 105, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck05, 0, 0, 5)

        self.deck06 = wx.StaticBitmap(self, 106, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck06, 0, 0, 5)

        self.deck07 = wx.StaticBitmap(self, 107, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck07, 0, 0, 5)

        self.deck08 = wx.StaticBitmap(self, 108, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck08, 0, 0, 5)

        self.deck09 = wx.StaticBitmap(self, 109, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck09, 0, 0, 5)

        self.deck10 = wx.StaticBitmap(self, 110, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck10, 0, 0, 5)

        self.deck11 = wx.StaticBitmap(self, 111, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck11, 0, 0, 5)

        self.deck12 = wx.StaticBitmap(self, 112, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck12, 0, 0, 5)

        self.deck13 = wx.StaticBitmap(self, 113, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck13, 0, 0, 5)

        self.deck14 = wx.StaticBitmap(self, 114, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck14, 0, 0, 5)

        self.deck15 = wx.StaticBitmap(self, 115, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck15, 0, 0, 5)

        self.deck16 = wx.StaticBitmap(self, 116, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck16, 0, 0, 5)

        self.deck17 = wx.StaticBitmap(self, 117, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck17, 0, 0, 5)

        self.deck18 = wx.StaticBitmap(self, 118, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck18, 0, 0, 5)

        self.deck19 = wx.StaticBitmap(self, 119, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck19, 0, 0, 5)

        self.deck20 = wx.StaticBitmap(self, 120, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck20, 0, 0, 5)

        self.deck21 = wx.StaticBitmap(self, 121, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck21, 0, 0, 5)

        self.deck22 = wx.StaticBitmap(self, 122, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck22, 0, 0, 5)

        self.deck23 = wx.StaticBitmap(self, 123, wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(appSettings.card_CL, appSettings.card_H), 0)
        bSizer4511111.Add(self.deck23, 0, 0, 5)

        self.deckFull = wx.StaticBitmap(self, 124, wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.Size(appSettings.card_L, appSettings.card_H), 0)
        bSizer4511111.Add(self.deckFull, 0, 0, 5)

        bSizer4511111.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer4211.Add(bSizer4511111, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 10)

        bSizer7111 = wx.BoxSizer(wx.HORIZONTAL)

        self.gameTabChatLbl = wx.StaticText(self, wx.ID_ANY, _(u"Chat :"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameTabChatLbl.Wrap(-1)

        bSizer7111.Add(self.gameTabChatLbl, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.gameTabChatMsg = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_PROCESS_ENTER)
        bSizer7111.Add(self.gameTabChatMsg, 1, wx.EXPAND, 0)

        bSizer4211.Add(bSizer7111, 0, wx.EXPAND, 0)

        self.SetSizer(bSizer4211)
        self.Layout()

        # Connect Events
        self.gameTabNordSound.Bind(wx.EVT_TOGGLEBUTTON, self.onGameTabNordSound)
        self.gameTabOuestSound.Bind(wx.EVT_TOGGLEBUTTON, self.onGameTabOuestSound)
        self.gameTabChien1.Bind(wx.EVT_LEFT_DOWN, self.onChien)
        self.gameTabChien2.Bind(wx.EVT_LEFT_DOWN, self.onChien)
        self.gameTabChien3.Bind(wx.EVT_LEFT_DOWN, self.onChien)
        self.gameTabChien4.Bind(wx.EVT_LEFT_DOWN, self.onChien)
        self.gameTabChien5.Bind(wx.EVT_LEFT_DOWN, self.onChien)
        self.gameTabChien6.Bind(wx.EVT_LEFT_DOWN, self.onChien)
        self.gameTabChienOk.Bind(wx.EVT_BUTTON, self.onGameTabChienOk)
        self.gameTabEstSound.Bind(wx.EVT_TOGGLEBUTTON, self.onGameTabEstSound)
        self.gameTabContratPasse.Bind(wx.EVT_BUTTON, self.onGameTabPassBtn)
        self.gameTabContratPetite.Bind(wx.EVT_BUTTON, self.onGameTabContratBtn)
        self.gameTabContratGardeSans.Bind(wx.EVT_BUTTON, self.onGameTabPassBtn)
        self.gameTabContratGardecontre.Bind(wx.EVT_BUTTON, self.onGameTabContratBtn)
        self.deck01.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck02.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck03.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck04.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck05.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck06.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck07.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck08.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck09.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck10.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck11.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck12.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck13.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck14.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck15.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck16.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck17.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck18.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck19.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck20.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck21.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck22.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deck23.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.deckFull.Bind(wx.EVT_LEFT_DOWN, self.onDeck)
        self.gameTabChatMsg.Bind(wx.EVT_TEXT_ENTER, self.onGameTabChat)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onGameTabNordSound(self, event):
        event.Skip()

    def onGameTabOuestSound(self, event):
        event.Skip()

    def onChien(self, event):
        event.Skip()

    def onGameTabChienOk(self, event):
        event.Skip()

    def onGameTabEstSound(self, event):
        event.Skip()

    def onGameTabPassBtn(self, event):
        event.Skip()

    def onGameTabContratBtn(self, event):
        event.Skip()

    def onDeck(self, event):
        event.Skip()

    def onGameTabChat(self, event):
        event.Skip()
