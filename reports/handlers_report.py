from reports.base import BaseReport
from collections import defaultdict


class HandlersReport(BaseReport):
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(int))
        self.total = 0

    def update(self, parsed_data):
        for handler, levels in parsed_data.items():
            for level, count in levels.items():
                self.data[handler][level] += count
                self.total += count

    def display(self):
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        handlers = sorted(self.data.keys())

        print(f"\nTotal requests: {self.total}\n")
        header = f"{'HANDLER':<24}\t" + "\t".join(f"{lvl:<8}" for lvl in levels)
        print(header)

        level_totals = dict.fromkeys(levels, 0)

        for handler in handlers:
            row = f"{handler:<24}\t"
            for level in levels:
                count = self.data[handler].get(level, 0)
                level_totals[level] += count
                row += f"{count:<8}\t"
            print(row)

        footer = f"{'':<24}\t" + "\t".join(f"{level_totals[lvl]:<8}" for lvl in levels)
        print("\n" + footer)
