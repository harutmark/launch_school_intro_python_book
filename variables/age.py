age = input('What is your age?\nAge: ')
age = int(age)

print(f'You are {age} years old.')
for i in range (10, 50, 10):
    age = age + 10
    print(f'In {i} years, you will be {age} years old.')
    