from datetime import datetime

from app.core.analyzer import (
    compute_logs_statistics,
    filter_logs_by_level,
    analyze_logs,
    compute_time_range,
    compute_by_level_and_component
)

"""Tests for the log analyzer functions."""

# Test cases for compute_logs_statistics function

def test_compute_logs_statistics(valid_logs_for_analysis, invalid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis
    invalid_logs = invalid_logs_for_analysis

    summary = compute_logs_statistics(valid_logs, invalid_logs, filter_level=None)

    assert summary.total_logs == 4
    assert summary.valid_logs == 2
    assert summary.invalid_logs == 2
    assert summary.count_by_level == {"INFO": 1, "WARNING": 1}
    assert summary.count_by_component == {"auth-service": 2}
    assert summary.first_log_time == datetime.strptime("2024-06-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert summary.last_log_time == datetime.strptime("2024-06-01 12:01:00", "%Y-%m-%d %H:%M:%S")


def test_compute_logs_statistics_with_filter(valid_logs_for_analysis, invalid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis
    invalid_logs = invalid_logs_for_analysis

    summary = compute_logs_statistics(valid_logs, invalid_logs, filter_level="WARNING")

    assert summary.total_logs == 3
    assert summary.valid_logs == 1
    assert summary.invalid_logs == 2
    assert summary.count_by_level == {"WARNING": 1}
    assert summary.count_by_component == {"auth-service": 1}
    assert summary.first_log_time == datetime.strptime("2024-06-01 12:01:00", "%Y-%m-%d %H:%M:%S")
    assert summary.last_log_time == datetime.strptime("2024-06-01 12:01:00", "%Y-%m-%d %H:%M:%S")

def test_compute_logs_statistics_with_no_valid_logs():
    valid_logs = []
    invalid_logs = []

    summary = compute_logs_statistics(valid_logs, invalid_logs, filter_level=None)

    assert summary.total_logs == 0
    assert summary.valid_logs == 0
    assert summary.invalid_logs == 0
    assert summary.count_by_level == {}
    assert summary.count_by_component == {}
    assert summary.first_log_time is None
    assert summary.last_log_time is None

# Test cases for filter_logs_by_level function

def test_filter_logs_by_level(valid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis

    filtered_logs = filter_logs_by_level(valid_logs, filter_level="WARNING")

    assert len(filtered_logs) == 1
    assert filtered_logs[0].level == "WARNING"


def test_filter_logs_by_level_with_no_matching_logs(valid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis

    filtered_logs = filter_logs_by_level(valid_logs, filter_level="ERROR")

    assert len(filtered_logs) == 0

# Test cases for analyze_logs function

def test_analyze_logs(valid_logs_for_analysis, invalid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis
    invalid_logs = invalid_logs_for_analysis

    summary = analyze_logs(valid_logs, invalid_logs)

    assert summary.total_logs == 4
    assert summary.valid_logs == 2
    assert summary.invalid_logs == 2
    assert summary.count_by_level == {"INFO": 1, "WARNING": 1}
    assert summary.count_by_component == {"auth-service": 2}
    assert summary.first_log_time == datetime.strptime("2024-06-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert summary.last_log_time == datetime.strptime("2024-06-01 12:01:00", "%Y-%m-%d %H:%M:%S")


def test_analyze_logs_with_no_valid_logs(invalid_logs_for_analysis):
    valid_logs = []
    invalid_logs = invalid_logs_for_analysis

    summary = analyze_logs(valid_logs, invalid_logs)

    assert summary.total_logs == 2
    assert summary.valid_logs == 0
    assert summary.invalid_logs == 2
    assert summary.count_by_level == {}
    assert summary.count_by_component == {}
    assert summary.first_log_time is None
    assert summary.last_log_time is None


def test_analyze_logs_with_no_invalid_logs(valid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis
    invalid_logs = []

    summary = analyze_logs(valid_logs, invalid_logs)

    assert summary.total_logs == 2
    assert summary.valid_logs == 2
    assert summary.invalid_logs == 0
    assert summary.count_by_level == {"INFO": 1, "WARNING": 1}
    assert summary.count_by_component == {"auth-service": 2}
    assert summary.first_log_time == datetime.strptime("2024-06-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert summary.last_log_time == datetime.strptime("2024-06-01 12:01:00", "%Y-%m-%d %H:%M:%S")


def test_analyze_logs_with_no_logs():
    valid_logs = []
    invalid_logs = []

    summary = analyze_logs(valid_logs, invalid_logs)

    assert summary.total_logs == 0
    assert summary.valid_logs == 0
    assert summary.invalid_logs == 0
    assert summary.count_by_level == {}
    assert summary.count_by_component == {}
    assert summary.first_log_time is None
    assert summary.last_log_time is None

# Test cases for compute_time_range function

def test_compute_time_range_with_valid_logs(valid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis

    first_time, last_time = compute_time_range(valid_logs)

    assert first_time == datetime.strptime("2024-06-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert last_time == datetime.strptime("2024-06-01 12:01:00", "%Y-%m-%d %H:%M:%S")


def test_compute_time_range_with_no_logs():
    valid_logs = []

    first_time, last_time = compute_time_range(valid_logs)

    assert first_time is None
    assert last_time is None

# Test cases for compute_by_level_and_component function

def test_compute_by_level_and_component(valid_logs_for_analysis):
    valid_logs = valid_logs_for_analysis

    count_by_level, count_by_component = compute_by_level_and_component(valid_logs)

    assert count_by_level == {"INFO": 1, "WARNING": 1}
    assert count_by_component == {"auth-service": 2}


def test_compute_by_level_and_component_with_no_logs():
    valid_logs = []

    count_by_level, count_by_component = compute_by_level_and_component(valid_logs)

    assert count_by_level == {}
    assert count_by_component == {}