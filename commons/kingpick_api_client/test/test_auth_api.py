# coding: utf-8

"""
    Kingpick Admin API

    Provides APIs for tenant maintenance

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kingpick_api_client
from kingpick_api_client.rest import ApiException
from kingpick_api_client.apis.auth_api import AuthApi


class TestAuthApi(unittest.TestCase):
    """ AuthApi unit test stubs """

    def setUp(self):
        self.api = kingpick_api_client.apis.auth_api.AuthApi()

    def tearDown(self):
        pass

    def test_token(self):
        """
        Test case for token

        
        """
        pass


if __name__ == '__main__':
    unittest.main()