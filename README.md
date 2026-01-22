# Python Data Engineering

## Project Overview

This repository contains a series of Python practice exercises and a mini end-to-end data cleaning project.  
It is designed to help learn Python basics and core data engineering concepts such as text parsing, data cleaning, deduplication, and basic pipeline structuring.

---

## Folder Structure

- **day1_strings/** – Practice on string manipulation in Python  
- **day1_numbers/** – Practice on numeric operations and data types  
- **day2_lists_sets_tuples/** – Practice on containers: lists, sets, tuples  
- **day2_dictionaries/** – Practice on key-value data using dictionaries  
- **day3_projects/** – Contains the data cleaning project and its refactored functions  

---

## Mini Project: Dirty User Data Cleaner

This project demonstrates a simple pipeline to:

1. Take raw user description strings  
2. Clean them into structured dictionaries  
3. Remove duplicate users  
4. Provide deduplicated output  

---

## Example

```python
raw_users = [
    "  Parth | 20 | delhi  ",
    "rahul|21|Mumbai",
    "parth | 20 | Delhi ",
]

cleaned_users = [clean_user(u) for u in raw_users]
unique_users = deduplicate_users(cleaned_users)

print(unique_users)
