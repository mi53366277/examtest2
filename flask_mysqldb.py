"""Stub for flask_mysqldb so the app boots without a real MySQL server.

Replit doesn't ship MySQL natively. This shim exposes the same surface
(`MySQL(app)` exposing `connection.cursor()`) but every cursor is a no-op
that returns empty result sets. To wire a real database, replace this
with the real `flask_mysqldb` package and provision MySQL externally.
"""


class _StubCursor:
    description = ()
    rowcount = 0
    lastrowid = 0

    def execute(self, *_args, **_kwargs):
        return 0

    def executemany(self, *_args, **_kwargs):
        return 0

    def fetchone(self):
        return None

    def fetchall(self):
        return []

    def fetchmany(self, *_args, **_kwargs):
        return []

    def close(self):
        return None

    def __iter__(self):
        return iter(())


class _StubConnection:
    def cursor(self):
        return _StubCursor()

    def commit(self):
        return None

    def rollback(self):
        return None

    def close(self):
        return None


class MySQL:
    def __init__(self, app=None):
        self.app = app
        self.connection = _StubConnection()

    def init_app(self, app):
        self.app = app
