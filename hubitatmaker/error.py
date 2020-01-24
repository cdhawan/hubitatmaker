from aiohttp import ClientError, ClientResponse, ClientTimeout, request


class NotReady(Exception):
    """Error when hub connection isn't ready."""


class ConnectionError(Exception):
    """Error when hub isn't responding."""


class InvalidToken(Exception):
    """Error for invalid access token."""


class InvalidConfig(Exception):
    """Error indicating invalid hub config data."""


class InvalidAttribute(Exception):
    """Error indicating an invalid device attribute."""


class InvalidInfo(Exception):
    """Error indicating that the hub returned invalid general info."""


class RequestError(Exception):
    """An error indicating that a request failed."""

    def __init__(self, resp: ClientResponse, **kwargs):
        super().__init__(f"{resp.method} {resp.url} - [{resp.status}] {resp.reason}")
