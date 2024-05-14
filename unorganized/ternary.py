# value1 if condition else value2

'''
INSTEAD OF WRITING...

if shape.sides() == 3:
    print("Triangle")
else:
    print("Square")
    
WE CAN WRITE A TERNARY SHORTHAND:

print("Triangle" if shape.sides() == 3 else "Square")
'''

print("Triangle" if shape.sides() == 3 else "Square")
