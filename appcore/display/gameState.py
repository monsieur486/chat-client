# -*- coding: utf-8 -*-


from appcore.translate import _


def gameState(state):
    if state == 0:
        msg = _("En attente de connexion à une partie")
        return msg
    if state == 1:
        msg = _("En attente de connexion de tous les joueurs")
        return msg
    if state == 2:
        msg = _("Tout les joueurs sont présents !!!")
        return msg
    if state == 3:
        msg = _("Ca joue !!!")
        return msg
