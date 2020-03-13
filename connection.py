import os
import fabric

CWD = os.environ['CWD']


class Connection:
  def __init__(self):
    self.con = connect()

  def __enter__(self):
    self.con.command_cwds = [CWD]
    return self.con

  def __exit__(self, a, b, c):
    self.con.close()


def connect():
  return fabric.Connection(
      host=os.environ['HOST'],
      user=os.environ['USER'],
      connect_kwargs=dict(
          password=os.getenv('PASSWORD'),
          key_filename=os.getenv('SSH_KEY')
      ),
      port=os.getenv('PORT', 22)
  )
