"""
data_cleaner.py

A reusable data cleaning pipeline built using core Python.

This script reads raw user data from a CSV file, cleans and normalizes
text fields, handles missing values, removes duplicate records, and
generates a summary report including total users, missing age count,
and users per city.

Designed to demonstrate end-to-end data cleaning logic without relying
on external libraries, making it suitable for lightweight automation
and environments where Pandas is not required.
"""
import csv
import os

def clean_user(test_user):
        
    parts = test_user.split("|")
    if len(parts) != 3:
        return None   
    raw_name = parts[0].strip().title()
    raw_age = parts[1].strip()
    raw_city = parts[2].strip().title()
        
    if raw_age == "":
        age = None
    else:
        age = int(raw_age)
                    
    return{
            "name":raw_name,
            "age":age,
            "city":raw_city
        }
    
def deduplicate_users(users):
        
    seen = set()
    unique = []
        
    for user in users:
        key = (user["name"], user["age"], user["city"])
            
        if key not in seen:
            seen.add(key)
            unique.append(user)
    return unique

def read_users_from_csv(filepath):
    users = []
    
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, filepath)
    
    with open(full_path, newline="") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            raw_user = f"{row['name']} | {row['age']} | {row['city']}"
            users.append(raw_user)

    return users

def main():
    raw_users = read_users_from_csv("users.csv")

    cleaned_users = []
    for ru in raw_users:
        user = clean_user(ru)
        if user is not None:
            cleaned_users.append(user)
    
    unique_users = deduplicate_users(cleaned_users)
    
    for user in unique_users:
        age = user["age"] if user["age"] is not None else "N/A"
        print(f"Name: {user['name']} | Age: {age} | City: {user['city']}")
    
    missing_age_count = 0
    
    for user in unique_users:
        if user["age"] is None:
            missing_age_count += 1
            
    city_counts = {}
    
    for user in unique_users:
        city = user["city"]
        
        if city in city_counts:
            city_counts[city] += 1 
        else:
            city_counts[city] = 1
    print("\nSummary Report")
    print(f"Total Users: {len(unique_users)}")
    print(f"Users with missing Age: {missing_age_count}")
    print("Users per City: ")
    
    for city, count in city_counts.items():
        print(f"- {city}: {count}")
if __name__ == "__main__":
    main()
