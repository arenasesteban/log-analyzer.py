from dataclasses import dataclass


@dataclass
class Log:
    timestamp: str | None = None
    level: str | None = None
    component: str | None = None
    message: str | None = None
    context: str | None = None
    raw_line: str | None = None