# -*- coding: utf-8 -*-


import wx
import appSettings


from appcore.display.gameState import gameState
from appcore.translate import _


def displayConnectedGame(self):
    self.cnxTabCreateDenomination.SetValue(appSettings.game_connect_denomination)

    if appSettings.game_connect_max_players == 5:
        self.cnxTabFicheGameInfos.SetLabel(str(appSettings.game_connect_num_players) + '/5')
    else:
        self.cnxTabFicheGameInfos.SetLabel(str(appSettings.game_connect_num_players) + '/4')

    self.cnxTabFichePly1Nickname.SetLabel(appSettings.game_connect_user1_nickname)
    if appSettings.game_connect_user1_is_online:
        self.cnxTabFichePly1Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
    else:
        self.cnxTabFichePly1Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

    self.cnxTabFichePly2Nickname.SetLabel(appSettings.game_connect_user2_nickname)
    if appSettings.game_connect_user2_is_online:
        self.cnxTabFichePly2Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
    else:
        self.cnxTabFichePly2Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

    self.cnxTabFichePly3Nickname.SetLabel(appSettings.game_connect_user3_nickname)
    if appSettings.game_connect_user3_is_online:
        self.cnxTabFichePly3Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
    else:
        self.cnxTabFichePly3Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

    self.cnxTabFichePly4Nickname.SetLabel(appSettings.game_connect_user4_nickname)
    if appSettings.game_connect_user4_is_online:
        self.cnxTabFichePly4Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
    else:
        self.cnxTabFichePly4Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

    self.cnxTabFichePly5Nickname.SetLabel(appSettings.game_connect_user5_nickname)
    if appSettings.game_connect_user5_is_online:
        self.cnxTabFichePly5Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
    else:
        self.cnxTabFichePly5Led.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))

    if appSettings.userPlay:
        self.cnxTabLeave.Enable()
        self.cnxTabOptionsSA.SetValue(appSettings.game_connect_is_with_annonce)
        self.cnxTabOptionsSA.Disable()

        self.cnxTabOptionsAR.SetValue(appSettings.game_connect_is_with_relance)
        self.cnxTabOptionsAR.Disable()

        self.cnxTabOptionsSC.SetValue(appSettings.game_connect_is_with_chat)
        self.cnxTabOptionsSC.Disable()

        self.cnxTabOptionsArrondi.SetValue(appSettings.game_connect_is_with_arrondi)
        self.cnxTabOptionsArrondi.Disable()

        self.cnxTabOptionsAB.SetValue(appSettings.game_connect_is_with_belge)
        self.cnxTabOptionsAB.Disable()

        self.cnxTabOptionsPetie.SetValue(appSettings.game_connect_is_with_petite)
        self.cnxTabOptionsPetie.Disable()

        self.cnxTabOptionsGarde.SetValue(appSettings.game_connect_is_with_garde)
        self.cnxTabOptionsGarde.Disable()

        self.cnxTabOptionsGardeSans.SetValue(appSettings.game_connect_is_with_garde_sans)
        self.cnxTabOptionsGardeSans.Disable()
