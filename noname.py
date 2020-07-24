# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jul 22 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

201 = 1000
202 = 1001
203 = 1002
101 = 1003
102 = 1004
103 = 1005
104 = 1006
105 = 1007
106 = 1008
107 = 1009
108 = 1010
109 = 1011
110 = 1012
111 = 1013
112 = 1014
113 = 1015
114 = 1016
115 = 1017
116 = 1018
117 = 1019
118 = 1020

###########################################################################
## Class AppFrame
###########################################################################

class AppFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ChatPubSub", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Quitter"+ u"\t" + u"ctrl-q", u"Quitter l'application", wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menubar1.Append( self.m_menu1, u"Menu" )

        self.SetMenuBar( self.m_menubar1 )

        self.mainStatusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.connexionTab = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer45 = wx.BoxSizer( wx.VERTICAL )

        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer46.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.cnxTabLock1 = wx.StaticBitmap( self.connexionTab, wx.ID_ANY, wx.Bitmap( u"public/icons/16x16_user.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer46.Add( self.cnxTabLock1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.cnxTabUserEntry = wx.TextCtrl( self.connexionTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer46.Add( self.cnxTabUserEntry, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.cnxTabLock11 = wx.StaticBitmap( self.connexionTab, wx.ID_ANY, wx.Bitmap( u"public/icons/16x16_key.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer46.Add( self.cnxTabLock11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.cnxTabPasswordEntry = wx.TextCtrl( self.connexionTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
        bSizer46.Add( self.cnxTabPasswordEntry, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.cnxTabCnxBtn = wx.Button( self.connexionTab, wx.ID_ANY, u"Connexion", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer46.Add( self.cnxTabCnxBtn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.cnxTabLock111 = wx.StaticBitmap( self.connexionTab, wx.ID_ANY, wx.Bitmap( u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer46.Add( self.cnxTabLock111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText45 = wx.StaticText( self.connexionTab, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText45.Wrap( -1 )

        bSizer46.Add( self.m_staticText45, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer46.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer45.Add( bSizer46, 0, wx.EXPAND, 5 )

        bSizer48 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer49 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl6 = wx.TextCtrl( self.connexionTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer49.Add( self.m_textCtrl6, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer48.Add( bSizer49, 1, wx.EXPAND, 5 )

        bSizer50 = wx.BoxSizer( wx.VERTICAL )

        self.m_button11 = wx.Button( self.connexionTab, wx.ID_ANY, u"Equipe", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer50.Add( self.m_button11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.cnxTabLock1111 = wx.StaticBitmap( self.connexionTab, wx.ID_ANY, wx.Bitmap( u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.cnxTabLock1111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText451 = wx.StaticText( self.connexionTab, wx.ID_ANY, u"xxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText451.Wrap( -1 )

        bSizer51.Add( self.m_staticText451, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer50.Add( bSizer51, 0, wx.EXPAND, 5 )

        bSizer511 = wx.BoxSizer( wx.HORIZONTAL )

        self.cnxTabLock11111 = wx.StaticBitmap( self.connexionTab, wx.ID_ANY, wx.Bitmap( u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer511.Add( self.cnxTabLock11111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText4511 = wx.StaticText( self.connexionTab, wx.ID_ANY, u"xxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4511.Wrap( -1 )

        bSizer511.Add( self.m_staticText4511, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer50.Add( bSizer511, 0, wx.EXPAND, 5 )

        bSizer513 = wx.BoxSizer( wx.HORIZONTAL )

        self.cnxTabLock11113 = wx.StaticBitmap( self.connexionTab, wx.ID_ANY, wx.Bitmap( u"public/icons/16x16_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer513.Add( self.cnxTabLock11113, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText4513 = wx.StaticText( self.connexionTab, wx.ID_ANY, u"xxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4513.Wrap( -1 )

        bSizer513.Add( self.m_staticText4513, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer50.Add( bSizer513, 0, wx.EXPAND, 5 )

        m_radioBox3Choices = [ u"Message Privé", u"Ne pas déranger" ]
        self.m_radioBox3 = wx.RadioBox( self.connexionTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox3.SetSelection( 0 )
        bSizer50.Add( self.m_radioBox3, 0, wx.ALL, 5 )


        bSizer48.Add( bSizer50, 0, wx.EXPAND, 5 )


        bSizer45.Add( bSizer48, 1, wx.EXPAND, 5 )

        bSizer59 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText53 = wx.StaticText( self.connexionTab, wx.ID_ANY, u"xxxxxxxxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText53.Wrap( -1 )

        bSizer59.Add( self.m_staticText53, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl7 = wx.TextCtrl( self.connexionTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer59.Add( self.m_textCtrl7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button12 = wx.Button( self.connexionTab, wx.ID_ANY, u"Envoyer", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer59.Add( self.m_button12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer45.Add( bSizer59, 0, wx.EXPAND, 5 )


        self.connexionTab.SetSizer( bSizer45 )
        self.connexionTab.Layout()
        bSizer45.Fit( self.connexionTab )
        bSizer1.Add( self.connexionTab, 1, wx.EXPAND |wx.ALL, 5 )

        self.mailBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer1.Add( self.mailBox, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onMenuQuit, id = self.m_menuItem1.GetId() )
        self.cnxTabPasswordEntry.Bind( wx.EVT_TEXT_ENTER, self.cnxTabOnCnxBtn )
        self.cnxTabCnxBtn.Bind( wx.EVT_BUTTON, self.cnxTabOnCnxBtn )
        self.mailBox.Bind( wx.EVT_TEXT, self.onImportChange )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onMenuQuit( self, event ):
        event.Skip()

    def cnxTabOnCnxBtn( self, event ):
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

        self.m_staticText224 = wx.StaticText( self, wx.ID_ANY, u"ANNONCE", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText224.Wrap( -1 )

        self.m_staticText224.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer138.Add( self.m_staticText224, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

        self.annonceText = wx.StaticText( self, wx.ID_ANY, u"ANNONCE", wx.DefaultPosition, wx.DefaultSize, 0 )
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

        self.m_button67 = wx.Button( self, wx.ID_OK, u"VU", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer138.Add( self.m_button67, 0, wx.ALIGN_CENTER|wx.ALL, 10 )


        self.SetSizer( bSizer138 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class Game5
###########################################################################

class Game5 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1400,900 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer421 = wx.BoxSizer( wx.VERTICAL )

        bSizer192 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer441 = wx.BoxSizer( wx.VERTICAL )

        bSizer45122 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer642 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer7222 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabGameDonneLbl = wx.StaticText( self, wx.ID_ANY, u"Donne", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabGameDonneLbl.Wrap( -1 )

        bSizer7222.Add( self.gameTabGameDonneLbl, 0, wx.ALL, 5 )

        self.gameTabGameContratLbl = wx.StaticText( self, wx.ID_ANY, u"Contrat", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabGameContratLbl.Wrap( -1 )

        bSizer7222.Add( self.gameTabGameContratLbl, 0, wx.ALL, 5 )

        self.meTabGamePreneurLbl = wx.StaticText( self, wx.ID_ANY, u"Preneur", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.meTabGamePreneurLbl.Wrap( -1 )

        bSizer7222.Add( self.meTabGamePreneurLbl, 0, wx.ALL, 5 )

        self.meTabGameAppelLb = wx.StaticText( self, wx.ID_ANY, u"Appel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.meTabGameAppelLb.Wrap( -1 )

        bSizer7222.Add( self.meTabGameAppelLb, 0, wx.ALL, 5 )

        self.gameTabGameTourLbl = wx.StaticText( self, wx.ID_ANY, u"Tour", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabGameTourLbl.Wrap( -1 )

        bSizer7222.Add( self.gameTabGameTourLbl, 0, wx.ALL, 5 )


        bSizer642.Add( bSizer7222, 0, wx.EXPAND, 5 )

        bSizer72211 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabGameDonne = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
        self.gameTabGameDonne.Wrap( -1 )

        bSizer72211.Add( self.gameTabGameDonne, 0, wx.ALL, 5 )

        self.gameTabGameContrat = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabGameContrat.Wrap( -1 )

        bSizer72211.Add( self.gameTabGameContrat, 0, wx.ALL, 5 )

        self.gameTabGamePreneur = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabGamePreneur.Wrap( -1 )

        bSizer72211.Add( self.gameTabGamePreneur, 0, wx.ALL, 5 )

        self.gameTabGameAppel = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabGameAppel.Wrap( -1 )

        bSizer72211.Add( self.gameTabGameAppel, 0, wx.ALL, 5 )

        self.gameTabGameTour = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabGameTour.Wrap( -1 )

        bSizer72211.Add( self.gameTabGameTour, 0, wx.ALL, 5 )


        bSizer642.Add( bSizer72211, 0, wx.EXPAND, 5 )


        bSizer45122.Add( bSizer642, 0, wx.EXPAND, 5 )


        bSizer45122.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer733 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabNordLed = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer733.Add( self.gameTabNordLed, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabNordStatus = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer733.Add( self.gameTabNordStatus, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabNordDealer = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer733.Add( self.gameTabNordDealer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabNordSound = wx.ToggleButton( self, wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer733.Add( self.gameTabNordSound, 0, 0, 5 )


        bSizer45122.Add( bSizer733, 0, wx.EXPAND, 5 )

        bSizer4914 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabNordCard = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer4914.Add( self.gameTabNordCard, 0, wx.ALL, 5 )


        bSizer45122.Add( bSizer4914, 0, wx.EXPAND, 5 )

        bSizer281 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabNord = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
        self.gameTabNord.Wrap( -1 )

        self.gameTabNord.SetToolTip( u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0" )

        bSizer281.Add( self.gameTabNord, 0, wx.ALL, 5 )

        self.gameTabNordAction = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabNordAction.Wrap( -1 )

        bSizer281.Add( self.gameTabNordAction, 0, wx.ALL, 5 )


        bSizer45122.Add( bSizer281, 0, wx.ALL, 5 )


        bSizer45122.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer7311 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabNord2Led = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7311.Add( self.gameTabNord2Led, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.gameTabNord2Status = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7311.Add( self.gameTabNord2Status, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.gameTabNord2Dealer = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7311.Add( self.gameTabNord2Dealer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabNord2Sound = wx.ToggleButton( self, wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7311.Add( self.gameTabNord2Sound, 0, 0, 5 )


        bSizer45122.Add( bSizer7311, 0, wx.EXPAND, 5 )

        bSizer49121 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabNord2Card = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer49121.Add( self.gameTabNord2Card, 0, wx.ALL, 5 )


        bSizer45122.Add( bSizer49121, 0, wx.EXPAND, 5 )

        bSizer2811 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabNord2 = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
        self.gameTabNord2.Wrap( -1 )

        self.gameTabNord2.SetToolTip( u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0" )

        bSizer2811.Add( self.gameTabNord2, 0, wx.ALL, 5 )

        self.gameTabNord2Action = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabNord2Action.Wrap( -1 )

        bSizer2811.Add( self.gameTabNord2Action, 0, wx.ALL, 5 )


        bSizer45122.Add( bSizer2811, 0, wx.ALL, 5 )


        bSizer45122.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer6411 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabChat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer6411.Add( self.gameTabChat, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer45122.Add( bSizer6411, 1, wx.EXPAND, 5 )


        bSizer441.Add( bSizer45122, 0, wx.EXPAND, 0 )


        bSizer441.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer45112 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer45112.Add( ( 0, 0), 0, wx.LEFT, 15 )

        bSizer7323 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabOuestLed = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7323.Add( self.gameTabOuestLed, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabOuestStatus = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7323.Add( self.gameTabOuestStatus, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabOuestDealer = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7323.Add( self.gameTabOuestDealer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabOuestSound = wx.ToggleButton( self, wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7323.Add( self.gameTabOuestSound, 0, 0, 5 )


        bSizer45112.Add( bSizer7323, 0, wx.EXPAND, 5 )

        bSizer49111 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabOuestCard = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer49111.Add( self.gameTabOuestCard, 0, wx.ALL, 5 )


        bSizer45112.Add( bSizer49111, 0, wx.EXPAND, 5 )

        bSizer2813 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabOuest = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
        self.gameTabOuest.Wrap( -1 )

        self.gameTabOuest.SetToolTip( u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0" )

        bSizer2813.Add( self.gameTabOuest, 0, wx.ALL, 5 )

        self.gameTabOuestAction = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabOuestAction.Wrap( -1 )

        bSizer2813.Add( self.gameTabOuestAction, 0, wx.ALL, 5 )


        bSizer45112.Add( bSizer2813, 0, wx.EXPAND, 5 )


        bSizer45112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer781 = wx.BoxSizer( wx.VERTICAL )

        bSizer129 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer128 = wx.BoxSizer( wx.HORIZONTAL )

        self.gameTabChien1 = wx.StaticBitmap( self, 201, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer128.Add( self.gameTabChien1, 0, wx.ALL, 5 )

        self.gameTabChien2 = wx.StaticBitmap( self, 202, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer128.Add( self.gameTabChien2, 0, wx.ALL, 5 )

        self.gameTabChien3 = wx.StaticBitmap( self, 203, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer128.Add( self.gameTabChien3, 0, wx.ALL, 5 )


        bSizer129.Add( bSizer128, 0, wx.EXPAND, 5 )


        bSizer781.Add( bSizer129, 1, wx.EXPAND, 5 )

        bSizer2791 = wx.BoxSizer( wx.HORIZONTAL )

        self.gameTabChienOk = wx.Button( self, wx.ID_ANY, u"Valider", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2791.Add( self.gameTabChienOk, 0, wx.ALL, 5 )

        self.gameTabCroupier = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabCroupier.Wrap( -1 )

        self.gameTabCroupier.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer2791.Add( self.gameTabCroupier, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer781.Add( bSizer2791, 0, wx.EXPAND, 5 )


        bSizer45112.Add( bSizer781, 0, wx.ALL, 5 )


        bSizer45112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer73211 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabEstLed = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73211.Add( self.gameTabEstLed, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.gameTabEstStatus = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73211.Add( self.gameTabEstStatus, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.gameTabEstDealer = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73211.Add( self.gameTabEstDealer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.gameTabEstSound = wx.ToggleButton( self, wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73211.Add( self.gameTabEstSound, 0, 0, 5 )


        bSizer45112.Add( bSizer73211, 0, wx.EXPAND, 5 )

        bSizer49131 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabEstCard = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer49131.Add( self.gameTabEstCard, 0, wx.ALL, 5 )


        bSizer45112.Add( bSizer49131, 0, wx.EXPAND, 5 )

        bSizer2812 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabEst = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
        self.gameTabEst.Wrap( -1 )

        self.gameTabEst.SetToolTip( u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0" )

        bSizer2812.Add( self.gameTabEst, 0, wx.ALL, 5 )

        self.gameTabEstAction = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabEstAction.Wrap( -1 )

        bSizer2812.Add( self.gameTabEstAction, 0, wx.ALL, 5 )


        bSizer45112.Add( bSizer2812, 0, wx.EXPAND, 5 )


        bSizer45112.Add( ( 0, 0), 0, wx.RIGHT, 15 )


        bSizer441.Add( bSizer45112, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 10 )


        bSizer441.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer451211 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer451211.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer73221 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabUserLed = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_led_grey.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73221.Add( self.gameTabUserLed, 0, wx.ALL, 5 )

        self.gameTabUserStatus = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_full_star.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73221.Add( self.gameTabUserStatus, 0, wx.ALL, 5 )

        self.gameTabUserDealer = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/icons/40x40_dealer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer73221.Add( self.gameTabUserDealer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer451211.Add( bSizer73221, 0, wx.EXPAND, 5 )

        self.gameTabUserCardSelect = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"public/bigCards/0_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer451211.Add( self.gameTabUserCardSelect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        bSizer28132 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabUser = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
        self.gameTabUser.Wrap( -1 )

        self.gameTabUser.SetToolTip( u"Location : --\nParties à 4 : 0\nParties à 5 : 0\nTOTAL : 0" )

        bSizer28132.Add( self.gameTabUser, 0, wx.ALL, 5 )

        self.gameTabUserAction = wx.StaticText( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabUserAction.Wrap( -1 )

        bSizer28132.Add( self.gameTabUserAction, 0, wx.ALL, 5 )

        self.gameTabPlayCardBtn = wx.Button( self, wx.ID_ANY, u"Jouer cette carte", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28132.Add( self.gameTabPlayCardBtn, 0, wx.ALL, 5 )

        self.gameTabVote = wx.Button( self, wx.ID_ANY, u"Vu", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28132.Add( self.gameTabVote, 0, wx.ALL, 5 )


        bSizer451211.Add( bSizer28132, 0, wx.ALL, 5 )


        bSizer451211.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer1031 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer8222 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabContratPasse = wx.Button( self, wx.ID_ANY, u"Je passe", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer8222.Add( self.gameTabContratPasse, 0, wx.ALL, 5 )

        self.gameTabContratPetite = wx.Button( self, wx.ID_ANY, u"Petite", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer8222.Add( self.gameTabContratPetite, 0, wx.ALL, 5 )

        self.gameTabContratGarde = wx.Button( self, wx.ID_ANY, u"Garde", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer8222.Add( self.gameTabContratGarde, 0, wx.ALL, 5 )


        bSizer1031.Add( bSizer8222, 0, wx.EXPAND, 5 )

        bSizer82211 = wx.BoxSizer( wx.VERTICAL )

        self.gameTabContratGardeSans = wx.Button( self, wx.ID_ANY, u"Garde Sans", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer82211.Add( self.gameTabContratGardeSans, 0, wx.ALL, 5 )

        self.gameTabContratGardecontre = wx.Button( self, wx.ID_ANY, u"Garde Contre", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer82211.Add( self.gameTabContratGardecontre, 0, wx.ALL, 5 )

        self.gameTabChelem = wx.CheckBox( self, wx.ID_ANY, u"Chelem", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer82211.Add( self.gameTabChelem, 0, wx.ALL, 5 )


        bSizer1031.Add( bSizer82211, 0, wx.EXPAND, 5 )


        bSizer451211.Add( bSizer1031, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer441.Add( bSizer451211, 0, wx.EXPAND, 0 )


        bSizer192.Add( bSizer441, 1, wx.EXPAND, 5 )

        sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Fiche de Match" ), wx.VERTICAL )

        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Partie" ), wx.VERTICAL )

        bSizer761 = wx.BoxSizer( wx.HORIZONTAL )

        self.cnxTabFicheGameIsPlayable = wx.StaticBitmap( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer761.Add( self.cnxTabFicheGameIsPlayable, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.cnxTabFicheGameName = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cnxTabFicheGameName.Wrap( -1 )

        bSizer761.Add( self.cnxTabFicheGameName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        sbSizer8.Add( bSizer761, 1, wx.EXPAND, 5 )


        sbSizer23.Add( sbSizer8, 0, wx.ALL|wx.EXPAND, 5 )

        sbSizer812 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Scores et Positions" ), wx.HORIZONTAL )

        bSizer154 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText237 = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"-1-", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText237.Wrap( -1 )

        bSizer154.Add( self.m_staticText237, 0, wx.ALL, 5 )

        self.m_staticText2371 = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"-2-", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2371.Wrap( -1 )

        bSizer154.Add( self.m_staticText2371, 0, wx.ALL, 5 )

        self.m_staticText2372 = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"-3-", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2372.Wrap( -1 )

        bSizer154.Add( self.m_staticText2372, 0, wx.ALL, 5 )

        self.m_staticText2373 = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"-4-", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2373.Wrap( -1 )

        bSizer154.Add( self.m_staticText2373, 0, wx.ALL, 5 )

        self.cnxTabFichePos5Label = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"-5-", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cnxTabFichePos5Label.Wrap( -1 )

        bSizer154.Add( self.cnxTabFichePos5Label, 0, wx.ALL, 5 )


        sbSizer812.Add( bSizer154, 0, wx.ALL, 5 )

        bSizer1541 = wx.BoxSizer( wx.VERTICAL )

        self.cnxTabFichePos1Nickname = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_RIGHT )
        self.cnxTabFichePos1Nickname.Wrap( -1 )

        bSizer1541.Add( self.cnxTabFichePos1Nickname, 0, wx.ALL|wx.EXPAND, 5 )

        self.cnxTabFichePos2Nickname = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_RIGHT )
        self.cnxTabFichePos2Nickname.Wrap( -1 )

        bSizer1541.Add( self.cnxTabFichePos2Nickname, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.cnxTabFichePos3Nickname = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_RIGHT )
        self.cnxTabFichePos3Nickname.Wrap( -1 )

        bSizer1541.Add( self.cnxTabFichePos3Nickname, 0, wx.ALL|wx.EXPAND, 5 )

        self.cnxTabFichePos4Nickname = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_RIGHT )
        self.cnxTabFichePos4Nickname.Wrap( -1 )

        bSizer1541.Add( self.cnxTabFichePos4Nickname, 0, wx.ALL|wx.EXPAND, 5 )

        self.cnxTabFichePos5Nickname = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_RIGHT )
        self.cnxTabFichePos5Nickname.Wrap( -1 )

        bSizer1541.Add( self.cnxTabFichePos5Nickname, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer812.Add( bSizer1541, 1, wx.ALL, 5 )

        bSizer15411 = wx.BoxSizer( wx.VERTICAL )

        self.cnxTabFichePos1Score = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.cnxTabFichePos1Score.Wrap( -1 )

        bSizer15411.Add( self.cnxTabFichePos1Score, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.cnxTabFichePos2Score = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cnxTabFichePos2Score.Wrap( -1 )

        bSizer15411.Add( self.cnxTabFichePos2Score, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.cnxTabFichePos3Score = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cnxTabFichePos3Score.Wrap( -1 )

        bSizer15411.Add( self.cnxTabFichePos3Score, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.cnxTabFichePos4Score = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.cnxTabFichePos4Score.Wrap( -1 )

        bSizer15411.Add( self.cnxTabFichePos4Score, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.cnxTabFichePos5Score = wx.StaticText( sbSizer812.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.cnxTabFichePos5Score.Wrap( -1 )

        bSizer15411.Add( self.cnxTabFichePos5Score, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        sbSizer812.Add( bSizer15411, 0, wx.ALL, 5 )


        sbSizer23.Add( sbSizer812, 0, wx.ALL|wx.EXPAND, 5 )

        self.cnxTabGameDetail = wx.ListCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
        sbSizer23.Add( self.cnxTabGameDetail, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer192.Add( sbSizer23, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer421.Add( bSizer192, 1, wx.EXPAND, 5 )

        bSizer451111 = wx.BoxSizer( wx.HORIZONTAL )

        self.gameTabLastTurn = wx.CheckBox( self, wx.ID_ANY, u"Dernière Donne", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer451111.Add( self.gameTabLastTurn, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer451111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.deck01 = wx.StaticBitmap( self, 101, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck01, 0, 0, 5 )

        self.deck02 = wx.StaticBitmap( self, 102, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck02, 0, 0, 5 )

        self.deck03 = wx.StaticBitmap( self, 103, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck03, 0, 0, 5 )

        self.deck04 = wx.StaticBitmap( self, 104, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck04, 0, 0, 5 )

        self.deck05 = wx.StaticBitmap( self, 105, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck05, 0, 0, 5 )

        self.deck06 = wx.StaticBitmap( self, 106, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck06, 0, 0, 5 )

        self.deck07 = wx.StaticBitmap( self, 107, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck07, 0, 0, 5 )

        self.deck08 = wx.StaticBitmap( self, 108, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck08, 0, 0, 5 )

        self.deck09 = wx.StaticBitmap( self, 109, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck09, 0, 0, 5 )

        self.deck10 = wx.StaticBitmap( self, 110, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck10, 0, 0, 5 )

        self.deck11 = wx.StaticBitmap( self, 111, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck11, 0, 0, 5 )

        self.deck12 = wx.StaticBitmap( self, 112, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck12, 0, 0, 5 )

        self.deck13 = wx.StaticBitmap( self, 113, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck13, 0, 0, 5 )

        self.deck14 = wx.StaticBitmap( self, 114, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck14, 0, 0, 5 )

        self.deck15 = wx.StaticBitmap( self, 115, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck15, 0, 0, 5 )

        self.deck16 = wx.StaticBitmap( self, 116, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck16, 0, 0, 5 )

        self.deck17 = wx.StaticBitmap( self, 117, wx.Bitmap( u"public/bigCards/C6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,180 ), 0 )
        bSizer451111.Add( self.deck17, 0, 0, 5 )

        self.deckFull = wx.StaticBitmap( self, 118, wx.Bitmap( u"public/bigCards/6_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 96,180 ), 0 )
        bSizer451111.Add( self.deckFull, 0, 0, 5 )


        bSizer451111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer421.Add( bSizer451111, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 10 )

        bSizer711 = wx.BoxSizer( wx.HORIZONTAL )

        self.gameTabChatLbl = wx.StaticText( self, wx.ID_ANY, u"Chat :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gameTabChatLbl.Wrap( -1 )

        bSizer711.Add( self.gameTabChatLbl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.gameTabChatMsg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer711.Add( self.gameTabChatMsg, 1, wx.EXPAND, 0 )


        bSizer421.Add( bSizer711, 0, wx.EXPAND, 0 )


        self.SetSizer( bSizer421 )
        self.Layout()

        # Connect Events
        self.gameTabNordSound.Bind( wx.EVT_TOGGLEBUTTON, self.onGameTabNordSound )
        self.gameTabNord2Sound.Bind( wx.EVT_TOGGLEBUTTON, self.onGameTabNord2Sound )
        self.gameTabOuestSound.Bind( wx.EVT_TOGGLEBUTTON, self.onGameTabOuestSound )
        self.gameTabChien1.Bind( wx.EVT_LEFT_DOWN, self.onChien )
        self.gameTabChien2.Bind( wx.EVT_LEFT_DOWN, self.onChien )
        self.gameTabChien3.Bind( wx.EVT_LEFT_DOWN, self.onChien )
        self.gameTabChienOk.Bind( wx.EVT_BUTTON, self.onGameTabChienOk )
        self.gameTabEstSound.Bind( wx.EVT_TOGGLEBUTTON, self.onGameTabEstSound )
        self.gameTabContratPasse.Bind( wx.EVT_BUTTON, self.onGameTabPassBtn )
        self.gameTabContratPetite.Bind( wx.EVT_BUTTON, self.onGameTabContratBtn )
        self.gameTabContratGardeSans.Bind( wx.EVT_BUTTON, self.onGameTabPassBtn )
        self.gameTabContratGardecontre.Bind( wx.EVT_BUTTON, self.onGameTabContratBtn )
        self.deck01.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck02.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck03.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck04.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck05.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck06.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck07.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck08.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck09.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck10.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck11.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck12.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck13.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck14.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck15.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck16.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deck17.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.deckFull.Bind( wx.EVT_LEFT_DOWN, self.onDeck )
        self.gameTabChatMsg.Bind( wx.EVT_TEXT_ENTER, self.onGameTabChat )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onGameTabNordSound( self, event ):
        event.Skip()

    def onGameTabNord2Sound( self, event ):
        event.Skip()

    def onGameTabOuestSound( self, event ):
        event.Skip()

    def onChien( self, event ):
        event.Skip()



    def onGameTabChienOk( self, event ):
        event.Skip()

    def onGameTabEstSound( self, event ):
        event.Skip()

    def onGameTabPassBtn( self, event ):
        event.Skip()

    def onGameTabContratBtn( self, event ):
        event.Skip()



    def onDeck( self, event ):
        event.Skip()


















    def onGameTabChat( self, event ):
        event.Skip()


