import pytest
from pathlib import Path

from app.core.exporter import (
    export_logs_summary,
    format_summary,
    write_summary   
)

""" Test for the log exporter functions. """

# Test cases for export_logs_summary function

def test_export_logs_summary(summary_for_export, log_file_path, output_dir):
    export_logs_summary(summary_for_export, output_dir, log_file_path)

    output_file = Path(output_dir) / f"{Path(log_file_path).stem}_output.txt"
    assert output_file.exists(), "Output file was not created"

    with open(output_file, "r") as file:
        content = file.read()
        assert "Processed file: sample_logs" in content
        assert "Total logs: 10" in content
        assert "Valid lines: 8" in content
        assert "Invalid lines: 2" in content
        assert "Counts by level" in content
        assert "- INFO: 5" in content
        assert "- WARNING: 3" in content
        assert "Counts by component" in content
        assert "- auth-service: 6" in content
        assert "- payment-service: 4" in content
        assert "Time range" in content
        assert "First log time: 2024-06-01 12:00:00" in content
        assert "Last log time: 2024-06-01 12:10:00" in content


def test_export_logs_summary_with_io_error(summary_for_export, log_file_path):
    invalid_output_path = Path("C://Windows/System32/invalid_dir/test_summary.txt")
    
    with pytest.raises(IOError):
        export_logs_summary(summary_for_export, invalid_output_path, log_file_path)

# Test cases for format_summary function

def test_format_summary(summary_for_export):
    result = format_summary(summary_for_export, "sample_logs")
    assert "Processed file: sample_logs" in result
    assert "Total logs: 10" in result
    assert "Valid lines: 8" in result
    assert "Invalid lines: 2" in result
    assert "Counts by level" in result
    assert "- INFO: 5" in result
    assert "- WARNING: 3" in result
    assert "Counts by component" in result
    assert "- auth-service: 6" in result
    assert "- payment-service: 4" in result
    assert "Time range" in result
    assert "First log time: 2024-06-01 12:00:00" in result
    assert "Last log time: 2024-06-01 12:10:00" in result

def test_format_summary_with_empty_data(empty_summary_for_export):
    result = format_summary(empty_summary_for_export, "empty_logs")
    assert "Processed file: empty_logs" in result
    assert "Total logs: 0" in result
    assert "Valid lines: 0" in result
    assert "Invalid lines: 0" in result
    assert "Counts by level" not in result
    assert "Counts by component" not in result
    assert "Time range" in result
    assert "First log time: N/A" in result
    assert "Last log time: N/A" in result

# Test cases for write_summary function

def test_write_summary(tmp_path):
    content = "Test summary content"
    output_path = tmp_path / "test_summary.txt"
    
    write_summary(content, output_path)

    assert output_path.exists(), "Output file was not created"

    with open(output_path, "r") as file:
        file_content = file.read()
        assert file_content == content, "Content written to file does not match expected content"

def test_write_summary_with_io_error():
    content = "Test summary content"
    invalid_output_path = Path("C://Windows/System32/invalid_dir/test_summary.txt")
    
    with pytest.raises(IOError):
        write_summary(content, invalid_output_path)
