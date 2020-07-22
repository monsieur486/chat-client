# -*- coding: utf-8 -*-


import configparser
import appSettings
from controller import PublicPath


def retrievingSettings():
    config = configparser.ConfigParser()
    settingsFile = PublicPath('settings', 'luncher.cfg')
    config.read(settingsFile)

    appSettings.locale = config['LUNCHER']['app_locale']
    appSettings.user = config['LUNCHER']['app_user']
    appSettings.password = config['LUNCHER']['app_password']
    appSettings.memoryInfos = config.getboolean('LUNCHER', 'app_memory_infos')
    mainVersion = config['LUNCHER']['app_main_version']
    subVersion = config['LUNCHER']['app_sub_version']
    branchVersion = config['LUNCHER']['app_branch_version']
    appSettings.appVersion = mainVersion + '.' + subVersion + '.' + branchVersion


def baseVariables():
    from gettext import translation

    lang = translation('base', localedir='locale', languages=[appSettings.locale])
    lang.install()
    _ = lang.gettext

    appSettings.appNickName = _("non inscrit")


def initialization():
    retrievingSettings()
    baseVariables()
