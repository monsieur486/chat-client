# -*- coding: utf-8 -*-


import appSettings


def statsDisplay(self):
    gameTotal = appSettings.game4players + appSettings.game5players
    self.statsGames.SetLabel(str(gameTotal))
    self.statsGames4.SetLabel(str(appSettings.game4players))
    self.statsGames5.SetLabel(str(appSettings.game5players))
    winPetiteTotal = appSettings.gameWins4Petite + appSettings.gameWins5Petite
    winGardeTotal = appSettings.gameWins4Garde + appSettings.gameWins5Garde
    winGardeSansTotal = appSettings.gameWins4GardeSans + appSettings.gameWins5GardeSans
    winGardeContreTotal = appSettings.gameWins4GardeContre + appSettings.gameWins5GardeContre
    winChelemTotal = appSettings.gameWins4Chelem + appSettings.gameWins5Chelem
    loosePetiteTotal = appSettings.gameLoose4Petite + appSettings.gameLoose5Petite
    looseGardeTotal = appSettings.gameLoose4Garde + appSettings.gameLoose5Garde
    looseGardeSansTotal = appSettings.gameLoose4GardeSans + appSettings.gameLoose5GardeSans
    looseGardeContreTotal = appSettings.gameLoose4GardeContre + appSettings.gameLoose5GardeContre
    looseChelemTotal = appSettings.gameLoose4Chelem + appSettings.gameLoose5Chelem

    self.winPetites.SetLabel(str(winPetiteTotal))
    self.winGardes.SetLabel(str(winGardeTotal))
    self.winGardesSans.SetLabel(str(winGardeSansTotal))
    self.winGardesContre.SetLabel(str(winGardeContreTotal))
    self.winChelems.SetLabel(str(winChelemTotal))

    self.loosePetites.SetLabel(str(loosePetiteTotal))
    self.looseGardes.SetLabel(str(looseGardeTotal))
    self.looseGardesSans.SetLabel(str(looseGardeSansTotal))
    self.looseGardesContre.SetLabel(str(looseGardeContreTotal))
    self.looseChelems.SetLabel(str(looseChelemTotal))

    self.winPetites4.SetLabel(str(appSettings.gameWins4Petite))
    self.winPetites5.SetLabel(str(appSettings.gameWins5Petite))
    self.loosePetites4.SetLabel(str(appSettings.gameLoose4Petite))
    self.loosePetites5.SetLabel(str(appSettings.gameLoose5Petite))

    self.winGardes4.SetLabel(str(appSettings.gameWins4Garde))
    self.winGardes5.SetLabel(str(appSettings.gameWins5Garde))
    self.looseGardes4.SetLabel(str(appSettings.gameLoose4Garde))
    self.looseGardes5.SetLabel(str(appSettings.gameLoose5Garde))

    self.winGardesSans4.SetLabel(str(appSettings.gameWins4GardeSans))
    self.winGardesSans5.SetLabel(str(appSettings.gameWins5GardeSans))
    self.looseGardesSans4.SetLabel(str(appSettings.gameLoose4GardeSans))
    self.looseGardesSans5.SetLabel(str(appSettings.gameLoose5GardeSans))

    self.winGardesContre4.SetLabel(str(appSettings.gameWins4GardeContre))
    self.winGardesContre5.SetLabel(str(appSettings.gameWins5GardeContre))
    self.looseGardesContre4.SetLabel(str(appSettings.gameLoose4GardeContre))
    self.looseGardesContre5.SetLabel(str(appSettings.gameLoose5GardeContre))

    self.winChelems4.SetLabel(str(appSettings.gameWins4Chelem))
    self.winChelems5.SetLabel(str(appSettings.gameWins5Chelem))
    self.looseChelems4.SetLabel(str(appSettings.gameLoose4Chelem))
    self.looseChelems5.SetLabel(str(appSettings.gameLoose5Chelem))
