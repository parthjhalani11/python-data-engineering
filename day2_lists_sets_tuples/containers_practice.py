                                                                          #Lists, Tuples, and Sets


#Q1
'''numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(len(numbers))'''

#Q2
'''users = ["parth", "rahul", "parth", "amit", "rahul"]

clean_users = set(users)
print(clean_users)'''

#Q3
'''config = ("localhost", 5432, "admin")

config[1] = 3306
print(config)'''

#Q4
'''data = [1, 2, 2, 3, 4, 4, 5]

clean_data = set(data)
print(clean_data)
list_data = list(clean_data)
print(list_data)'''

#Q5
records = [
    ("order1", "SUCCESS"),
    ("order2", "FAILED"),
    ("order3", "SUCCESS"),
    ("order4", "PENDING"),
    ("order5", "SUCCESS")
]

for record in records:
    if record[1] == 'SUCCESS':
        print(record[0])
