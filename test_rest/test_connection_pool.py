import unittest

from massive import RESTClient


class ConnectionPoolTest(unittest.TestCase):
    def test_maxsize_defaults_to_ten(self):
        client = RESTClient(api_key="test")

        assert client.client.connection_pool_kw["maxsize"] == 10

    def test_maxsize_is_configurable(self):
        client = RESTClient(api_key="test", maxsize=64)

        assert client.client.connection_pool_kw["maxsize"] == 64

    def test_maxsize_is_independent_of_num_pools(self):
        # num_pools caps the number of distinct HOST pools, which does not help a client
        # that talks to one host from many threads -- that is what maxsize controls.
        client = RESTClient(api_key="test", num_pools=50, maxsize=32)

        assert client.client.connection_pool_kw["maxsize"] == 32
