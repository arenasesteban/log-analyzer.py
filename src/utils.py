import csv


def write_txt(summary, output_path):
    with open(f"{output_path}.txt", "w") as file:
        file.write(f"Total logs: {summary['total_logs']}\n")
        
        for key, value in summary['levels'].items():
            file.write(f"{key}: {value}\n")


def write_csv(summary, output_path):
    field_names = ["level", "count"]

    with open(f"{output_path}.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, field_names)
        writer.writeheader()
        
        for key, value in summary['levels'].items():
            writer.writerow({
                "level": key,
                "count": value
            })
