# CSV Log Parser

This project is a Python-based CSV log parser that reads log data from a CSV file, aggregates the data, and provides insights such as user activity and log level counts.

## Files

- **`data.csv`**: Contains sample log data with fields like date, time, level, user, and action.
- **`main.py`**: Implements the `CSVHandler` class to parse logs, count entries, and clear logs.
- **`utility.py`**: Contains the `Utility` class with helper methods for data aggregation.
- **`.gitignore`**: Specifies files and directories to be ignored by Git, such as `__pycache__/`.


## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository and navigate to the project directory.
3. Run the `main.py` script:
   ```bash
   python main.py