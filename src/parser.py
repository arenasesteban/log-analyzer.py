import logging
from pathlib import Path

from .models.log import Log

logger = logging.getLogger(__name__)


def load_logs(file_path: str) -> list[Log]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    logs = []

    logger.info(f"Starting to read logs from {file_path}")

    with open(file_path, "r") as file:
        for line in file:
            result = parse_log_line(line)
            logs.append(result)

    logger.info(f"Finished reading logs.")

    return logs


def parse_log_line(line: str) -> Log:
    line = line.strip()

    if not line:
        logger.warning("Empty line found.")
        return Log(raw_line=line) # Empty line

    line_parts = line.split(" - ", maxsplit=4)

    if len(line_parts) != 5:
        logger.warning("Line with invalid structure found.")
        return Log(raw_line=line) # Invalid log format
    
    timestamp, level, component, message, context = line_parts

    return Log(
        timestamp=timestamp,
        level=level,
        component=component,
        message=message,
        context=context,
        raw_line=line
    )