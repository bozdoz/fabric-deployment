import os
import fabric


class Connection:
    def __init__(self):
        self.con = connect()

    def __enter__(self):
        CWD = os.getenv("FAB_CWD", os.getenv("CWD", "."))
        self.con.command_cwds = [CWD]
        return self.con

    def __exit__(self, a, b, c):
        self.con.close()


def connect():
    connect_kwargs = dict()
    password = os.getenv("FAB_PASSWORD", os.getenv("PASSWORD"))
    key_filename = os.getenv("FAB_SSH_KEY", os.getenv("SSH_KEY"))

    if password:
        connect_kwargs["password"] = password

    if key_filename:
        connect_kwargs["key_filename"] = key_filename

    return fabric.Connection(
        host=os.getenv("FAB_HOST") or os.environ["HOST"],
        user=os.getenv("FAB_USER") or os.environ["USER"],
        connect_kwargs=connect_kwargs,
        port=os.getenv("FAB_PORT", os.getenv("PORT", 22)),
    )
