from abc import ABC, abstractmethod
from base64 import b64decode

from boto3 import client
from botocore.exceptions import ClientError
from flask import current_app
from werkzeug.exceptions import InternalServerError

from project.utils import add_random_prefix, create_temp_file_from_bytes


class StorageInterface(ABC):
    @abstractmethod
    def store_file(self, data: str, name: str) -> str:
        """ Store the file data and return the path to download it
        Arguments:
            data {str} -- file data
        Returns:
            str -- path to file
        """
        pass

    @abstractmethod
    def delete_file(self, path: str):
        """ Download and return the file data
        Arguments:
            data {str} -- file data
        Returns:
            str -- path to file
        """
        pass


class S3Storage(StorageInterface):
    AWS_S3_CLIENT = 's3'
    AWS_S3_HOST = 's3.amazonaws.com'

    def store_file(self, data: str, name: str) -> str:
        data_in_bytes = b64decode(data)
        temp_file = create_temp_file_from_bytes(data_in_bytes)
        # We add a prefix to avoid partition perfomance issues in s3
        new_file_name = add_random_prefix(name)
        s3_bucket_name = current_app.config.get('AWS_S3_BUCKET')
        s3_client = client(self.AWS_S3_CLIENT)
        path = '{}.{}/{}'.format(
            s3_bucket_name,
            self.AWS_S3_HOST,
            new_file_name
        )
        try:
            s3_client.upload_fileobj(temp_file, s3_bucket_name, new_file_name)
        except ClientError as e:
            raise InternalServerError('AWS Error: {}'.format(e.__str__))
        finally:
            temp_file.close()
        return path

    def delete_file(self, path: str):
        s3_bucket_name = current_app.config.get('AWS_S3_BUCKET')
        s3_client = client(self.S3_CLIENT)
        s3_filename = path.split('/')[-1]
        response = s3_client.delete_object(s3_bucket_name, s3_filename)
        deleted = response.get('DeleteMarker', False)
        if not deleted:
            raise InternalServerError('Media could not be deleted')
