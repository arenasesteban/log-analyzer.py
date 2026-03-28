from src.analyzer import (
    compute_logs_statistics,
    filter_logs_by_level,
    count_logs_by_level
)

"""Tests for the log analyzer functions."""

# Test cases for compute_logs_statistics function

def test_compute_logs_statistics_with_no_logs(empty_log_entries):
    summary = compute_logs_statistics(empty_log_entries, invalid_lines=5, filter_level="ALL")

    assert summary["total_logs"] == 0
    assert summary["invalid_lines"] == 5
    assert summary["levels"] == {}

def test_compute_logs_statistics_with_logs(log_entries):
    summary = compute_logs_statistics(log_entries, invalid_lines=2, filter_level="ALL")

    assert summary["total_logs"] == 3
    assert summary["invalid_lines"] == 2
    assert summary["levels"]["INFO"] == 1
    assert summary["levels"]["WARNING"] == 1
    assert summary["levels"]["ERROR"] == 1

def test_compute_logs_statistics_with_filter(log_entries):
    summary = compute_logs_statistics(log_entries, invalid_lines=2, filter_level="WARNING")

    assert summary["total_logs"] == 1
    assert summary["invalid_lines"] == 2
    assert summary["levels"]["WARNING"] == 1

# Test cases for filter_logs_by_level function

def test_filter_logs_by_level(log_entries):
    filtered_logs = filter_logs_by_level(log_entries, "WARNING")

    assert len(filtered_logs) == 1
    assert filtered_logs[0].log_level == "WARNING"

# Test cases for count_logs_by_level function

def test_count_logs_by_level(log_entries):
    summary = count_logs_by_level(log_entries, invalid_lines=2)

    assert summary["total_logs"] == 3
    assert summary["invalid_lines"] == 2
    assert summary["levels"]["INFO"] == 1
    assert summary["levels"]["WARNING"] == 1
    assert summary["levels"]["ERROR"] == 1