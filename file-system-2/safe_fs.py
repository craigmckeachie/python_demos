
from typing import ContextManager

from contextlib import contextmanager


@contextmanager
def safe_open(file_path, file_mode="r"):

    file_handle = None

    try:
        file_handle = open(file_path, file_mode)
    except IOError as exc:
        yield None, exc
    else:
        try:
            yield file_handle, None
        finally:
            file_handle.close()
