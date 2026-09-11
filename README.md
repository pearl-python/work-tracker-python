# Work Tracker Python

A small Python command-line tool that reads work records from a CSV file and summarizes completed work.

This project was created as a practical exercise in Python classes, CSV processing, functions, exception handling, and automated testing.

## Features

* Reads work records from CSV
* Converts each row into a `Work` object
* Counts completed tasks
* Calculates total completed work time
* Finds the longest completed task
* Detects invalid CSV rows
* Prevents potentially incomplete data from being treated as a valid summary
* Includes automated tests with `pytest`

## CSV Format

Each row contains:

```text
name,time,status
```

Example:

```csv
Python Learning,60,done
Image Creation,90,doing
Document Review,30,done
```

The `time` field must be an integer.

The `status` field uses values such as:

```text
done
doing
```

## Project Structure

```text
work-tracker-python/
├─ main.py
├─ sample/
│  ├─ works.csv
│  ├─ works_invalid.csv
│  ├─ works_empty.csv
│  └─ works_no_done.csv
├─ tests/
│  └─ test_main.py
├─ README.md
├─ README_ja.md
└─ .gitignore
```

## Usage

The program uses the bundled sample file:

```text
sample/works.csv
```

Run the program from the project root:

```bash
python main.py
```

Example output:

```text
done件数:3
done合計時間:135
done最長時間:60
done最長タスク:Python Learning
```

The CSV path is passed to `load_works(file_path)`, so the same loader can be reused with different CSV files.

## Testing

This project uses `pytest` for automated testing.

Install pytest if necessary:

```bash
python -m pip install pytest
```

Run the test suite from the project root:

```bash
python -m pytest
```

The current test suite covers:

* Valid CSV input
* Invalid integer values
* Missing CSV columns
* Missing CSV files
* Empty CSV files
* Cases where no tasks have `done` status

All current tests are expected to pass successfully.

## Error Handling

The program detects several common CSV errors.

* Missing CSV file
* Non-integer values in the `time` field
* Missing columns

If invalid data is found, the program records the affected row and stops the final summary from being treated as valid.

Example:

```text
Data errors were found. Summary was cancelled.
Error row: 2
Error detail: invalid integer value
Error data: ['Image Creation', 'abc', 'done']
```

## What I Practiced

This project uses:

```text
Python classes
instance attributes
instance methods
lists
CSV processing
functions
try / except
FileNotFoundError
ValueError
IndexError
multiple return values
function arguments
if __name__ == "__main__"
pytest
assert
```

## Future Improvements

Possible improvements include:

```text
Support command-line file arguments
Export summary results to CSV or JSON
Add logging
Add GitHub Actions for automated test execution
Rewrite the data analysis portion with pandas
```

## Purpose

The goal of this project is not only to produce a working script, but also to practice breaking a problem into small functions, handling invalid input, testing expected behavior, and writing code that can be modified later.
