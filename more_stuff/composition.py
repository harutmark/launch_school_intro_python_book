print(list(range(3, 17, 4)))  
'''
for above code Python processes in this order:
1. looks at variables
2. feeds those variables to range
3. feeds rnage output to list
4 feeds list output to print
'''


def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

'''
sum = add(20, 45)
print(sum)                              # 65

difference = subtract(80, 10)
print(difference)                       # 70
'''

#Instead of the above, you can just do this:
print(add(20, 45))                      # 65
print(subtract(80, 10))                 # 70



#Here's a more complex example:
def times(num1, num2):
  return num1 * num2

print(times(add(20, 45), subtract(80, 10))) # 4550      # 4550 == ((20 + 45) * (80 - 10))
# line 35 same as lines 37-40:
total = add(20, 45)
difference = subtract(80, 10)
result = times(total, difference)
print(result)