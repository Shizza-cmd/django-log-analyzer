import os
from reports.handlers_report import HandlersReport


def validate_files(paths: list[str]) -> None:
    for path in paths:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")


def get_report_class(name: str):
    mapping = {
        "handlers": HandlersReport
    }
    if name not in mapping:
        raise ValueError(f"Unsupported report type: {name}")
    return mapping[name]
