import os
from datetime import datetime

from log_entry import LogEntry


def read_file(file_name):
    file_path = f"../data/{file_name}"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_name}")

    logs = []

    with open(file_path, "r") as file:
        for line in file:
            result = parse_line(line)

            if result is not None:
                logs.append(result)

    return logs


def parse_line(line):
    line = line.strip()

    if not line:
        return None # Skip empty lines

    log = line.split(" - ")
    
    if len(log) != 3:
        return None # Invalid log format

    timestamp, level, message = log
    
    if not is_timestamp_valid(timestamp):
        return None # Invalid timestamp format
    if not is_level_valid(level):
        return None # Invalid log level
    if not is_message_valid(message):
        return None # Invalid log message
    
    return LogEntry(timestamp, level, message)


def is_timestamp_valid(timestamp):
    date_format = "%Y-%m-%d %H:%M:%S"
    
    try:
        datetime.strptime(timestamp, date_format)
        return True
    except ValueError:
        return None


def is_level_valid(level):
    levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

    if level not in levels:
        return None
    
    return True


def is_message_valid(message):
    if not message.strip():
        return None
    
    return True