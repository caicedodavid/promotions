from flask_injector import inject
from werkzeug.exceptions import NotFound

from project.mixins import TableMixin
from .models import Media
from .storage import StorageInterface


class MediaRepository(TableMixin):
    @inject
    def __init__(self, storage: StorageInterface):
        self.model = Media
        self.storage = storage

    def store_media(self, media_data: dict):
        url = self.storage.store_file(
            media_data.get('data'),
            media_data.get('name')
        )
        media = self.model(
            name=media_data.get('name'),
            ext=media_data.get('name').split('.')[-1],
            description=media_data.get('description'),
            url=url,
        )
        return media.save()

    def update_media(self, id, media_data: dict):
        media = self.get_or_fail(id)
        if not media:
            raise NotFound('Media not found')

        url = self.storage.store_file(
            media_data.get('data'),
            media_data.get('name')
        )
        media.name = media_data.get('name'),
        media.ext = media_data.get('name').split('.')[-1],
        media.description = media_data.get('descprition')
        media.url = url
        return media.save()
