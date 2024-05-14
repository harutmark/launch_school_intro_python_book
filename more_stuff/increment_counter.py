'''
def increment_counter():
    global counter
    counter += 1             #ignore the error, counter is initialized on next line
    
counter = 0

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101
'''

#This is a much more elegant solution:
def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()
