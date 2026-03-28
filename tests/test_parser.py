import pytest
from datetime import datetime

from src.parser import (
    read_logs, 
    parse_log_line, 
    is_valid_format, 
    is_valid_timestamp, 
    is_valid_level, 
    is_valid_message
)

"""Tests for the log parser functions."""

# Test cases for read_logs function

def test_file_not_found():
    non_existent_file = "non_existent_file.txt"

    with pytest.raises(FileNotFoundError):
        read_logs(non_existent_file)

def test_file_with_valid_and_invalid_lines(log_file_path):
    logs, invalid_lines = read_logs(log_file_path)

    assert len(logs) == 2
    assert invalid_lines == 2

def test_file_with_only_valid_lines(log_file_path_only_valid):
    logs, invalid_lines = read_logs(log_file_path_only_valid)

    assert len(logs) == 2
    assert invalid_lines == 0

# Test cases for parse_log_line function

def test_parse_valid_log_line(sample_log_line):
    log_entry = parse_log_line(sample_log_line)

    assert log_entry is not None
    assert log_entry.timestamp == datetime.strptime("2024-06-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert log_entry.log_level == "INFO"
    assert log_entry.message == "Sample log message"

def test_parse_invalid_log_line(invalid_log_line):
    log_entry = parse_log_line(invalid_log_line)

    assert log_entry is None

def test_parse_empty_log_line(empty_log_line):
    log_entry = parse_log_line(empty_log_line)

    assert log_entry is None

def test_parse_log_line_with_invalid_level(invalid_log_level_log_line):
    log_entry = parse_log_line(invalid_log_level_log_line)

    assert log_entry is None

# Test cases for is_valid_format function

def test_valid_format():
    timestamp = "2024-06-01 12:00:00"
    level = "INFO"
    message = "Sample log message"
    assert is_valid_format(timestamp, level, message) == True

def test_invalid_format():
    timestamp = "2024-06-01 12:00:00"
    level = "CRITICAL"
    message = "Sample log message"
    assert is_valid_format(timestamp, level, message) == False

def test_invalid_timestamp_format():
    invalid_timestamp = "2024/06/01 12:00:00"
    level = "INFO"
    message = "Sample log message"
    assert is_valid_format(invalid_timestamp, level, message) == False

# Test cases for is_valid_timestamp function

def test_valid_timestamp():
    valid_timestamp = "2024-06-01 12:00:00"
    assert is_valid_timestamp(valid_timestamp) == True

def test_invalid_timestamp():
    invalid_timestamp = "2024/06/01 12:00:00"
    assert is_valid_timestamp(invalid_timestamp) == False

# Test cases for is_valid_level function

def test_valid_level():
    valid_level = "INFO"
    assert is_valid_level(valid_level) == True

def test_invalid_level():   
    invalid_level = "CRITICAL"
    assert is_valid_level(invalid_level) == False

# Test cases for is_valid_message function

def test_valid_message():
    valid_message = "Sample log message"
    assert is_valid_message(valid_message) == True

def test_invalid_message():
    invalid_message = "   "
    assert is_valid_message(invalid_message) == False