# Log Processing Pipeline | CLI

This project implements a log processing pipeline that can be executed from the command line. The pipeline reads log files, processes them to extract useful information, and generates output in both text and CSV formats. The implementation includes error handling and unit tests to ensure robustness and reliability.

## Problem Statement

In many applications, log files are generated to record events, errors, and other important information. However, these log files can be large and difficult to analyze manually. The goal of this project is to create a command-line tool that can efficiently process log files, extract relevant information, and provide insights in a structured format.

The system process log file through the following steps:

```
Input Log File -> Log Parser -> Data Analyzer -> Output Generator
```

## Project Structure

```
log-processing-pipeline/
├── data/
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── analyzer.py
|   ├── log_entry.py
│   ├── utils.py
├── tests/
│   ├── test_parser.py
│   ├── test_analyzer.py
│   ├── test_integration.py
├── .gitignore
├── environment.yml
├── README.md
```

## Installation

To set up the environment for this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd log-processing-pipeline
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   micromamba env create -f environment.yml
   micromamba activate log-processing-pipeline
   ```

## Usage

To run the log processing pipeline, use the following command:

```bash
python -m src.main --file <path_to_log_file> --level <log_level> --output <path_to_output_directory>
```

### Command-Line Arguments

- `--file`: Path to the input log file (required).
- `--level`: Log level to filter (optional, default is "ALL").
- `--output`: Path to the output directory where results will be saved (optional, default is "output/").

## Testing

The project includes unit tests for the log parser and data analyzer, as well as integration tests for the entire pipeline.

To run the unit and integration tests, use the following command:

```bash
pytest tests/
```

## Credits

Esteban Arenas - Computer Science Student at the Universidad de Santiago de Chile (USACH) - [GitHub](https://github.com/arenasesteban)