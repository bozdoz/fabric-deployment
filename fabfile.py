import os
from fabric import task

from connection import Connection


@task
def pwd(ctx):
  """Runs pwd for debugging purposes
  """
  _run('pwd')


@task
def ls(ctx):
  """Runs ls for debugging purposes
  """
  _run('ls')


@task
def gitpull(ctx):
  """Runs git pull
  """
  _run('git pull')


@task
def npminstall(ctx):
  """Runs npm install
  """
  _run('npm i')


@task
def npmci(ctx):
  """Runs npm ci
  """
  _run('npm ci')


@task
def npmbuild(ctx):
  """Runs npm run build
  """
  _run('npm run build')


@task
def dockercomposeup(ctx):
  """Runs docker-compose up -d
  """
  _run('docker-compose up -d')


@task
def dockercomposebuild(ctx):
  """Runs docker-compose up -d --build
  """
  _run('docker-compose up -d --build')


@task
def dockercomposerestart(ctx):
  """Runs docker-compose restart, which stops/starts containers
  """
  _run('docker-compose restart')


@task
def gulpproduction(ctx):
  """Runs gulp production
  """
  _run('gulp production')


@task
def djangostatic(ctx):
  """Runs collectstatic on a Django project
  """
  _run('./manage.py collectstatic --noinput')


@task
def apachereload(ctx):
  """Reloads Apache, assuming sudo permissions are setup
  """
  _run('sudo /etc/init.d/apache2 reload')


@task(help=dict(file="local shell script to transfer and execute"))
def runscript(ctx, file):
  """Moves a shell script to remote CWD, then executes it
  """
  # moves file to cwd
  _put(file)
  # gets relative path to remote file
  base = os.path.basename(file)
  # calls remote shell script
  _run("sh %s" % base)


@task(help=dict(local="local file", remote="remote file"))
def put(ctx, local, remote="./"):
  """Transfer files from local disk to remote server
  """
  _put(local, remote)


def _put(local, remote="./"):
  with Connection() as con:
    # `put` uses the user's home directory as reference
    # requires an absolute path
    remote_abs = os.path.abspath(os.path.join(con.cwd, remote))
    con.put(local, remote=remote_abs)


def _run(cmd):
  with Connection() as con:
    con.run(cmd)
