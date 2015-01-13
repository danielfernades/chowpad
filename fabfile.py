__author__ = 'marc'
import os
from fabric.api import run
from fabric.api import get
from fabric.api import local
from fabric.api import settings



SRC = '/home/marc/development/personal/python_apps/chowpad/'



def sync():
    """
    copy local changes in ~/personal/chef to sfgeek.net:rails_apps/rrg_chef using rsync
    :return:
    """
    cmd =  'rsync  -ah --delete  --exclude="*/tmp/*"   --exclude=".git/*"  %s marc@sfgeek.net:python_test_apps/chowpad'%(SRC)
    local(cmd)
