from requests import Session, Request
from loguru import logger

from utils.functions import requests_exceptions_handler


class HttpClient:

    def __init__(self, verify=False):
        self.session = Session()

        if verify is False:
            self.session.verify = False

    @logger.catch
    @requests_exceptions_handler
    def send_request(self, url, method='POST', data=None, params=None,
                     timeout=30, headers=None, cookies=None, json=None):
        req = Request(method, url=url, data=data, headers=headers, cookies=cookies, json=json, params=params)
        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped, timeout=timeout)
        return response
