# -*- coding: utf-8 -*-


import appSettings
from appcore.display.displayConnectedGame import displayConnectedGame


def userJoinGameMsg(self, gameInfos):
    appSettings.userPlay = gameInfos['gameId']
    appSettings.game_connect_denomination = gameInfos['denomination']
    appSettings.game_connect_is_private = gameInfos['private']
    appSettings.game_connect_num_players = gameInfos['nbPlayers']
    appSettings.game_connect_max_players = gameInfos['maxPlayers']
    appSettings.game_connect_is_with_chat = gameInfos['isWithChat']
    appSettings.game_connect_is_with_relance = gameInfos['isWithRelance']
    appSettings.game_connect_is_with_annonce = gameInfos['isWithAnnonce']
    appSettings.game_connect_is_with_arrondi = gameInfos['isWithRound']
    appSettings.game_connect_is_with_belge = gameInfos['isWithBelge']
    appSettings.game_connect_is_with_petite = gameInfos['isWithPetite']
    appSettings.game_connect_is_with_garde = gameInfos['isWithGarde']
    appSettings.game_connect_is_with_garde_sans = gameInfos['isWithGardeSans']
    appSettings.game_connect_is_playable = gameInfos['isPlayable']
    appSettings.game_connect_state = gameInfos['state']
    appSettings.game_connect_user1_nickname = gameInfos['user1']
    appSettings.game_connect_user1_is_online = gameInfos['user1onLine']
    appSettings.game_connect_user2_nickname = gameInfos['user2']
    appSettings.game_connect_user2_is_online = gameInfos['user2onLine']
    appSettings.game_connect_user3_nickname = gameInfos['user3']
    appSettings.game_connect_user3_is_online = gameInfos['user3onLine']
    appSettings.game_connect_user4_nickname = gameInfos['user4']
    appSettings.game_connect_user4_is_online = gameInfos['user4onLine']
    appSettings.game_connect_user5_nickname = gameInfos['user5']
    appSettings.game_connect_user5_is_online = gameInfos['user5onLine']

    displayConnectedGame(self)
