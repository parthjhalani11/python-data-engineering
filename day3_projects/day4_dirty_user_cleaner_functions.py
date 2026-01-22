def clean_user(test_user):
    parts = test_user.split("|")
    
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

def duplicate_users(users):
     seen = set()
     unique = []
     
     for user in users:
         key = (user["name"], user["age"], user["city"])
         
         if key not in seen:
             seen.add(key)
             unique.append(user)
     return unique

raw_users = [
    "  Parth | 20 | delhi  ",
    "rahul|21|Mumbai",
    "parth | 20 | Delhi ",
]

cleaned_users = []

for ru in raw_users:
    cleaned_users.append(clean_user(ru))
    
unique_users = duplicate_users(cleaned_users)

print(unique_users)
