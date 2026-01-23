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
    
def main():
    raw_users = [
        "  Parth | 20 | delhi  ",
        "rahul|21|Mumbai",
        "parth | 20 | Delhi ",
        "Nikita| |Pune"
    ]

    cleaned_users = []
    for ru in raw_users:
        user = clean_user(ru)
        if user is not None:
            cleaned_users.append(user)
    
    unique_users = deduplicate_users(cleaned_users)
    
    print(f"Total unique users: {len(unique_users)}\n")
    for user in unique_users:
        age = user["age"] if user["age"] is not None else "N/A"
        print(f"Name: {user['name']} | Age: {age} | City: {user['city']}")
    
if __name__ == "__main__":
    main()
