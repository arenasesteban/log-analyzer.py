import logging
from collections import Counter

from .log_entry import LogEntry

logger = logging.getLogger(__name__)


def compute_logs_statistics(logs: list[LogEntry], invalid_lines: int, filter_level: str) -> dict:
    logger.info("Starting to compute log statistics")

    if not logs:
        logger.warning("No valid log entries found.")
        return {
            "total_logs": 0,
            "invalid_lines": invalid_lines,
            "levels": {}
        }
    
    if filter_level != "ALL":
        logs = filter_logs_by_level(logs, filter_level)

    summary = count_logs_by_level(logs, invalid_lines)

    logger.info(f"Finished computing log statistics.")

    return summary


def filter_logs_by_level(logs: list[LogEntry], filter_level: str) -> list[LogEntry]:
    return [log for log in logs if log.log_level == filter_level]


def count_logs_by_level(logs: list[LogEntry], invalid_lines: int) -> dict:
    summary = {
        "total_logs": len(logs),
        "invalid_lines": invalid_lines,
        "levels": Counter(log.log_level for log in logs)
    }

    logger.debug(f"Total logs: {summary['total_logs']}")
    logger.debug(f"Invalid lines: {summary['invalid_lines']}")
    logger.debug(f"Log levels count: {summary['levels']}")

    return summary
