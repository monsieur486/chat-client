# -*- coding: utf-8 -*-
import wx

import appSettings


from appcore.display.nbFree4Display import nbFree4Display
from appcore.display.nbFree5Display import nbFree5Display
from appcore.display.nbGamesDisplay import nbGamesDisplay
from appcore.display.nbPlayersDisplay import nbPlayersDisplay
from appcore.gameMsg.userJoinGameMsg import userJoinGameMsg
from appcore.translate import _


def gameActionMsg(self, infos):
    statsInfos = infos['statsInfos']
    gameInfos = infos['gameConnectInfos']

    self.cnxTabFicheGameStart.Show(False)
    self.cnxTabPly1Change.Show(False)
    self.cnxTabPly2Change.Show(False)
    self.cnxTabPly3Change.Show(False)
    self.cnxTabPly4Change.Show(False)
    self.cnxTabPly5Change.Show(False)

    if gameInfos['user1'] == appSettings.nickName \
            or gameInfos['user2'] == appSettings.nickName \
            or gameInfos['user3'] == appSettings.nickName \
            or gameInfos['user4'] == appSettings.nickName \
            or gameInfos['user5'] == appSettings.nickName:
        userJoinGameMsg(self, gameInfos)
        self.cnxTabCreateBtn.Disable()
        if appSettings.game_connect_first_connexion:
            appSettings.game_connect_first_connexion = False
            msg = _("Connexion à la partie ") + gameInfos['denomination'] + _(" acceptée.")
            self.mainStatusBar.SetStatusText(msg, 0)
        self.cnxTabGamesList.Disable()
        self.cnxTabPlay4.Disable()
        self.cnxTabPlay5.Disable()
        self.cnxTabJoinBtn.Disable()
        self.cnxTabSearchPwd.Disable()
        self.cnxTabCaptainLed.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_red.png", wx.BITMAP_TYPE_ANY))
        if appSettings.user == gameInfos['captain']:
            self.cnxTabCaptainLed.SetBitmap(wx.Bitmap(u"public/icons/16x16_led_green.png", wx.BITMAP_TYPE_ANY))
            self.cnxTabFicheGameStart.Show(True)
            self.cnxTabFicheGameStart.Disable()
            if gameInfos['isPlayable']:
                self.cnxTabFicheGameStart.Enable()
            if not appSettings.game_connect_user1_is_online and appSettings.game_connect_user1_nickname != "--":
                self.cnxTabPly1Change.Show(True)
            if not appSettings.game_connect_user2_is_online and appSettings.game_connect_user2_nickname != "--":
                self.cnxTabPly2Change.Show(True)
            if not appSettings.game_connect_user3_is_online and appSettings.game_connect_user3_nickname != "--":
                self.cnxTabPly3Change.Show(True)
            if not appSettings.game_connect_user4_is_online and appSettings.game_connect_user4_nickname != "--":
                self.cnxTabPly4Change.Show(True)
            if not appSettings.game_connect_user5_is_online and appSettings.game_connect_user5_nickname != "--":
                self.cnxTabPly5Change.Show(True)

    nbPlayersDisplay(self, statsInfos['nbPlayers'])
    nbGamesDisplay(self, statsInfos['nbGames'])
    nbFree4Display(self, statsInfos['free4'])
    nbFree5Display(self, statsInfos['free5'])

    self.cnxTabGamesList.DeleteAllItems()
    idx = 0
    self.cnxTabJoinBtn.Enable()
    if appSettings.userPlay:
        self.cnxTabJoinBtn.Disable()
    for game in statsInfos['privatesGames']:
        index = self.cnxTabGamesList.InsertItem(idx, game[0])
        self.cnxTabGamesList.SetItem(index, 1, str(game[1]))
        self.cnxTabGamesList.SetItem(index, 2, game[2])
        idx += 1
    if not idx:
        self.cnxTabJoinBtn.Disable()
    self.Layout()
