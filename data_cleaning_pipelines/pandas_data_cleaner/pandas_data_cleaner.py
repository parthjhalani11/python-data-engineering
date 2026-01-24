"""
pandas_data_cleaner.py

An end-to-end data cleaning and analysis pipeline built using Pandas.

This script reads raw user data from a CSV file and performs
column-wise data cleaning, normalization, duplicate removal,
and summary reporting using Pandas’ vectorized operations.

The pipeline demonstrates real-world data engineering tasks such as
handling missing values, standardizing text data, deduplicating records,
and generating aggregated insights like user counts per city.

Designed for scalability and performance, this implementation reflects
industry-standard practices for working with tabular data using Pandas.
"""
import os
import pandas as pd

def main():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "users.csv")
    
    df = pd.read_csv(csv_path)
    
    df["name"] = df["name"].str.strip().str.title()
    df["city"] = df["city"].str.strip().str.title()
    
    df_dedup = df.drop_duplicates(subset=["name", "age", "city"])
    
    total_users = len(df_dedup)
    missing_age_count = df_dedup["age"].isna().sum()
    city_counts = df_dedup["city"].value_counts()
    
    print("\nSummary Report")
    print(f"Total Users: {total_users}")
    print(f"Users with missing age: {missing_age_count}")
    print("Users per city:")
    
    for city, counts in city_counts.items():
        print(f" - {city}: {counts}")
    
    
if __name__ == "__main__":
    main()
