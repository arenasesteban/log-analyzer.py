import argparse

from parser import read_file
from analyzer import analyze_logs, write_summary


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer")

    parser.add_argument("--file-name", type=str, required=True, help="Path to the log file")
    parser.add_argument("--filter-level", type=str, required=False, choices=["INFO", "WARNING", "ERROR", "DEBUG"], default="ALL", help="Filter logs by level")
    parser.add_argument("--output-dir", type=str, required=False, default="../data/", help="Directory to save the output files")

    args = parser.parse_args()

    logs = read_file(args.file_name)
    summary = analyze_logs(logs, args.filter_level)
    write_summary(summary, args.output_dir, args.file_name)


if __name__ == "__main__":
    main()