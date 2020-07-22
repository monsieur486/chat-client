# -*- coding: utf-8 -*-


from appcore.display.nbFree4Display import nbFree4Display
from appcore.display.nbFree5Display import nbFree5Display
from appcore.display.nbGamesDisplay import nbGamesDisplay
from appcore.display.nbPlayersDisplay import nbPlayersDisplay


def updateStatsInfosMsg(self, statsInfos):
    nbPlayersDisplay(self, statsInfos['nbPlayers'])
    nbGamesDisplay(self, statsInfos['nbGames'])
    nbFree4Display(self, statsInfos['free4'])
    nbFree5Display(self, statsInfos['free5'])

    self.cnxTabGamesList.DeleteAllItems()
    idx = 0
    for game in statsInfos['privatesGames']:
        index = self.cnxTabGamesList.InsertItem(idx, game[0])
        self.cnxTabGamesList.SetItem(index, 1, str(game[1]))
        self.cnxTabGamesList.SetItem(index, 2, game[2])
        idx += 1

    self.Layout()
