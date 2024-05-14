value = 5

'''
CLOUD9 DOES NOT SUPPORT PYTHON 3.10
MATCH STATEMENTS NOT SUPPORTED

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: #default case
        print('value is neither 5 nor 6')

USE IF INSTEAD OF MATCH
'''

if value == 5:
    print('value is 5')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')
# value is 5