from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

#env.hosts = ['my_server']

def prepare_deploy():
#   local("./manage.py test my_app")
    local("git add .")
    local("git commit")

def pushpull():
    local('git push')

def deploy():
   code_dir = 'httpdocs/dfabric'
   with settings(warn_only=True):
       if run("test -d %s" % code_dir).failed:
          run("git clone git@github.com:eliasfernandez/dfabric.git %s" % code_dir)
   with cd(code_dir):
    	run('git pull')
#	run('touch app.wsgi')

