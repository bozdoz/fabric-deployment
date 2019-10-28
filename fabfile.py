import os

from fabric import Connection
from fabric import task


@task
def gitpull(ctx):
  run('git pull')


@task
def npmbuild(ctx):
  run('npm i', 'npm run build')


@task
def dockercomposeup(ctx):
  run('docker-compose up -d')

  
@task
def dockercomposebuild(ctx):
  run('docker-compose up -d --build')


@task
def dockercomposerestart(ctx):
  run('docker-compose restart')


@task
def gulpproduction(ctx):
  run('gulp production')


@task
def djangostatic(ctx):
  run('./manage.py collectstatic --noinput')


@task
def apachereload(ctx):
  run('sudo /etc/init.d/apache2 reload')


def run(*cmds):
  with connect() as con:
    cwd = os.getenv('CWD')
    with con.cd(cwd):
      for cmd in cmds:
        con.run(cmd)


def connect():
  return Connection(
    host=os.getenv('HOST'), 
    user=os.getenv('USER'),
    connect_kwargs=dict(
      password=os.getenv('PASSWORD')
    ),
    port=os.getenv('PORT', 22)
  )
