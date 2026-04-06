import logging
from datetime import datetime

from .models.log import Log
from .models.validation_result import ValidationResult

logger = logging.getLogger(__name__)

def validate_logs(logs: list[Log]) -> list[ValidationResult]:
    valid_logs = []
    invalid_logs = []

    for log in logs:
        validation = validate_log(log)

        if validation.is_valid:
            valid_logs.append(log)
        else:
            invalid_logs.append((log, validation.errors))

    return valid_logs, invalid_logs


def validate_log(log: Log) -> ValidationResult:
    errors = []

    if not is_valid_timestamp(log.timestamp):
        errors.append("Missing timestamp or invalid format")

    if not is_valid_level(log.level):
        errors.append("Invalid log level")

    if not is_valid_component(log.component):
        errors.append("Empty component")

    if not is_valid_message(log.message):
        errors.append("Empty message")

    is_valid = len(errors) == 0
    return ValidationResult(is_valid=is_valid, errors=errors)


def is_valid_timestamp(timestamp: datetime | None) -> bool:
    if timestamp is None:
        return False
    else:
        try:
            datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False


def is_valid_level(level: str) -> bool:
    valid_levels = {"INFO", "WARNING", "ERROR", "DEBUG"}

    if level not in valid_levels:
        return False
    
    return True


def is_valid_component(component: str) -> bool:
    if component is None or not component.strip():
        return False

    return True


def is_valid_message(message: str) -> bool:
    if message is None or not message.strip():
        return False

    return True
    