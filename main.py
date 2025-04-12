from cli import parse_args
from utils import validate_files, get_report_class
from parser import parse_log_file
from concurrent.futures import ProcessPoolExecutor
from reports.base import BaseReport


def main():
    args = parse_args()
    validate_files(args.log_paths)
    report_cls = get_report_class(args.report_name)

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(parse_log_file, args.log_paths))

    report = report_cls()
    for parsed_data in results:
        report.update(parsed_data)

    report.display()


if __name__ == "__main__":
    main()
