import argparse
import logging

from src.parser import load_logs
from src.validator import validate_logs
from src.analyzer import compute_logs_statistics
from src.exporter import export_logs_summary

logger = logging.getLogger(__name__)

def main() -> None:
    logger.info("Starting Log Analyzer")

    parser = argparse.ArgumentParser(description="Log Analyzer")

    parser.add_argument("--file", type=str, required=True, help="Path to the log file")
    parser.add_argument("--level", type=str, required=False, default=None, choices=["INFO", "WARNING", "ERROR", "DEBUG"], help="Filter logs by level")
    parser.add_argument("--output", type=str, required=False, default="output", help="Directory to save the output files")

    args = parser.parse_args()
    
    try:
        logs = load_logs(args.file)

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return
    
    valid_logs, invalid_logs = validate_logs(logs)
    summary = compute_logs_statistics(valid_logs, invalid_logs, args.level)
    export_logs_summary(summary, args.output, args.file)

    logger.info("Log Analyzer finished successfully.")

if __name__ == "__main__":
    main()