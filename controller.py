# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))
publicDir = os.path.join(base, "public")


def PublicPath(folderInPublic, fileName):
    result = os.path.join(publicDir, folderInPublic, fileName)
    return result
