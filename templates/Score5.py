# -*- coding: utf-8 -*-


import wx


from appcore.translate import _


class Score5(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(713, 777), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer138 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText224 = wx.StaticText(self, wx.ID_ANY, _(u"SCORE"), wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText224.Wrap(-1)

        self.m_staticText224.SetFont(
            wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer138.Add(self.m_staticText224, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer53 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"Détails")), wx.VERTICAL)

        bSizer169 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer170 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText264 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Preneur : "), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText264.Wrap(-1)

        bSizer170.Add(self.m_staticText264, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText265 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Appel : "), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText265.Wrap(-1)

        bSizer170.Add(self.m_staticText265, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText266 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Contrat : "), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText266.Wrap(-1)

        bSizer170.Add(self.m_staticText266, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText267 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Bouts : "), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText267.Wrap(-1)

        bSizer170.Add(self.m_staticText267, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText268 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Points : "), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText268.Wrap(-1)

        bSizer170.Add(self.m_staticText268, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText274 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Petit au bout : "),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText274.Wrap(-1)

        bSizer170.Add(self.m_staticText274, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText2741 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Annonces : "),
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2741.Wrap(-1)

        bSizer170.Add(self.m_staticText2741, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText27412 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Chelem : "), wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText27412.Wrap(-1)

        bSizer170.Add(self.m_staticText27412, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText27411 = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"RESULTAT :"),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27411.Wrap(-1)

        bSizer170.Add(self.m_staticText27411, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer169.Add(bSizer170, 1, 0, 5)

        bSizer171 = wx.BoxSizer(wx.VERTICAL)

        self.score5Preneur = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.score5Preneur.Wrap(-1)

        bSizer171.Add(self.score5Preneur, 0, wx.ALL, 5)

        self.score5Appel = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.score5Appel.Wrap(-1)

        bSizer171.Add(self.score5Appel, 0, wx.ALL, 5)

        self.score5Contrat = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.score5Contrat.Wrap(-1)

        bSizer171.Add(self.score5Contrat, 0, wx.ALL, 5)

        self.score5Bouts = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.score5Bouts.Wrap(-1)

        bSizer171.Add(self.score5Bouts, 0, wx.ALL, 5)

        self.score5Points = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.score5Points.Wrap(-1)

        bSizer171.Add(self.score5Points, 0, wx.ALL, 5)

        self.score5PAB = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.score5PAB.Wrap(-1)

        bSizer171.Add(self.score5PAB, 0, wx.ALL, 5)

        self.score5Annonces = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.score5Annonces.Wrap(-1)

        bSizer171.Add(self.score5Annonces, 0, wx.ALL, 5)

        self.score5Chelem = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.score5Chelem.Wrap(-1)

        bSizer171.Add(self.score5Chelem, 0, wx.ALL, 5)

        self.score5Resultat = wx.StaticText(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.score5Resultat.Wrap(-1)

        bSizer171.Add(self.score5Resultat, 0, wx.ALL, 5)

        bSizer169.Add(bSizer171, 1, 0, 5)

        sbSizer53.Add(bSizer169, 1, wx.EXPAND, 5)

        sbSizer54 = wx.StaticBoxSizer(wx.StaticBox(sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Points")), wx.HORIZONTAL)

        sbSizer55 = wx.StaticBoxSizer(wx.StaticBox(sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.score5Player1 = wx.StaticText(sbSizer55.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.score5Player1.Wrap(-1)

        sbSizer55.Add(self.score5Player1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText277 = wx.StaticText(sbSizer55.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText277.Wrap(-1)

        sbSizer55.Add(self.m_staticText277, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        sbSizer54.Add(sbSizer55, 1, wx.ALL, 5)

        sbSizer551 = wx.StaticBoxSizer(wx.StaticBox(sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.score5Player2 = wx.StaticText(sbSizer551.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.score5Player2.Wrap(-1)

        sbSizer551.Add(self.score5Player2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText2771 = wx.StaticText(sbSizer551.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2771.Wrap(-1)

        sbSizer551.Add(self.m_staticText2771, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        sbSizer54.Add(sbSizer551, 1, wx.ALL, 5)

        sbSizer552 = wx.StaticBoxSizer(wx.StaticBox(sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.score5Player3 = wx.StaticText(sbSizer552.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.score5Player3.Wrap(-1)

        sbSizer552.Add(self.score5Player3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText2772 = wx.StaticText(sbSizer552.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2772.Wrap(-1)

        sbSizer552.Add(self.m_staticText2772, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        sbSizer54.Add(sbSizer552, 1, wx.ALL, 5)

        sbSizer553 = wx.StaticBoxSizer(wx.StaticBox(sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.score5Player4 = wx.StaticText(sbSizer553.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.score5Player4.Wrap(-1)

        sbSizer553.Add(self.score5Player4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText2773 = wx.StaticText(sbSizer553.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2773.Wrap(-1)

        sbSizer553.Add(self.m_staticText2773, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        sbSizer54.Add(sbSizer553, 1, wx.ALL, 5)

        sbSizer554 = wx.StaticBoxSizer(wx.StaticBox(sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.score5Player5 = wx.StaticText(sbSizer554.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.score5Player5.Wrap(-1)

        sbSizer554.Add(self.score5Player5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText2774 = wx.StaticText(sbSizer554.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2774.Wrap(-1)

        sbSizer554.Add(self.m_staticText2774, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        sbSizer54.Add(sbSizer554, 1, wx.ALL, 5)

        sbSizer53.Add(sbSizer54, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer138.Add(sbSizer53, 0, wx.ALL | wx.EXPAND, 5)

        bSizer139 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer139.Add((0, 0), 1, wx.EXPAND, 5)

        self.chienCard1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard1, 0, wx.ALL, 5)

        self.chienCard2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard2, 0, wx.ALL, 5)

        self.chienCard3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard3, 0, wx.ALL, 5)

        bSizer139.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer138.Add(bSizer139, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.score5Vu = wx.Button(self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer138.Add(self.score5Vu, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizer(bSizer138)
        self.Layout()

        # Connect Events
        self.score5Vu.Bind(wx.EVT_BUTTON, self.onScore5Vu)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onScore5Vu(self, event):
        event.Skip()
