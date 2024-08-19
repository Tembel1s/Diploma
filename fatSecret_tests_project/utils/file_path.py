from pathlib import Path


def relative_path(path: str):
    return Path(__file__).parent.parent.joinpath(path).absolute().__str__()
