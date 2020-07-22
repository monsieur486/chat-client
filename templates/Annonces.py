# -*- coding: utf-8 -*-


import wx


from appcore.translate import _


class Annonces(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(1062, 401), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer138 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText224 = wx.StaticText(self, wx.ID_ANY, _(u"ANNONCE"), wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText224.Wrap(-1)

        self.m_staticText224.SetFont(
            wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer138.Add(self.m_staticText224, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        self.annonceText = wx.StaticText(self, wx.ID_ANY, _(u"ANNONCE"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.annonceText.Wrap(-1)

        bSizer138.Add(self.annonceText, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 15)

        bSizer138.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer87 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer87.Add((0, 0), 1, wx.EXPAND, 5)

        self.gameTabCenterCard1 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard1, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard2 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard2, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard3 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard3, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard4 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard4, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard5 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard5, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard6 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard6, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard7 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard7, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard8 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard8, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard9 = wx.StaticBitmap(self, wx.ID_ANY,
                                                  wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                  wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard9, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard10 = wx.StaticBitmap(self, wx.ID_ANY,
                                                   wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                   wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard10, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard11 = wx.StaticBitmap(self, wx.ID_ANY,
                                                   wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                   wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard11, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard12 = wx.StaticBitmap(self, wx.ID_ANY,
                                                   wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                   wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard12, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard13 = wx.StaticBitmap(self, wx.ID_ANY,
                                                   wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                   wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard13, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCard14 = wx.StaticBitmap(self, wx.ID_ANY,
                                                   wx.Bitmap(u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY),
                                                   wx.DefaultPosition, wx.Size(60, 180), 0)
        bSizer87.Add(self.gameTabCenterCard14, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gameTabCenterCardFull = wx.StaticBitmap(self, wx.ID_ANY,
                                                     wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                                     wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer87.Add(self.gameTabCenterCardFull, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        bSizer87.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer138.Add(bSizer87, 1, wx.EXPAND, 5)

        bSizer138.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button67 = wx.Button(self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer138.Add(self.m_button67, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizer(bSizer138)
        self.Layout()

    def __del__(self):
        pass
