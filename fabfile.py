from fabric.api import local

PACKAGES = 'Flask Frozen-Flask Flask-FlatPages Flask-Assets markdown ' \
           'smartypants'

def init(venv='venv'):
    local('rm -rf {}'.format(venv))
    local('virtualenv -p python2.7 --no-site-packages {}'.format(venv))
    local('{}/bin/pip install {}'.format(venv, PACKAGES))

def build(venv='venv'):
    local('rm -rf {}'.format('build'))
    local('{}/bin/python freeze.py'.format(venv))
