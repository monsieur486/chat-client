# -*- coding: utf-8 -*-


import appSettings

from appcore.display.mainBoardDisplay import mainBoardDisplay
from appcore.display.statsDisplay import statsDisplay
from appcore.initialization.modifyUserSettings import modifyUserSettings


def cnxOkMsg(self, userInfos):
    appSettings.userIsLoggedIn = True
    appSettings.user = userInfos['user']
    appSettings.nickName = userInfos['nickname']
    appSettings.profilePremium = userInfos['premium']
    appSettings.profilePremiumValidity = userInfos['premium_validity']
    appSettings.game4players = int(userInfos['game_4players'])
    appSettings.game5players = int(userInfos['game_5players'])
    appSettings.gameWins4Petite = int(userInfos['game_wins4_petite'])
    appSettings.gameWins4Garde = int(userInfos['game_wins4_garde'])
    appSettings.gameWins4GardeSans = int(userInfos['game_wins4_garde_sans'])
    appSettings.gameWins4GardeContre = int(userInfos['game_wins4_garde_contre'])
    appSettings.gameWins4Chelem = int(userInfos['game_wins4_chelem'])
    appSettings.gameLoose4Petite = int(userInfos['game_loose4_petite'])
    appSettings.gameLoose4Garde = int(userInfos['game_loose4_garde'])
    appSettings.gameLoose4GardeSans = int(userInfos['game_loose4_garde_sans'])
    appSettings.gameLoose4GardeContre = int(userInfos['game_loose4_garde_contre'])
    appSettings.gameLoose4Chelem = int(userInfos['game_loose4_chelem'])
    appSettings.gameWins5Petite = int(userInfos['game_wins5_petite'])
    appSettings.gameWins5Garde = int(userInfos['game_wins5_garde'])
    appSettings.gameWins5GardeSans = int(userInfos['game_wins5_garde_sans'])
    appSettings.gameWins5GardeContre = int(userInfos['game_wins5_garde_contre'])
    appSettings.gameWins5Chelem = int(userInfos['game_wins5_chelem'])
    appSettings.gameLoose5Petite = int(userInfos['game_loose5_petite'])
    appSettings.gameLoose5Garde = int(userInfos['game_loose5_garde'])
    appSettings.gameLoose5GardeSans = int(userInfos['game_loose5_garde_sans'])
    appSettings.gameLoose5GardeContre = int(userInfos['game_loose5_garde_contre'])
    appSettings.gameLoose5Chelem = int(userInfos['game_loose5_chelem'])
    modifyUserSettings('app_user', appSettings.user)
    if self.cnxTabCheckInfos:
        modifyUserSettings('app_memory_infos', '1')
        modifyUserSettings('app_password', appSettings.password)
    statsDisplay(self)
    mainBoardDisplay(self)

