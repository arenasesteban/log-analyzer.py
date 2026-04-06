from app.core.validator import (
    validate_logs,
    validate_log_entry,
    is_valid_timestamp,
    is_valid_level,
    is_valid_component,
    is_valid_message    
)

""" Test for the log validator functions. """

# Test cases for validate_logs function

def test_validate_logs(logs_entries):
    valid_logs, invalid_logs = validate_logs(logs_entries)

    assert len(valid_logs) == 2
    assert len(invalid_logs) == 3


def test_validate_logs_with_all_valid_entries(logs_entries):
    valid_logs, invalid_logs = validate_logs(logs_entries[:2])

    assert len(valid_logs) == 2
    assert len(invalid_logs) == 0


def test_validate_logs_with_all_invalid_entries(logs_entries):
    valid_logs, invalid_logs = validate_logs(logs_entries[2:])

    assert len(valid_logs) == 0
    assert len(invalid_logs) == 3

# Test cases for validate_log_entry function

def test_validate_log_entry_with_valid_entry(valid_log_entry):
    validation_result = validate_log_entry(valid_log_entry)

    assert validation_result.is_valid
    assert len(validation_result.errors) == 0


def test_validate_log_entry_with_invalid_entry(invalid_log_entry):
    validation_result = validate_log_entry(invalid_log_entry)

    assert not validation_result.is_valid
    assert len(validation_result.errors) == 2
    assert validation_result.errors[0] == "Missing timestamp or invalid format"
    assert validation_result.errors[1] == "Invalid log level"


def test_validate_log_entry_with_component_and_message_empty(log_entry_with_component_and_message_empty):
    validation_result = validate_log_entry(log_entry_with_component_and_message_empty)

    assert not validation_result.is_valid
    assert len(validation_result.errors) == 2
    assert "Empty component" in validation_result.errors
    assert "Empty message" in validation_result.errors

# Test cases for is_valid_timestamp function

def test_is_valid_timestamp_with_valid_timestamp():
    assert is_valid_timestamp("2024-06-01 12:00:00") == True

def test_is_valid_timestamp_with_invalid_timestamp():
    assert is_valid_timestamp("2024/06/01 12:00:00") == False

# Test cases for is_valid_level function

def test_is_valid_level_with_valid_level():
    assert is_valid_level("INFO") == True

def test_is_valid_level_with_invalid_level():
    assert is_valid_level("CRITICAL") == False

# Test cases for is_valid_component function

def test_is_valid_component_with_valid_component():
    assert is_valid_component("auth-service") == True

def test_is_valid_component_with_empty_component():
    assert is_valid_component("") == False

# Test cases for is_valid_message function

def test_is_valid_message_with_valid_message():
    assert is_valid_message("User login successful") == True

def test_is_valid_message_with_empty_message():
    assert is_valid_message("") == False
