#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    function that packs the contents of web_Static to tgz archive
    """
    tym = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        archive_file = "versions/web_static_{}.tgz".format(tym)
        local("tar -cvzf {} web_static/".format(archive_file))
        return archive_file
    except Exception:
        return None
