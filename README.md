# Work Tracker Python

A small Python command-line tool that reads work records from a CSV file and summarizes completed work.

This project was created as a practical exercise in Python classes, CSV processing, functions, and exception handling.

## Features

* Reads work records from CSV
* Converts each row into a `Work` object
* Counts completed tasks
* Calculates total completed work time
* Finds the longest completed task
* Detects invalid CSV rows
* Prevents potentially incomplete data from being treated as a valid summary

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

## Usage

Place the CSV file at:

```text
work.csv
```

Then run:

```bash
python main.py
```

Example output:

```text
done count: 3
done total time: 135
done longest task: Python Learning
done longest time: 60
```

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
```

## Future Improvements

Possible improvements include:

```text
Support command-line file arguments
Export summary results to CSV or JSON
Add logging
Add automated tests
Rewrite the data analysis portion with pandas
```

## Purpose

The goal of this project is not only to produce a working script, but also to practice breaking a problem into small functions, handling invalid input, and writing code that can be modified later.
