from cli import parse_args
from utils import validate_files, get_report_class
from parser import parse_log_file
from concurrent.futures import ProcessPoolExecutor
from reports.base import BaseReport


def main():
    try:
        args = parse_args()

        try:
            validate_files(args.log_paths)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        try:
            report_cls = get_report_class(args.report_name)
        except ValueError as e:
            print(f"Error: {e}")
            return

        with ProcessPoolExecutor() as executor:
            results = list(executor.map(parse_log_file, args.log_paths))

        report: BaseReport = report_cls()
        for parsed_data in results:
            report.update(parsed_data)

        report.display()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()