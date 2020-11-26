from os import makedirs
from tempfile import NamedTemporaryFile
from uuid import uuid4


def create_temp_file_from_bytes(
        data: bytes, suffix='txt') -> NamedTemporaryFile:
    """ Create and returns a temporary file.
    The returned file is a copy of the file argument
    MUST CLOSE THE FILE FOR REMOVAL
    Arguments:
        data {str} -- file data
    Returns:
        NamedTemporaryFile -- file
    """
    makedirs("tmp", exist_ok=True)
    temp_file = NamedTemporaryFile(dir='tmp', suffix='.' + suffix)
    temp_file.write(data)
    temp_file.seek(0)
    return temp_file


MIN_PREFIX_SIZE = 6
MAX_PREFIX_SIZE = 32


def add_random_prefix(string: str):
    prefix_size = max(MIN_PREFIX_SIZE, MAX_PREFIX_SIZE - len(string))
    return ''.join([str(uuid4().hex[:prefix_size]), string])
