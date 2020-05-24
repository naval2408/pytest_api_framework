from .connection import Connection

"""
This is a wrapper class, which is composed over
Connections class. We will use it as base class 
while defining the various functions for different
get requests.
"""


class BaseUrl:

    def __init__(self, connection: Connection):
        self._connection = connection
