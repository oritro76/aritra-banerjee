from loguru import logger

from clients.http_client import HttpClient
from conf.conf import best_buy_base_path
from utils.functions import get_common_headers


class ApiPlaygroundClient:
    def __init__(self):
        self.base_url = best_buy_base_path
        self.http_client = HttpClient()

    def create_product(self, product):
        url = self.base_url + 'products'
        headers = get_common_headers()
        body = product

        logger.info(f'request.method -> POST '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def fetch_products(self, params=None, prd_id=None):
        if prd_id is None:
            url = self.base_url + 'products'
        else:
            url = self.base_url + 'products' + f'/{prd_id}'

        headers = get_common_headers()

        logger.info(f'request.method -> GET '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.params -> {params}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="GET",
                                                 params=params)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def delete_product(self, prd_id):
        url = self.base_url + 'products' + f'/{prd_id}'
        headers = get_common_headers()

        logger.info(f'request.method -> DELETE '
                    f'request.url -> {url} '
                    f'request.headers -> {headers}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="DELETE")

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def edit_product(self, prd_id, product):
        url = self.base_url + 'products' + f'/{prd_id}'
        headers = get_common_headers()
        body = product

        logger.info(f'request.method -> PATCH '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, method="PATCH", headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def create_store(self, store):
        url = self.base_url + 'stores'
        headers = get_common_headers()
        body = store

        logger.info(f'request.method -> POST '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def fetch_stores(self, params=None, str_id=None):
        if str_id is None:
            url = self.base_url + 'stores'
        else:
            url = self.base_url + 'stores' + f'/{str_id}'

        headers = get_common_headers()

        logger.info(f'request.method -> GET '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.params -> {params}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="GET",
                                                 params=params)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def delete_store(self, str_id):
        url = self.base_url + 'stores' + f'/{str_id}'
        headers = get_common_headers()

        logger.info(f'request.method -> DELETE '
                    f'request.url -> {url} '
                    f'request.headers -> {headers}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="DELETE")

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def edit_store(self, str_id, store):
        url = self.base_url + 'stores' + f'/{str_id}'
        headers = get_common_headers()
        body = store

        logger.info(f'request.method -> PATCH'
                    f' request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, method="PATCH", headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def create_service(self, service):
        url = self.base_url + 'services'
        headers = get_common_headers()
        body = service

        logger.info(f'request.method -> POST '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def fetch_services(self, params=None, srv_id=None):
        if srv_id is None:
            url = self.base_url + 'services'
        else:
            url = self.base_url + 'services' + f'/{srv_id}'

        headers = get_common_headers()

        logger.info(f'request.method -> GET '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.params -> {params}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="GET",
                                                 params=params)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def delete_service(self, srv_id):
        url = self.base_url + 'services' + f'/{srv_id}'
        headers = get_common_headers()

        logger.info(f'request.method -> DELETE '
                    f'request.url -> {url} '
                    f'request.headers -> {headers}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="DELETE")

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def edit_service(self, srv_id, service):
        url = self.base_url + 'services' + f'/{srv_id}'
        headers = get_common_headers()

        body = service

        logger.info(f'request.method -> PATCH '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, method="PATCH", headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def create_category(self, category):
        url = self.base_url + 'categories'
        headers = get_common_headers()
        body = category

        logger.info(f'request.method -> POST '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def fetch_categories(self, params=None, cat_id=None):
        if cat_id is None:
            url = self.base_url + 'categories'
        else:
            url = self.base_url + 'categories' + f'/{cat_id}'
        headers = get_common_headers()

        logger.info(f'request.method -> GET '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.params -> {params}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="GET",
                                                 params=params)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def delete_category(self, cat_id):
        url = self.base_url + 'categories' + f'/{cat_id}'
        headers = get_common_headers()

        logger.info(f'request.method -> DELETE '
                    f'request.url -> {url} '
                    f'request.headers -> {headers}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="DELETE")

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def edit_category(self, cat_id, category):
        url = self.base_url + 'categories' + f'/{cat_id}'
        headers = get_common_headers()
        body = category

        logger.info(f'request.method -> PATCH '
                    f'request.url -> {url} '
                    f'request.headers -> {headers} '
                    f'request.body -> {body}')

        response = self.http_client.send_request(url=url, method="PATCH", headers=headers, json=body)

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def health_check(self):
        url = self.base_url + 'healthcheck'
        headers = get_common_headers()

        logger.info(f'request.method -> GET '
                    f'request.url -> {url} '
                    f'request.headers -> {headers}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="GET")

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}

    def fetch_api_version(self):
        url = self.base_url + 'version'
        headers = get_common_headers()

        logger.info(f'request.method -> GET '
                    f'request.url -> {url} '
                    f'request.headers -> {headers}')

        response = self.http_client.send_request(url=url,
                                                 headers=headers,
                                                 method="GET")

        logger.info(f'response.status_code -> {response.status_code} '
                    f'response.headers -> {response.headers} '
                    f'response.body -> {response.json()}')

        return {"status_code": response.status_code, "json": response.json()}
