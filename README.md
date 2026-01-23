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
