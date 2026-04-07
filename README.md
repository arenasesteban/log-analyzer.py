# Log Processing Pipeline (CLI)

A command-line pipeline that turns structured log files into a reliable operational summary by parsing, validating, and analyzing entries before reporting results.

## Why This Project Exists

In many systems, logs are consumed for analysis without first checking data integrity.
That creates unreliable metrics and weakens operational decisions.

This project addresses that gap with a deterministic processing flow that:

- Parses each raw line into a domain object.
- Validates structural and semantic integrity.
- Separates valid and invalid entries.
- Computes summary statistics from valid logs.
- Exports a plain-text report for traceable review.

## Scope

This project is intentionally focused on offline log processing via CLI.

It is designed for:

- Single-file batch processing.
- Basic integrity validation.
- Aggregated summaries for quick diagnostics.

It is not designed for:

- Real-time streaming ingestion.
- Distributed processing.
- Dashboarding or long-term storage.

## Input Contract

Each log line is expected to follow this format:

`YYYY-MM-DD HH:MM:SS - LEVEL - COMPONENT - MESSAGE - CONTEXT`

Valid levels:

- `INFO`
- `WARNING`
- `ERROR`
- `DEBUG`

Any line that does not match the expected structure, or fails field validation, is marked as invalid.

## Processing Pipeline

The system is structured into four stages:

1. Parser
    Converts raw text lines into log entities.

2. Validator
    Applies explicit rules for timestamp format, level, component, and message.

3. Analyzer
    Computes totals, level/component counts, and time range.

4. Exporter
    Writes a text summary to the output directory.

This separation keeps responsibilities explicit and supports focused unit testing.

## Installation

1. Create the environment from the provided specification:

```bash
micromamba env create -f environment.yml
micromamba activate log-analyzer
```

## Usage

Base command:

```bash
python -m app.main --file input/sample_logs.txt
```

Filter by level:

```bash
python -m app.main --file input/sample_logs.txt --level ERROR
```

Custom output directory:

```bash
python -m app.main --file input/sample_logs.txt --output output
```

### CLI Arguments

- `--file`
   Path to the input log file (required).

- `--level`
   Optional level filter. Allowed values: `INFO`, `WARNING`, `ERROR`, `DEBUG`.

- `--output`
   Output directory for generated reports (optional, default: `output`).

## Output

Execution generates:

`<input_filename>_output.txt`

The report includes:

- Processed file name
- Total log lines
- Valid lines
- Invalid lines
- Counts by level
- Counts by component
- Time range (first and last valid timestamp)

## Testing

Current test strategy emphasizes unit-level verification for parser, validator, analyzer, and exporter behaviors.

Run tests with:

```bash
pytest tests/
```

## Project Structure

```text
.
├── README.md                   # Project documentation
├── environment.yml             # Environment and dependency management
├── pytest.ini                  # Test suite configuration
│
├── app/                        # Source code
│   ├── main.py                 # Application entry point
│   ├── core/                   # Core business logic
│   │   ├── __init__.py
│   │   ├── analyzer.py         # Data analysis logic
│   │   ├── exporter.py         # Data export utilities
│   │   ├── parser.py           # Input processing
│   │   └── validator.py        # Validation rules
│   └── models/                 # Data structures
│       ├── __init__.py
│       ├── log.py
│       ├── summary.py
│       └── validation_result.py
│
├── input/                      # Input data files
│   └── sample_logs.txt
│
├── output/                     # Generated output files
│   └── sample_logs_output.txt
│
└── tests/                      # Testing suite
    ├── conftest.py             # Shared test fixtures
    ├── integration/            # Integration tests
    │   └── test_integration.py
    └── unit/                   # Individual component tests
        ├── test_analyzer.py
        ├── test_exporter.py
        ├── test_parser.py
        └── test_validator.py
```

## Author

**Esteban Arenas** – Computer Science Student, Universidad de Santiago de Chile (USACH)