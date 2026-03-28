from src.parser import read_logs
from src.analyzer import compute_logs_statistics
from src.utils import export_logs_summary

def test_integration(log_file_path, tmp_path):
    # Step 1: Read logs from the file
    logs, invalid_lines = read_logs(log_file_path)
    
    # Step 2: Compute statistics from the log entries
    summary = compute_logs_statistics(logs, invalid_lines, "ALL")
    
    # Step 3: Export the summary to a file
    output_dir = tmp_path
    export_logs_summary(summary, output_dir, log_file_path)
    
    # Verify results
    txt_file_path = f"{output_dir}/sample_logs_output.txt"
    csv_file_path = f"{output_dir}/sample_logs_output.csv"

    assert txt_file_path.exists()
    assert csv_file_path.exists()

    with open(txt_file_path, "r") as file:
        content = file.read()
        content = content.split("\n")

        assert "Total logs: 2" in content
        assert "Invalid lines: 2" in content
        assert "INFO: 1" in content
        assert "WARNING: 1" in content