import random
from datetime import datetime, timedelta
import os

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
HANDLERS = ["/api/items", "/api/status", "/auth/login", "/auth/logout", "/dashboard", "/metrics"]
LINES = 10_000  # можно регулировать объём

LOG_TEMPLATE = "{level} {timestamp} django.request path={handler}\n"


def random_timestamp(start: datetime, delta_sec: int) -> datetime:
    offset = timedelta(seconds=random.randint(0, delta_sec))
    return start + offset


def generate_logs(filename: str, lines: int = LINES):
    start_time = datetime(2024, 4, 1, 8, 0, 0)

    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(lines):
            level = random.choices(LOG_LEVELS, weights=[10, 40, 20, 20, 10])[0]
            handler = random.choice(HANDLERS)
            timestamp = random_timestamp(start_time, 3600)
            formatted = timestamp.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
            f.write(LOG_TEMPLATE.format(level=level, timestamp=formatted, handler=handler))


if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    generate_logs("logs/generated.log")
    print("Log file generated: logs/generated.log")
