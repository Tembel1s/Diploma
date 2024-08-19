from pathlib import Path
import os


def relative_path(path: str):
    return Path(__file__).parent.parent.parent.joinpath(path).absolute().__str__()

