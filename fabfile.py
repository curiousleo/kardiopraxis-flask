from fabric.api import local

PACKAGES = 'Flask Frozen-Flask Flask-FlatPages Flask-Assets markdown ' \
           'smartypants'
VENV = 'venv'
BUILD = 'build'

def init(venv=VENV, build=BUILD):
    local('rm -rf {}'.format(venv))
    local('virtualenv -p python2.7 --no-site-packages {}'.format(venv))
    local('{}/bin/pip install {}'.format(venv, PACKAGES))

def build(venv=VENV, build=BUILD):
    local('rm -rf {}'.format(build))
    local('{}/bin/python freeze.py'.format(venv))

def serve(build=BUILD):
    local('cd {} && python -m SimpleHTTPServer'.format(build))
