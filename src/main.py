import argparse
import logging

from parser import read_logs
from analyzer import compute_logs_statistics
from utils import export_logs_summary

logger = logging.getLogger(__name__)

def main() -> None:
    logger.info("Starting Log Analyzer")

    parser = argparse.ArgumentParser(description="Log Analyzer")

    parser.add_argument("--file", type=str, required=True, help="Path to the log file")
    parser.add_argument("--level", type=str, required=False, default="ALL", choices=["INFO", "WARNING", "ERROR", "DEBUG", "ALL"], help="Filter logs by level")
    parser.add_argument("--output", type=str, required=False, default="../data/", help="Directory to save the output files")

    args = parser.parse_args()
    
    try:
        logs, invalid_lines = read_logs(args.file)

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return

    summary = compute_logs_statistics(logs, invalid_lines, args.level)
    export_logs_summary(summary, args.output, args.file)

    logger.info("Log Analyzer finished successfully.")

if __name__ == "__main__":
    main()