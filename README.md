# Python Data Engineering

## Project Overview

This repository contains a series of Python practice exercises and a mini end-to-end data cleaning project.  
It is designed to learn Python fundamentals and core data engineering concepts such as text parsing, data cleaning, deduplication, defensive coding, and basic pipeline structuring.

---

## Folder Structure

- **day1_strings/** – Practice on string manipulation in Python  
- **day1_numbers/** – Practice on numeric operations and data types  
- **day2_lists_sets_tuples/** – Practice on containers: lists, sets, tuples  
- **day2_dictionaries/** – Practice on key-value data using dictionaries  

- **day3_projects/** – Dirty User Data Cleaner project (step-by-step evolution):
  - `day3_dirty_user_cleaner.py` – Initial script version
  - `day4_dirty_user_cleaner_functions.py` – Refactored using reusable functions
  - `day5_dirty_user_cleaner_pipeline.py` – Final pipeline with validation, main flow, and clean output

---

## Mini Project: Dirty User Data Cleaner

This mini project demonstrates how raw, inconsistent user data can be transformed into clean, structured, and deduplicated data using Python.

### Pipeline Overview

1. Accept raw user strings  
2. Clean and normalize data (name, age, city)  
3. Handle missing or invalid values safely  
4. Remove duplicate users  
5. Display clean, human-readable output  

---

## Day 5 Enhancements

On Day 5, the project was improved with real-world engineering practices:

- Introduced a `main()` function to control program flow  
- Added defensive coding to safely handle invalid or incomplete input  
- Ensured functions return predictable outputs (`dict` or `None`)  
- Implemented clean, human-readable output formatting  
- Used execution guard `if __name__ == "__main__"`  

These changes make the script more robust and closer to real data engineering pipelines.

---

## Example (Day 5 Pipeline)

### Input

```python
raw_users = [
    "  Parth | 20 | delhi  ",
    "rahul|21|Mumbai",
    "parth | 20 | Delhi ",
    "Nikita| |Pune"
]
```
Output

Total unique users: 3

Name: Parth  | Age: 20  | City: Delhi
Name: Rahul  | Age: 21  | City: Mumbai
Name: Nikita | Age: N/A | City: Pune
How to Use

Clone the repository

Navigate to the desired folder

Run any Python file using:

python <filename>.py


Example:

python day3_projects/day5_dirty_user_cleaner_pipeline.py

Future Work

Read raw data from CSV or JSON files

Add summary statistics (counts per city, missing values, etc.)

Write unit tests for data cleaning functions

Extend pipeline using Pandas

License

This project is open-source and free to use.
