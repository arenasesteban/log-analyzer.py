import logging
from pathlib import Path

from .models.summary import Summary

logger = logging.getLogger(__name__)


def export_logs_summary(summary: Summary, output_dir: str, file_path: str) -> None:
    input_name = Path(file_path).stem
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    txt_output_path = output_path / f"{input_name}_output.txt"

    logger.info(f"Exporting summary to {output_dir}")

    try:
        summary_text = format_summary(summary, input_name)
        write_summary(summary_text, txt_output_path)
        logger.info(f"Summary successfully exported")

    except IOError as e:
        logger.error(f"Failed to write summary: {e}")


def format_summary(summary: Summary, input_name: str) -> str:
    lines = [
        f"Processed file: {input_name}",
        f"Total logs: {summary.total_logs}",
        f"Valid lines: {summary.valid_logs}",
        f"Invalid lines: {summary.invalid_logs}",
        "-"*50
    ]

    if summary.count_by_level:
        lines.append("Counts by level:")
        for key, value in summary.count_by_level.items():
            lines.append(f"- {key}: {value}")
        lines.append("-"*50)

    if summary.count_by_component:
        lines.append("Counts by component:")
        for key, value in summary.count_by_component.items():
            lines.append(f"- {key}: {value}")
        lines.append("-"*50)

    lines.append("Time range:")
    lines.append(f"- First log time: {summary.first_log_time if summary.first_log_time else 'N/A'}")
    lines.append(f"- Last log time: {summary.last_log_time if summary.last_log_time else 'N/A'}")

    return "\n".join(lines)


def write_summary(content: str, output_path: Path) -> None:
    logger.info(f"Writing summary to {output_path}")

    with open(output_path, "w") as file:
        file.write(content)
