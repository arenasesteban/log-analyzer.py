from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Summary:
    total_logs: int = 0
    valid_logs: int = 0
    invalid_logs: int = 0
    count_by_level: dict[str, int] = field(default_factory=dict)
    count_by_component: dict[str, int] = field(default_factory=dict)
    first_log_time: datetime | None = None
    last_log_time: datetime | None = None
