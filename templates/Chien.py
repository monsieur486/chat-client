# -*- coding: utf-8 -*-


import wx


from appcore.translate import _


class Chien(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(713, 401), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer138 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText224 = wx.StaticText(self, wx.ID_ANY, _(u"LE CHIEN"), wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText224.Wrap(-1)

        self.m_staticText224.SetFont(
            wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer138.Add(self.m_staticText224, 1, wx.ALL | wx.EXPAND, 5)

        bSizer138.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer139 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer139.Add((0, 0), 1, wx.EXPAND, 5)

        self.chienCard1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard1, 0, wx.ALL, 5)

        self.chienCard2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard2, 0, wx.ALL, 5)

        self.chienCard3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard3, 0, wx.ALL, 5)

        self.chienCard4 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard4, 0, wx.ALL, 5)

        self.chienCard5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard5, 0, wx.ALL, 5)

        self.chienCard6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(96, 180), 0)
        bSizer139.Add(self.chienCard6, 0, wx.ALL, 5)

        bSizer139.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer138.Add(bSizer139, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer138.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button67 = wx.Button(self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer138.Add(self.m_button67, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizer(bSizer138)
        self.Layout()

    def __del__(self):
        pass
