# -*- coding: utf-8 -*-


from appcore.translate import _


def nbGamesDisplay(self, nbGames):
    if nbGames < 2:
        self.cnxTabNbGamesLbl.SetLabel(_(" Partie : ") + str(nbGames))
    else:
        self.cnxTabNbGamesLbl.SetLabel(_(" Parties : ") + str(nbGames))
