import requests
from core.logger import Logger
from environment import ENV


class Request:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies: dict = None):
        return Request._send(url, data, headers, json, cookies, 'POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies: dict = None):
        return Request._send(url, data, headers, json, cookies, 'GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies: dict = None):
        return Request._send(url, data, headers, json, cookies, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies: dict = None):
        return Request._send(url, data, headers, json, cookies, 'DELETE')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, json: dict, cookies: dict, method: str):
        url = f"{ENV.base_url()}{url}"

        if headers is None:
            headers = {}

        if cookies is None:
            cookies = {}

        additional_header = {
            'X-THIS_IS_TEST': 'True'
        }
        headers.update(additional_header)

        Logger.get_instance().add_request(url, data, headers, json, cookies, method)

        if method == 'GET':
            response = requests.get(url, data=data, headers=headers, json=json, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, json=json, cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, json=json, cookies=cookies)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, json=json, cookies=cookies)
        else:
            raise Exception(f'Bad HTTP method "{method}" was received')

        Logger.get_instance().add_response(response)
        return response
