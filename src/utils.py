import os
import csv
import logging

logger = logging.getLogger(__name__)


def export_logs_summary(summary: dict, output_dir: str, file_path: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    file_name = file_path.split("/")[-1].split(".")[0]
    output_name = f"{output_dir}/{file_name}_output"

    logger.info(f"Exporting summary to {output_dir}")

    try:
        write_summary_to_txt(summary, output_name)
        write_summary_to_csv(summary, output_name)

        logger.info(f"Summary successfully exported")

    except IOError as e:
        logger.error(f"Failed to write summary: {e}")


def write_summary_to_txt(summary: dict, output_path: str) -> None:
    logger.info(f"Writing summary to {output_path}.txt")

    with open(f"{output_path}.txt", "w") as file:
        file.write(f"Total logs: {summary['total_logs']}\n")
        file.write(f"Invalid lines: {summary['invalid_lines']}\n")
        
        for key, value in summary['levels'].items():
            file.write(f"{key}: {value}\n")


def write_summary_to_csv(summary: dict, output_path: str) -> None:
    logger.info(f"Writing summary to {output_path}.csv")
    
    field_names = ["level", "count"]

    with open(f"{output_path}.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, field_names)
        writer.writeheader()

        for key, value in summary['levels'].items():
            writer.writerow({
                "level": key,
                "count": value
            })
