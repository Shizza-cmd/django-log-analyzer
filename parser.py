import re
from collections import defaultdict
from typing import Dict


LOG_PATTERN = re.compile(
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+"
    r".*django.request.*"
    r"path=(?P<path>\S+)"
)


def parse_log_file(path: str) -> Dict[str, Dict[str, int]]:
    counts = defaultdict(lambda: defaultdict(int))

    with open(path, encoding="utf-8") as f:
        for line in f:
            match = LOG_PATTERN.search(line)
            if match:
                handler = match.group("path")
                level = match.group("level")
                counts[handler][level] += 1

    return counts
