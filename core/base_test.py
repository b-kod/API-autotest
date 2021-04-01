from datetime import datetime
from requests import Response
from core.logger import Logger


class BaseCase:
    def setup(self):
        pass

    def teardown(self):
        Logger.get_instance().write_log_to_file()

    @staticmethod
    def get_cookie(response: Response, cookie_name):
        if cookie_name in response.cookies:
            return {cookie_name: response.cookies[cookie_name]}
        else:
            raise Exception(f"Cannot find cookie with the name {cookie_name} in the last response")

    @staticmethod
    def get_header(response: Response, headers_name):
        if headers_name in response.headers:
            return {headers_name: response.headers[headers_name]}
        else:
            raise Exception(f"Cannot find header with the name {headers_name} in the last response")

    @staticmethod
    def create_unique_email(base: str, domain="example.com"):
        return f'{base}+{datetime.now().strftime("%m%d%Y%H%M%S")}@{domain}'
