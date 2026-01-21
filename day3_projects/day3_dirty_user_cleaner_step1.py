
#RAW INPUT
raw_users = [
    "  Parth | 20 | delhi  ",
    "rahul|21|Mumbai",
    "  AMIT | 19 |  delhi",
    "parth | 20 | Delhi ",
    "Nikita| |Pune"
]

cleaned_users = []

for user in raw_users:
    parts = user.split("|")
    raw_name = parts[0].strip().title()
    raw_age = parts[1].strip()
    raw_city = parts[2].strip().title()
    if raw_age == "":
        age = None
    else:
        age = int(raw_age.strip())
    user_dict = {'name' : raw_name, 'age' : age, 'city' : raw_city}
    cleaned_users.append(user_dict)
print(cleaned_users)
