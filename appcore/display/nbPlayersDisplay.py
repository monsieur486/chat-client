# -*- coding: utf-8 -*-


from appcore.translate import _


def nbPlayersDisplay(self, nbPlayers):
    if nbPlayers < 2:
        self.cnxTabNbPlayersLbl.SetLabel(_("Joueur connecté : ") + str(nbPlayers))
    else:
        self.cnxTabNbPlayersLbl.SetLabel(_("Joueurs connectés : ") + str(nbPlayers))
