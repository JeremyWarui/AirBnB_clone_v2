#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from os.path import isfile
env.hosts = ['54.236.56.164', '54.90.17.105']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    function that deploys our archive to webservers
    """
    if not isfile(archive_path):
        return False
    try:
        zip_file = archive_path.split("/")[1]
        unzip_file = zip_file.split(".")[0]
        unzipfile_path = "/data/web_static/releases/{}".format(unzip_file)
        sym_link = "/data/web_static/current"

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(unzipfile_path))
        """ uncompress the zipfile and place it in webstatic releases"""
        run("tar -xvf /tmp/{} -C {}".format(zip_file, unzipfile_path))
        """ delete the zip files"""
        run("rm /tmp/{}".format(zip_file))
        run("mv {}web_static/* {}".format(unzipfile_path, unzipfile_path))
        run("rm -rf {}web_static".format(unzipfile_path))
        """ delete symbiotic link """
        run("rm -rf {}".format(sym_link))
        """ create new link """
        run("ln -sf {} {}".format(unzipfile_path, sym_link))
        print("New version deployed!")
        return True
    except Exception:
        return False
