import pytest

from src.log_entry import LogEntry

"""Fixtures for testing the log analyzer functions."""

@pytest.fixture
def log_file_path(tmp_path):
    log_file = tmp_path / "sample_logs.txt"
    log_file.write_text(
        "2024-06-01 12:00:00 - INFO - Sample log message\n"
        "2024-06-01 12:01:00 - WARNING - Another log message\n"
        "Invalid log line without proper format\n"
        "   \n"  # Empty line
    )
    return str(log_file)

@pytest.fixture
def log_file_path_only_valid(tmp_path):
    log_file = tmp_path / "valid_logs.txt"
    log_file.write_text(
        "2024-06-01 12:00:00 - INFO - Sample log message\n"
        "2024-06-01 12:01:00 - WARNING - Another log message\n"
    )
    return str(log_file)

@pytest.fixture
def sample_log_line():
    return "2024-06-01 12:00:00 - INFO - Sample log message"

@pytest.fixture
def invalid_log_line():
    return "Invalid log line without proper format"

@pytest.fixture
def empty_log_line():
    return "   "

@pytest.fixture()
def invalid_log_level_log_line():
    return "2024-06-01 12:00:00 - CRITICAL - Sample log message"


"""Fixtures for testing the log analyzer functions."""

@pytest.fixture
def log_entries():
    return [
        LogEntry(timestamp="2024-06-01 12:00:00", log_level="INFO", message="Sample log message"),
        LogEntry(timestamp="2024-06-01 12:01:00", log_level="WARNING", message="Another log message"),
        LogEntry(timestamp="2024-06-01 12:02:00", log_level="ERROR", message="Error log message")
    ]

@pytest.fixture
def empty_log_entries():
    return []
