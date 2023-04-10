#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import *
from os.path import isfile
from datetime import datetime
env.hosts = ['54.236.56.164', '54.90.17.105']
env.user = 'ubuntu'


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

def do_deploy(archive_path):
    """
    function that deploys our archive to webservers
    """
    if not isfile(archive_path):
        return False
    try:
        zip_file = archive_path.split("/")[1]
        unzip_file = zip_file.split(".")[0]
        unzipfile_path = "/data/web_static/releases/{}/".format(unzip_file)
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

def deploy():
    """ function that finally deploys """
    zip_file_path = do_pack()
    if zip_file_path is None:
        return False
    return do_deploy(zip_file_path)
