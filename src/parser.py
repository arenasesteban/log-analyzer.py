import os
import logging
from typing import Optional
from datetime import datetime

from .log_entry import LogEntry

logger = logging.getLogger(__name__)


def read_logs(file_path: str) -> tuple[list[LogEntry], int]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    logs = []
    invalid_lines = 0

    logger.info(f"Starting to read logs from {file_path}")

    with open(file_path, "r") as file:
        for line in file:
            result = parse_log_line(line)

            if result is None:
                invalid_lines += 1
            else:
                logs.append(result)

    logger.debug(f"Total lines read: {len(logs) + invalid_lines}, Valid entries: {len(logs)}, Invalid lines: {invalid_lines}")
    logger.info(f"Finished reading logs.")

    return logs, invalid_lines


def parse_log_line(line: str) -> Optional[LogEntry]:
    line = line.strip()

    if not line:
        logger.warning("Skipping empty line.")
        return None # Empty line

    log = line.split(" - ")
    
    if len(log) != 3:
        logger.warning("Skipping line with invalid format.")
        return None # Invalid log format

    timestamp, level, message = log
    
    if not is_valid_format(timestamp, level, message):
        logger.warning("Skipping line with invalid log entry.")
        return None # Invalid log format
    
    return LogEntry(timestamp, level, message)


def is_valid_format(timestamp: str, level: str, message: str) -> bool:
    return is_valid_timestamp(timestamp) and is_valid_level(level) and is_valid_message(message)


def is_valid_timestamp(timestamp: str) -> bool:
    date_format = "%Y-%m-%d %H:%M:%S"
    
    try:
        datetime.strptime(timestamp, date_format)
        return True
    
    except ValueError:
        return False


def is_valid_level(level: str) -> bool:
    levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

    if level not in levels:
        return False
    
    return True


def is_valid_message(message: str) -> bool:
    if not message.strip():
        return False
    
    return True