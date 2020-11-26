import os
import json
from flask import current_app
from project._tests.base import BaseTestCase


class TestCreate(BaseTestCase):
    def test_health(self) -> None:
        with self.client:
            response = self.client.get('/health')
            self.assertStatus(response, 200)
