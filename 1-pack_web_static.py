#!/bin/usr/python3
"""Generates the .tgz archive of the web_static folder"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def  do_pack():
    """Generates a .tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        f_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(f_name))
        return f_name
    except:
        return None