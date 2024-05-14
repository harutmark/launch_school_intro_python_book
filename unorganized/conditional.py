value = int(input('Enter a number: '))

'''
    if value == 3:
       print('value is 3')
    else:
        if value == 4:
            print('value is 4')
        else:
            print('value is NOT 3 or 4')
            
    ELIF STATEMENTS CAN REPLACE NESTED IF STATEMENTS
'''

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass # We don't care about 9
else:
    print('value is something else')
    