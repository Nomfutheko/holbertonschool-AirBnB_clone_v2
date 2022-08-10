#!/usr/bin/python3
"""Script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime as dt
from fabric.api import local


def do_pack():
    """File compressor"""
    try:
        timestamp = dt.now().strftime("%Y%m%d%H%M%S")
        filepath = "./versions/web_static_{}".format(timestamp)
        local('mkdir -p ./versions')
        file = local('tar -cvzf {}.tgz web_static'.format(filepath))
        return file
    except:
        return None
