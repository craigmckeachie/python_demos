
from typing import ContextManager

from contextlib import contextmanager
from pathlib import Path


@contextmanager
def safe_open(file_path, file_mode="r"):

    if not isinstance(file_path, Path):
        file_path = Path(file_path)

    file_handle = None

    try:
        file_handle = file_path.open(file_mode)
    except IOError as exc:
        yield None, exc
    else:
        try:
            yield file_handle, None
        finally:
            file_handle.close()
