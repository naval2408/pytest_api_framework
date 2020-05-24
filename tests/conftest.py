import pytest

import configuration

from api_client.interface import Interface

"""
Defining a simple fixture that returns an Interface object,
which later can be used by the tests for calling the appropriate
get function. 
"""

@pytest.fixture(scope='module')
def api_end_point():
    _api_end_point = Interface(
        host=configuration.test_environment['host'],
        port=configuration.test_environment['port']
    )
    return _api_end_point
