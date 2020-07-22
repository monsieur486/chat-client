# -*- coding: utf-8 -*-
import wx

import appSettings
from appcore.translate import _
from templates.Game4 import Game4
from templates.Game5 import Game5


def boussole(maxPlayer, position, antiHoraire, userPos, playState):
    if maxPlayer == 4:
        if antiHoraire:
            position += 3
            cycle = (3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0)
        else:
            cycle = (0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3)
    else:
        if antiHoraire:
            position += 4
            cycle = (4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0)
        else:
            cycle = (0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4)

    returnList = []

    init = position

    for f in range(maxPlayer):
        playerPos = init + 1
        returnList.append(cycle[playerPos] + 1)
        init = playerPos

    player = returnList[userPos - 1]

    if player == 1:
        return playState['tablePlayer1']

    if player == 2:
        return playState['tablePlayer2']

    if player == 3:
        return playState['tablePlayer3']

    if player == 4:
        return playState['tablePlayer4']

    if player == 5:
        return playState['tablePlayer5']


def playActionSelectContractMsg(self, playState):
    maxPlayers = appSettings.game_connect_max_players
    if maxPlayers == 5:
        self.gameTab = Game5(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
    else:
        self.gameTab = Game4(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

    self.m_notebook1.AddPage(self.gameTab, _(u"Partie"), False)
    self.m_notebook1.SetSelection(2)
    self.Layout()

    if playState['state'] == 3:
        self.cnxTabFicheGameState.SetLabel(_('Ca joue !!!'))

    msg = _('En attente de prise ou passe du joueur : ') + playState['nextPlayerNickname']

    self.gameTab.gameTabCroupier.SetLabel(msg)
    # playState['donnes']
    self.gameTab.gameTabGameDonne.SetLabel(str(playState['donne']))
    self.gameTab.gameTabGameTour.SetLabel(str(playState['turn']))
    # playState['dealerNickname']
    contract = str(playState['contract'])
    if contract == 0:
        msg = '--'
    if contract == 1:
        msg = _('Petite')
    if contract == 2:
        msg = _('Garde')
    if contract == 3:
        msg = _('Garde Sans')
    if contract == 4:
        msg = _('Garde Contre')
    if playState['withChelem']:
        msg += ' Chelem annoncé'
    self.gameTab.gameTabGameContrat.SetLabel(msg)

    if maxPlayers == 5:
        card = playState['cardCall']
        if not card:
            msg = '--'
        else:
            msg = str(playState['cardCall'])
        self.gameTab.gameTabGameAppel.SetLabel(msg)

    color = playState['color']
    if not color:
        msg = '--'
    if color == 1:
        msg = _('Pique')
    if color == 2:
        msg = _('Coeur')
    if color == 3:
        msg = _('Trèfle')
    if color == 4:
        msg = _('Carreau')
    if color == 5:
        msg = _('Atout')

    self.gameTab.cnxTabFichePos1Nickname.SetLabel(playState['tablePlayer1']['nickname'])
    self.gameTab.cnxTabFichePos1Score.SetLabel(str(playState['tablePlayer1']['score']))

    self.gameTab.cnxTabFichePos2Nickname.SetLabel(playState['tablePlayer2']['nickname'])
    self.gameTab.cnxTabFichePos2Score.SetLabel(str(playState['tablePlayer2']['score']))

    self.gameTab.cnxTabFichePos3Nickname.SetLabel(playState['tablePlayer3']['nickname'])
    self.gameTab.cnxTabFichePos3Score.SetLabel(str(playState['tablePlayer3']['score']))

    self.gameTab.cnxTabFichePos4Nickname.SetLabel(playState['tablePlayer4']['nickname'])
    self.gameTab.cnxTabFichePos4Score.SetLabel(str(playState['tablePlayer4']['score']))

    if maxPlayers == 5:
        self.gameTab.cnxTabFichePos5Nickname.SetLabel(playState['tablePlayer5']['nickname'])
        self.gameTab.cnxTabFichePos5Score.SetLabel(str(playState['tablePlayer5']['score']))

    if maxPlayers == 4:
        positionPlayer = playState['positionPlayer']

        player1 = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 1, playState)
        player2 = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 2, playState)
        player3 = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 3, playState)
        player = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 4, playState)
        self.gameTab.gameTabUser.SetLabel(player['nickname'])
        self.gameTab.gameTabOuest.SetLabel(player1['nickname'])
        self.gameTab.gameTabNord.SetLabel(player2['nickname'])
        self.gameTab.gameTabEst.SetLabel(player3['nickname'])

    else:
        positionPlayer = playState['positionPlayer']

        player1 = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 1, playState)
        player2 = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 2, playState)
        player3 = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 3, playState)
        player4 = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 4, playState)
        player = boussole(maxPlayers, positionPlayer, appSettings.antiHoraire, 5, playState)
        self.gameTab.gameTabUser.SetLabel(player['nickname'])
        self.gameTab.gameTabOuest.SetLabel(player1['nickname'])
        self.gameTab.gameTabNord.SetLabel(player2['nickname'])
        self.gameTab.gameTabNord2.SetLabel(player3['nickname'])
        self.gameTab.gameTabEst.SetLabel(player4['nickname'])

    self.Layout()






    #    = playState['tablePlayer1']['selectCard']
    #   = playState['tablePlayer1']['nextAction']
    #  = playState['tablePlayer1']['isPreneur']
    #    = playState['tablePlayer1']['viewCall']
    # = playState['tablePlayer1']['isOnline']

    # playState['centralCards']
    # playState['centralCardsType']
    #print(playState['playerDeck'])
