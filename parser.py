import re
from collections import defaultdict
from typing import Dict

# LOG_PATTERN = re.compile(r"django\.requests - (?P<level>\w+) - (?P<path>/\S+)")
LOG_PATTERN = re.compile(
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+"
    r".*django\.request.*"
    r"path=(?P<path>\S+)"
)

def create_nested_defaultdict():
    return defaultdict(int)

def parse_log_file(path: str) -> Dict[str, Dict[str, int]]:
    counts = defaultdict(create_nested_defaultdict)

    with open(path, encoding="utf-8") as f:
        for line in f:
            match = LOG_PATTERN.search(line)
            if match:
                handler = match.group("path")
                level = match.group("level")
                counts[handler][level] += 1

    return counts
