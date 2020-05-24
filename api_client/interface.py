from .connection import Connection
from .todos import ToDos

"""
This is an interfacing class through which we will expose
the functionaries of api_client to tests module.   
"""


class Interface:

    def __init__(self, host, port):
        self._schema = 'http'
        self.base_url = f'{self._schema}://{host}:{port}'
        self._connection = Connection(base_url=self.base_url)

    @property
    def todos(self):
        return ToDos(self._connection)
