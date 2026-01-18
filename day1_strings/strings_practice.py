                                                              #strings


#Q!
'''name = "  Data Engineer  "
name = name.strip()
print (name.upper())'''

#Q2
'''email = "parth.jhalani@gmail.com"
parts = email.split('@')

username = parts[0]
domain = parts[1]

print (username)
print (domain)'''

#Q3
'''text = "python is awesome"

titled_text = text.title()

print(titled_text)'''

#Q4
'''data = "  order_id=123 | amount=450 | status=SUCCESS  "

data = data.replace('=',':')
data = data.strip()
data = data.split('|')
for order in data:
    print(order.strip())'''
    
#Q5
'''filename = "report_2025_01_16.csv"

filename = filename.split('.')
filename = filename[0].split('_')
filename = (filename[-3:])
print ("Date : ",'-'.join(filename))'''

#Q5
raw_name = "  paRTh   jHalAni "

name = raw_name.lower()
name = name.title()
name = name.split()
print ("Name :",' '.join(name))
