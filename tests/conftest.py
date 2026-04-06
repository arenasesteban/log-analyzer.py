import pytest

from app.models.log import Log
from app.models.summary import Summary


""" Fixtures for testing the log parser functions. """

# Fixtures for load_logs function

@pytest.fixture
def log_file_path(tmp_path):
    log_file = tmp_path / "sample_logs.txt"
    log_file.write_text(
        "2024-06-01 12:00:00 - INFO - auth-service - User login successful - user_id=1234\n"
        "2024-06-01 12:01:00 - WARNING - auth-service - User login attempt failed - user_id=5678\n"
        "Invalid log line without proper format\n"
        "   \n"
    )
    return str(log_file)


@pytest.fixture
def log_file_path_with_valid_lines(tmp_path):
    log_file = tmp_path / "sample_logs_valid.txt"
    log_file.write_text(
        "2024-06-01 12:00:00 - INFO - auth-service - User login successful - user_id=1234\n"
    )
    return str(log_file)


@pytest.fixture
def log_file_path_with_invalid_line(tmp_path):
    log_file = tmp_path / "sample_logs_invalid.txt"
    log_file.write_text(
        "Invalid log line without proper format\n"
    )
    return str(log_file)


@pytest.fixture
def log_file_path_with_empty_line(tmp_path):
    log_file = tmp_path / "sample_logs_empty.txt"
    log_file.write_text(
        "   \n"
    )
    return str(log_file)

# Fixtures for parse_log_line function

@pytest.fixture
def sample_log_line():
    return "2024-06-01 12:00:00 - INFO - auth-service - User login successful - user_id=1234"

@pytest.fixture
def invalid_log_line():
    return "Invalid log line without proper format"

@pytest.fixture
def empty_log_line():
    return "   "


""" Fixtures for testing the log validator functions. """

# Fixtures for validate_logs function

@pytest.fixture
def logs_entries():
    return [
        Log(timestamp="2024-06-01 12:00:00", level="INFO", component="auth-service", message="User login successful", context="user_id=1234"),
        Log(timestamp="2024-06-01 12:01:00", level="WARNING", component="auth-service", message="User login attempt failed", context="user_id=5678"),
        Log(timestamp=None, level="ERROR", component="payment-service", message="Payment processing failed", context="order_id=9876"),
        Log(timestamp="2024-06-01 12:02:00", level="DEBUG", component="", message="Debugging information", context=""),
        Log(timestamp="2024-06-01 12:03:00", level="INFO", component="inventory-service", message="", context="")
    ]


@pytest.fixture
def valid_logs_entries():
    return [
        Log(timestamp="2024-06-01 12:00:00", level="INFO", component="auth-service", message="User login successful", context="user_id=1234"),
        Log(timestamp="2024-06-01 12:01:00", level="WARNING", component="auth-service", message="User login attempt failed", context="user_id=5678")
    ]


@pytest.fixture
def invalid_logs_entries():
    return [
        Log(timestamp=None, level="ERROR", component="payment-service", message="Payment processing failed", context="order_id=9876"),
        Log(timestamp="2024-06-01 12:02:00", level="DEBUG", component="", message="Debugging information", context=""),
        Log(timestamp="2024-06-01 12:03:00", level="INFO", component="inventory-service", message="", context="")
    ]

# Fixtures for validate_log_entry function

@pytest.fixture
def valid_log_entry():
    return Log(timestamp="2024-06-01 12:00:00", level="INFO", component="auth-service", message="User login successful", context="user_id=1234")


@pytest.fixture
def invalid_log_entry():
    return Log(timestamp=None, level="CRITICAL", component="payment-service", message="Payment processing failed", context="order_id=9876")


@pytest.fixture
def log_entry_with_component_and_message_empty():
    return Log(timestamp="2024-06-01 12:02:00", level="DEBUG", component="", message="", context="user_id=5678")

""" Fixture for testing the log analyzer functions. """

@pytest.fixture
def valid_logs_for_analysis():
    return [
        Log(timestamp="2024-06-01 12:00:00", level="INFO", component="auth-service", message="User login successful", context="user_id=1234"),
        Log(timestamp="2024-06-01 12:01:00", level="WARNING", component="auth-service", message="User login attempt failed", context="user_id=5678")
    ]

@pytest.fixture
def invalid_logs_for_analysis():
    return [
        (Log(timestamp=None, level="ERROR", component="payment-service", message="Payment processing failed", context="order_id=9876"), ["Missing timestamp or invalid format"]),
        (Log(timestamp="2024-06-01 12:02:00", level="CRITICAL", component="", message="Debugging information", context=""), ["Invalid log level", "Empty component"]),
    ]

""" Fixture for testing the log exporter functions. """

# Fixtures for export_logs_summary function

@pytest.fixture
def output_dir(tmp_path):
    return tmp_path / "output"

@pytest.fixture
def summary_for_export():
    return Summary(
        total_logs=10,
        valid_logs=8,
        invalid_logs=2,
        count_by_level={"INFO": 5, "WARNING": 3},
        count_by_component={"auth-service": 6, "payment-service": 4},
        first_log_time="2024-06-01 12:00:00",
        last_log_time="2024-06-01 12:10:00"
    )


@pytest.fixture
def empty_summary_for_export():
    return Summary(
        total_logs=0,
        valid_logs=0,
        invalid_logs=0,
        count_by_level={},
        count_by_component={},
        first_log_time=None,
        last_log_time=None
    )