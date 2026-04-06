import logging
from datetime import datetime
from collections import Counter

from ..models.log import Log
from ..models.summary import Summary

logger = logging.getLogger(__name__)


def compute_logs_statistics(valid_logs: list[Log], invalid_logs: list[tuple[Log, list[str]]], filter_level: str | None) -> Summary:
    logger.info("Starting to compute log statistics.")

    if not valid_logs and not invalid_logs:
        logger.warning("No logs entries found for analysis.")
        return Summary()
    
    if filter_level is not None:
        valid_logs = filter_logs_by_level(valid_logs, filter_level)

    summary = analyze_logs(valid_logs, invalid_logs)
    logger.info("Finished computing log statistics")

    return summary


def filter_logs_by_level(logs: list[Log], filter_level: str) -> list[Log]:
    return [log for log in logs if log.level == filter_level]


def analyze_logs(valid_logs: list[Log], invalid_logs: list[tuple[Log, list[str]]]) -> Summary:
    total_logs = len(valid_logs) + len(invalid_logs)
    valid_count = len(valid_logs)
    invalid_count = len(invalid_logs)

    count_by_level, count_by_component = compute_by_level_and_component(valid_logs)
    first_time, last_time = compute_time_range(valid_logs)

    return Summary(
        total_logs=total_logs,
        valid_logs=valid_count,
        invalid_logs=invalid_count,
        count_by_level=count_by_level,
        count_by_component=count_by_component,
        first_log_time=first_time,
        last_log_time=last_time
    )


def compute_time_range(logs: list[Log]) -> tuple[datetime | None, datetime | None]:
    timestamps = []

    for log in logs:
        if log.timestamp is not None:
            parsed_timestamp = datetime.strptime(log.timestamp, "%Y-%m-%d %H:%M:%S")
            timestamps.append(parsed_timestamp)

    if not timestamps:
        return None, None

    return min(timestamps), max(timestamps)


def compute_by_level_and_component(logs: list[Log]) -> tuple[dict, dict]:
    count_by_level = Counter()
    count_by_component = Counter()

    for log in logs:
        count_by_level[log.level] += 1
        count_by_component[log.component] += 1
            
    return dict(count_by_level), dict(count_by_component)