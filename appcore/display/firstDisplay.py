# -*- coding: utf-8 -*-


import appSettings


def firstDisplay(self):
    self.mailBox.Hide()
    self.cnxTabPlay4.Disable()
    self.cnxTabPlay5.Disable()
    self.cnxTabJoinBtn.Disable()
    self.cnxTabLeave.Disable()
    self.cnxTabCreateBtn.Disable()
    self.cnxTabOptionsSA.Disable()
    self.cnxTabOptionsAR.Disable()
    self.cnxTabOptionsSC.Disable()
    self.cnxTabOptionsArrondi.Disable()
    self.cnxTabOptionsAB.Disable()
    self.cnxTabOptionsPetie.Disable()
    self.cnxTabOptionsGarde.Disable()
    self.cnxTabOptionsGardeSans.Disable()
    self.cnxTabCreatePassword.Disable()
    self.m_staticText110.Disable()
    self.cnxTabPly1Change.Show(False)
    self.cnxTabPly2Change.Show(False)
    self.cnxTabPly3Change.Show(False)
    self.cnxTabPly4Change.Show(False)
    self.cnxTabPly5Change.Show(False)
    self.cnxTabFicheGameStart.Show(False)
    self.cnxTabUserEntry.SetValue(appSettings.user)

    if appSettings.memoryInfos:
        self.cnxTabPasswordEntry.SetValue(appSettings.password)
        self.cnxTabCheckInfos.SetValue(True)

    self.Layout()
