# -*- coding: utf-8 -*-


from controller import PublicPath


def modifyUserSettings(key, value):
    from configparser import ConfigParser
    config = ConfigParser()
    settingsFile = PublicPath('settings', 'luncher.cfg')
    config.read(settingsFile)
    config.set('LUNCHER', key, value)

    with open(settingsFile, 'w') as configfile:
        config.write(configfile)
