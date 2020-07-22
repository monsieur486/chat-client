# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 May 18 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

import gettext
_ = gettext.gettext

201 = 1000
202 = 1001
203 = 1002
204 = 1003
205 = 1004
206 = 1005
101 = 1006
102 = 1007
103 = 1008
104 = 1009
105 = 1010
106 = 1011
107 = 1012
108 = 1013
109 = 1014
110 = 1015
111 = 1016
112 = 1017
113 = 1018
114 = 1019
115 = 1020
116 = 1021
117 = 1022
118 = 1023
119 = 1024
120 = 1025
121 = 1026
122 = 1027
123 = 1028
124 = 1029

###########################################################################
## Class AppFrame
###########################################################################

class AppFrame ( wx.Frame ):


    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onMenuQuit( self, event ):
        event.Skip()

    def cnxTabOnCnxBtn( self, event ):
        event.Skip()


    def onCnxTabPlay4( self, event ):
        event.Skip()

    def onCnxTabPlay5( self, event ):
        event.Skip()

    def onCnxTabJoinBtn( self, event ):
        event.Skip()

    def onGameSelect( self, event ):
        event.Skip()

    def onCnxTabCreateBtn( self, event ):
        event.Skip()

    def onCnxTabCreatePrivate( self, event ):
        event.Skip()

    def onCnxTabPly1Change( self, event ):
        event.Skip()

    def onCnxTabPly2Change( self, event ):
        event.Skip()

    def onCnxTabPly3Change( self, event ):
        event.Skip()

    def onCnxTabPly4Change( self, event ):
        event.Skip()

    def onCnxTabPly5Change( self, event ):
        event.Skip()

    def onCnxTabLeave( self, event ):
        event.Skip()

    def onCnxTabFicheGameStart( self, event ):
        event.Skip()

    def onImportChange( self, event ):
        event.Skip()


###########################################################################
## Class Annonces
###########################################################################

class Annonces ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1062,401 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer138 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText224 = wx.StaticText( self, wx.ID_ANY, _(u"ANNONCE"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText224.Wrap( -1 )

        self.m_staticText224.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer138.Add( self.m_staticText224, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

        self.annonceText = wx.StaticText( self, wx.ID_ANY, _(u"ANNONCE"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.annonceText.Wrap( -1 )

        bSizer138.Add( self.annonceText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 15 )


        bSizer138.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer87 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer87.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.gameTabCenterCard1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard1, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard2, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard3, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard4, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard5 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard5, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard6, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard7 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard7, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard8 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard8, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard9 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard9, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard10 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard10, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard11 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard11, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard12 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard12, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard13 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard13, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCard14 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCard14, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

        self.gameTabCenterCardFull = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer87.Add( self.gameTabCenterCardFull, 0, wx.ALIGN_CENTER_VERTICAL, 0 )


        bSizer87.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer138.Add( bSizer87, 1, wx.EXPAND, 5 )


        bSizer138.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button67 = wx.Button( self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer138.Add( self.m_button67, 0, wx.ALIGN_CENTER|wx.ALL, 10 )


        self.SetSizer( bSizer138 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class Chien
###########################################################################

class Chien ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 713,401 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer138 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText224 = wx.StaticText( self, wx.ID_ANY, _(u"LE CHIEN"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText224.Wrap( -1 )

        self.m_staticText224.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer138.Add( self.m_staticText224, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer138.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer139 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer139.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.chienCard1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard1, 0, wx.ALL, 5 )

        self.chienCard2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard2, 0, wx.ALL, 5 )

        self.chienCard3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard3, 0, wx.ALL, 5 )

        self.chienCard4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard4, 0, wx.ALL, 5 )

        self.chienCard5 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard5, 0, wx.ALL, 5 )

        self.chienCard6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard6, 0, wx.ALL, 5 )


        bSizer139.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer138.Add( bSizer139, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer138.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button67 = wx.Button( self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer138.Add( self.m_button67, 0, wx.ALIGN_CENTER|wx.ALL, 10 )


        self.SetSizer( bSizer138 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class Score5
###########################################################################

class Score5 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 713,777 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer138 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText224 = wx.StaticText( self, wx.ID_ANY, _(u"SCORE"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText224.Wrap( -1 )

        self.m_staticText224.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer138.Add( self.m_staticText224, 1, wx.ALL|wx.EXPAND, 5 )

        sbSizer53 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Détails") ), wx.VERTICAL )

        bSizer169 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer170 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText264 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Preneur : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText264.Wrap( -1 )

        bSizer170.Add( self.m_staticText264, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText265 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Appel : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText265.Wrap( -1 )

        bSizer170.Add( self.m_staticText265, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText266 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Contrat : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText266.Wrap( -1 )

        bSizer170.Add( self.m_staticText266, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText267 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Bouts : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText267.Wrap( -1 )

        bSizer170.Add( self.m_staticText267, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText268 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Points : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText268.Wrap( -1 )

        bSizer170.Add( self.m_staticText268, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText274 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Petit au bout : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText274.Wrap( -1 )

        bSizer170.Add( self.m_staticText274, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText2741 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Annonces : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2741.Wrap( -1 )

        bSizer170.Add( self.m_staticText2741, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText27412 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Chelem : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27412.Wrap( -1 )

        bSizer170.Add( self.m_staticText27412, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText27411 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"RESULTAT :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27411.Wrap( -1 )

        bSizer170.Add( self.m_staticText27411, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        bSizer169.Add( bSizer170, 1, 0, 5 )

        bSizer171 = wx.BoxSizer( wx.VERTICAL )

        self.score5Preneur = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Preneur.Wrap( -1 )

        bSizer171.Add( self.score5Preneur, 0, wx.ALL, 5 )

        self.score5Appel = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Appel.Wrap( -1 )

        bSizer171.Add( self.score5Appel, 0, wx.ALL, 5 )

        self.score5Contrat = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Contrat.Wrap( -1 )

        bSizer171.Add( self.score5Contrat, 0, wx.ALL, 5 )

        self.score5Bouts = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Bouts.Wrap( -1 )

        bSizer171.Add( self.score5Bouts, 0, wx.ALL, 5 )

        self.score5Points = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Points.Wrap( -1 )

        bSizer171.Add( self.score5Points, 0, wx.ALL, 5 )

        self.score5PAB = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5PAB.Wrap( -1 )

        bSizer171.Add( self.score5PAB, 0, wx.ALL, 5 )

        self.score5Annonces = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Annonces.Wrap( -1 )

        bSizer171.Add( self.score5Annonces, 0, wx.ALL, 5 )

        self.score5Chelem = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Chelem.Wrap( -1 )

        bSizer171.Add( self.score5Chelem, 0, wx.ALL, 5 )

        self.score5Resultat = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Resultat.Wrap( -1 )

        bSizer171.Add( self.score5Resultat, 0, wx.ALL, 5 )


        bSizer169.Add( bSizer171, 1, 0, 5 )


        sbSizer53.Add( bSizer169, 1, wx.EXPAND, 5 )

        sbSizer54 = wx.StaticBoxSizer( wx.StaticBox( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Points") ), wx.HORIZONTAL )

        sbSizer55 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.score5Player1 = wx.StaticText( sbSizer55.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Player1.Wrap( -1 )

        sbSizer55.Add( self.score5Player1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText277 = wx.StaticText( sbSizer55.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText277.Wrap( -1 )

        sbSizer55.Add( self.m_staticText277, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer55, 1, wx.ALL, 5 )

        sbSizer551 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.score5Player2 = wx.StaticText( sbSizer551.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Player2.Wrap( -1 )

        sbSizer551.Add( self.score5Player2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2771 = wx.StaticText( sbSizer551.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2771.Wrap( -1 )

        sbSizer551.Add( self.m_staticText2771, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer551, 1, wx.ALL, 5 )

        sbSizer552 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.score5Player3 = wx.StaticText( sbSizer552.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Player3.Wrap( -1 )

        sbSizer552.Add( self.score5Player3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2772 = wx.StaticText( sbSizer552.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2772.Wrap( -1 )

        sbSizer552.Add( self.m_staticText2772, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer552, 1, wx.ALL, 5 )

        sbSizer553 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.score5Player4 = wx.StaticText( sbSizer553.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Player4.Wrap( -1 )

        sbSizer553.Add( self.score5Player4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2773 = wx.StaticText( sbSizer553.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2773.Wrap( -1 )

        sbSizer553.Add( self.m_staticText2773, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer553, 1, wx.ALL, 5 )

        sbSizer554 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.score5Player5 = wx.StaticText( sbSizer554.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.score5Player5.Wrap( -1 )

        sbSizer554.Add( self.score5Player5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2774 = wx.StaticText( sbSizer554.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2774.Wrap( -1 )

        sbSizer554.Add( self.m_staticText2774, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer554, 1, wx.ALL, 5 )


        sbSizer53.Add( sbSizer54, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer138.Add( sbSizer53, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer139 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer139.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.chienCard1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard1, 0, wx.ALL, 5 )

        self.chienCard2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard2, 0, wx.ALL, 5 )

        self.chienCard3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard3, 0, wx.ALL, 5 )


        bSizer139.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer138.Add( bSizer139, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.score5Vu = wx.Button( self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer138.Add( self.score5Vu, 0, wx.ALIGN_CENTER|wx.ALL, 10 )


        self.SetSizer( bSizer138 )
        self.Layout()

        # Connect Events
        self.score5Vu.Bind( wx.EVT_BUTTON, self.onScore5Vu )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onScore5Vu( self, event ):
        event.Skip()


###########################################################################
## Class Score4
###########################################################################

class Score4 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 713,777 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer138 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText224 = wx.StaticText( self, wx.ID_ANY, _(u"SCORE"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText224.Wrap( -1 )

        self.m_staticText224.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer138.Add( self.m_staticText224, 1, wx.ALL|wx.EXPAND, 5 )

        sbSizer53 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Détails") ), wx.VERTICAL )

        bSizer169 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer170 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText264 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Preneur : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText264.Wrap( -1 )

        bSizer170.Add( self.m_staticText264, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText266 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Contrat : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText266.Wrap( -1 )

        bSizer170.Add( self.m_staticText266, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText267 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Bouts : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText267.Wrap( -1 )

        bSizer170.Add( self.m_staticText267, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText268 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Points : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText268.Wrap( -1 )

        bSizer170.Add( self.m_staticText268, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText274 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Petit au bout : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText274.Wrap( -1 )

        bSizer170.Add( self.m_staticText274, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText2741 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Annonces : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2741.Wrap( -1 )

        bSizer170.Add( self.m_staticText2741, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText27412 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Chelem : "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27412.Wrap( -1 )

        bSizer170.Add( self.m_staticText27412, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_staticText27411 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"RESULTAT :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27411.Wrap( -1 )

        bSizer170.Add( self.m_staticText27411, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        bSizer169.Add( bSizer170, 1, 0, 5 )

        bSizer171 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText269 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText269.Wrap( -1 )

        bSizer171.Add( self.m_staticText269, 0, wx.ALL, 5 )

        self.m_staticText271 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText271.Wrap( -1 )

        bSizer171.Add( self.m_staticText271, 0, wx.ALL, 5 )

        self.m_staticText272 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText272.Wrap( -1 )

        bSizer171.Add( self.m_staticText272, 0, wx.ALL, 5 )

        self.m_staticText273 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText273.Wrap( -1 )

        bSizer171.Add( self.m_staticText273, 0, wx.ALL, 5 )

        self.m_staticText275 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText275.Wrap( -1 )

        bSizer171.Add( self.m_staticText275, 0, wx.ALL, 5 )

        self.m_staticText2751 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2751.Wrap( -1 )

        bSizer171.Add( self.m_staticText2751, 0, wx.ALL, 5 )

        self.m_staticText2752 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2752.Wrap( -1 )

        bSizer171.Add( self.m_staticText2752, 0, wx.ALL, 5 )

        self.m_staticText2753 = wx.StaticText( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2753.Wrap( -1 )

        bSizer171.Add( self.m_staticText2753, 0, wx.ALL, 5 )


        bSizer169.Add( bSizer171, 1, 0, 5 )


        sbSizer53.Add( bSizer169, 1, wx.EXPAND, 5 )

        sbSizer54 = wx.StaticBoxSizer( wx.StaticBox( sbSizer53.GetStaticBox(), wx.ID_ANY, _(u"Points") ), wx.HORIZONTAL )

        sbSizer551 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.m_staticText2761 = wx.StaticText( sbSizer551.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2761.Wrap( -1 )

        sbSizer551.Add( self.m_staticText2761, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2771 = wx.StaticText( sbSizer551.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2771.Wrap( -1 )

        sbSizer551.Add( self.m_staticText2771, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer551, 1, wx.ALL, 5 )

        sbSizer552 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.m_staticText2762 = wx.StaticText( sbSizer552.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2762.Wrap( -1 )

        sbSizer552.Add( self.m_staticText2762, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2772 = wx.StaticText( sbSizer552.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2772.Wrap( -1 )

        sbSizer552.Add( self.m_staticText2772, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer552, 1, wx.ALL, 5 )

        sbSizer553 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.m_staticText2763 = wx.StaticText( sbSizer553.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2763.Wrap( -1 )

        sbSizer553.Add( self.m_staticText2763, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2773 = wx.StaticText( sbSizer553.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2773.Wrap( -1 )

        sbSizer553.Add( self.m_staticText2773, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer553, 1, wx.ALL, 5 )

        sbSizer554 = wx.StaticBoxSizer( wx.StaticBox( sbSizer54.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.m_staticText2764 = wx.StaticText( sbSizer554.GetStaticBox(), wx.ID_ANY, _(u"Player"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2764.Wrap( -1 )

        sbSizer554.Add( self.m_staticText2764, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_staticText2774 = wx.StaticText( sbSizer554.GetStaticBox(), wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2774.Wrap( -1 )

        sbSizer554.Add( self.m_staticText2774, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer54.Add( sbSizer554, 1, wx.ALL, 5 )


        sbSizer53.Add( sbSizer54, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer138.Add( sbSizer53, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer139 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer139.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.chienCard1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard1, 0, wx.ALL, 5 )

        self.chienCard2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard2, 0, wx.ALL, 5 )

        self.chienCard3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard3, 0, wx.ALL, 5 )

        self.chienCard4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard4, 0, wx.ALL, 5 )

        self.chienCard5 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard5, 0, wx.ALL, 5 )

        self.chienCard6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer139.Add( self.chienCard6, 0, wx.ALL, 5 )


        bSizer139.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer138.Add( bSizer139, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button67 = wx.Button( self, wx.ID_OK, _(u"VU"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer138.Add( self.m_button67, 0, wx.ALIGN_CENTER|wx.ALL, 10 )


        self.SetSizer( bSizer138 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class Game4
###########################################################################



###########################################################################
## Class Game5
###########################################################################



