# -*- coding: utf-8 -*-


import appSettings


from appcore.display.displayConnectedGame import displayConnectedGame
from appcore.display.mainBoardDisplay import mainBoardDisplay


def playerLogoutDisplay(self):
    appSettings.userPlay = None
    appSettings.private_game_select = None
    appSettings.game_connect_first_connexion = True
    appSettings.game_connect_denomination = '-'
    appSettings.game_connect_max_players = 5
    appSettings.game_connect_num_players = 0
    appSettings.game_connect_is_private = False
    appSettings.game_connect_is_with_chat = False
    appSettings.game_connect_is_with_relance = False
    appSettings.game_connect_is_with_annonce = False
    appSettings.game_connect_is_with_arrondi = False
    appSettings.game_connect_is_with_belge = False
    appSettings.game_connect_is_with_petite = False
    appSettings.game_connect_is_with_garde = False
    appSettings.game_connect_is_with_garde_sans = False
    appSettings.game_connect_user1_nickname = '-'
    appSettings.game_connect_user1_is_online = False
    appSettings.game_connect_user2_nickname = '-'
    appSettings.game_connect_user2_is_online = False
    appSettings.game_connect_user3_nickname = '-'
    appSettings.game_connect_user3_is_online = False
    appSettings.game_connect_user4_nickname = '-'
    appSettings.game_connect_user4_is_online = False
    appSettings.game_connect_user5_nickname = '-'
    appSettings.game_connect_user5_is_online = False
    appSettings.game_connect_state = 0
    appSettings.game_connect_is_playable = False

    displayConnectedGame(self)

    mainBoardDisplay(self)
    self.cnxTabLeave.Disable()
    self.cnxTabPrivateTitle.SetLabel('--')
    self.cnxTabSearchPwd.SetValue('')
    self.cnxTabSearchPwd.Enable()
    self.cnxTabJoinBtn.Enable()
    self.cnxTabGamesList.Enable()
