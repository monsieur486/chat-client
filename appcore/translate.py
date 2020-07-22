# -*- coding: utf-8 -*-


from gettext import translation
import appSettings

lang = translation('base', localedir='locale', languages=[appSettings.locale])
lang.install()
_ = lang.gettext
