import functools
from requests import exceptions


def get_common_headers():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    return headers


def requests_exceptions_handler(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exceptions.HTTPError:
            raise
        except exceptions.ProxyError:
            raise
        except exceptions.SSLError:
            raise
        except exceptions.ConnectTimeout:
            raise
        except exceptions.ConnectionError:
            raise
        except exceptions.ReadTimeout:
            raise
        except exceptions.Timeout:
            raise
        except exceptions.URLRequired:
            raise
        except exceptions.TooManyRedirects:
            raise
        except exceptions.MissingSchema:
            raise
        except exceptions.InvalidSchema:
            raise
        except exceptions.InvalidProxyURL:
            raise
        except exceptions.InvalidURL:
            raise
        except exceptions.InvalidHeader:
            raise
        except exceptions.ChunkedEncodingError:
            raise
        except exceptions.ContentDecodingError:
            raise
        except exceptions.StreamConsumedError:
            raise
        except exceptions.RetryError:
            raise
        except exceptions.UnrewindableBodyError:
            raise
        except exceptions.FileModeWarning:
            raise
        except exceptions.RequestsDependencyWarning:
            raise
        except exceptions.RequestsWarning:
            raise

    return inner_func
