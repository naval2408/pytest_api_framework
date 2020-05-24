import requests
import urllib.parse

"""
This class defines the method to create a get request 
with different parameters from a base url.
Also, as I am testing only get APIs in this project,
have skipped the addition for POST, PUT and DELETE functions.
"""


class Connection:

    def __init__(self, base_url):
        self._base_url = base_url

    def do_get(self, path, params=None, **kwargs):
        return requests.get(
            url=urllib.parse.urljoin(self._base_url, path),
            params=params,
            **kwargs
        )
