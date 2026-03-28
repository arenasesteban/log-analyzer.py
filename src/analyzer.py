import csv

from utils import write_txt, write_csv

def analyze_logs(logs, filter_level):
    if filter_level != "ALL":
        logs = filter_logs_by_level(logs, filter_level)

    summary = summarize_logs(logs)
    return summary

def filter_logs_by_level(logs, filter_level):
    return [log for log in logs if log.log_level == filter_level]


def summarize_logs(logs):
    summary = {
        "total_logs": len(logs),
        "levels": {}
    }

    for log in logs:
        if log.log_level not in summary["levels"]:
            summary["levels"][log.log_level] = 0
        
        summary["levels"][log.log_level] += 1

    return summary

def write_summary(summary, output_dir, file_name):
    file_name = file_name.split(".")[0]
    output_dir = f"{output_dir}/{file_name}_output"

    write_txt(summary, output_dir)
    write_csv(summary, output_dir)
