import pytest

from app.core.parser import (
    load_logs, 
    parse_log_line
)


""" Tests for the log parser functions. """

# Test cases for load_logs function

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_logs("non_existent_file.txt")


def test_file_with_mixed_lines(log_file_path):
    logs = load_logs(log_file_path)

    assert len(logs) == 4


def test_file_with_valid_lines(log_file_path_with_valid_lines):
    logs = load_logs(log_file_path_with_valid_lines)

    assert len(logs) == 1
    assert logs[0].timestamp == "2024-06-01 12:00:00"
    assert logs[0].level == "INFO"
    assert logs[0].component == "auth-service"
    assert logs[0].message == "User login successful"
    assert logs[0].context == "user_id=1234"
    assert logs[0].raw_line == "2024-06-01 12:00:00 - INFO - auth-service - User login successful - user_id=1234\n"


def test_file_with_empty_line(log_file_path_with_empty_line):
    logs = load_logs(log_file_path_with_empty_line)

    assert len(logs) == 1
    assert logs[0].timestamp is None
    assert logs[0].level is None
    assert logs[0].component is None
    assert logs[0].message is None
    assert logs[0].context is None
    assert logs[0].raw_line == "   \n"


def test_file_with_invalid_line(log_file_path_with_invalid_line):
    logs = load_logs(log_file_path_with_invalid_line)

    assert len(logs) == 1
    assert logs[0].timestamp is None
    assert logs[0].level is None
    assert logs[0].component is None
    assert logs[0].message is None
    assert logs[0].context is None
    assert logs[0].raw_line == "Invalid log line without proper format\n"

# Test cases for parse_log_line function

def test_parse_empty_line(empty_log_line):
    log = parse_log_line(empty_log_line)

    assert log.timestamp is None
    assert log.level is None
    assert log.component is None
    assert log.message is None
    assert log.context is None
    assert log.raw_line == "   "


def test_parse_invalid_line(invalid_log_line):
    log = parse_log_line(invalid_log_line)

    assert log.timestamp is None
    assert log.level is None
    assert log.component is None
    assert log.message is None
    assert log.context is None
    assert log.raw_line == "Invalid log line without proper format"


def test_parse_valid_line(sample_log_line):
    log = parse_log_line(sample_log_line)

    assert log.timestamp == "2024-06-01 12:00:00"
    assert log.level == "INFO"
    assert log.component == "auth-service"
    assert log.message == "User login successful"
    assert log.context == "user_id=1234"
    assert log.raw_line == "2024-06-01 12:00:00 - INFO - auth-service - User login successful - user_id=1234"
