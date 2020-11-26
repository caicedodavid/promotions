from dataclasses import dataclass
from typing import Tuple

from flask import jsonify, request
from injector import inject

from project.views import BaseView
from .repositories import MediaRepository
from .serializers import MediaSchema, LoadMediaSchema


@inject
@dataclass
class MediaAPI(BaseView):
    media_repository: MediaRepository
    media_schema: MediaSchema
    load_media_schema: LoadMediaSchema

    def get_one(self, id: int) -> Tuple:
        media = self.media_repository.get_or_fail(id)
        return jsonify(self.media_schema.dump(media)), 200

    def get_all(self) -> Tuple:
        media = self.media_repository.get_all()
        return jsonify(self.media_schema.dump(media, many=True)), 200

    def post(self) -> Tuple:
        media_data = self.load_media_schema.load(request.json)
        media = self.media_repository.store_media(media_data)
        return jsonify(self.media_schema.dump(media)), 201

    def put(self, id: str) -> Tuple:
        media_data = self.load_media_schema.load(request.json)
        media = self.media_repository.update_media(int(id), media_data)
        return jsonify(self.media_schema.dump(media)), 200
