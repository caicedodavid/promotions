import json
import os
from typing import Tuple

from flask import jsonify
from flask.views import MethodView

from project.models import Products

class HealthAPI(MethodView):
    def get(self) -> Tuple:
        return jsonify(Products.objects[:20]), 200
