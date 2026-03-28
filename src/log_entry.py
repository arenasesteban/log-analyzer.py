from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEntry:
    timestamp: datetime 
    log_level: str
    message: str

    def __post_init__(self) -> None:
        if isinstance(self.timestamp, str):
            self.timestamp = datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M:%S")
        if self.log_level not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
            raise ValueError(f"Invalid log level: {self.log_level}")