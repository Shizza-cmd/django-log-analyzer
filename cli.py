import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Django log analyzer")
    parser.add_argument("log_paths", nargs="+", help="Paths to log files")
    parser.add_argument("--report", dest="report_name", required=True, help="Report name")
    return parser.parse_args()
