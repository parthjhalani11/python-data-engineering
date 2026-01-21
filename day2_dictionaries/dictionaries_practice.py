                                                                # Dictionaries - Working with Key-Value Pairs

#Q1
'''user = {
    "name": "Parth",
    "age": 20,
    "city": "Delhi"
}

print(user['name'])
print(user['age'])
print(len(user))'''

#Q2
'''user = {
    "name": "Parth",
    "age": 20,
    "city": "Delhi"
}

user['email'] = 'partjhalani.com'
user['age'] = 21
print(user)'''

#Q3
'''data = {
    "order_id": 123,
    "amount": 450
}

print(data.get('status','not found'))'''

#Q4
'''orders = ["SUCCESS", "FAILED", "SUCCESS", "PENDING", "SUCCESS", "FAILED"]

counts = {}

for status in orders:
    if status in counts:
        counts[status] = counts[status] +1
    else:
        counts[status] = 1
print(counts)'''
        
#Q5
users = [
    {"id": 1, "name": "Parth", "active": True},
    {"id": 2, "name": "Rahul", "active": False},
    {"id": 3, "name": "Amit", "active": True}
]

for student in users:
    if student["active"] == True:
        print(student["name"])
