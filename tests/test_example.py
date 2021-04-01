import pytest
from core.base_test import BaseCase
from core.my_request import Request
from core.asserts import Asserts


class TestExample(BaseCase):
    def test_example(self):
        response = Request.get('')
        Asserts.assert_code_status(response, 200)
        Asserts.assert_time_is_less_than(response, 1)

