def top():
    bottom()

def bottom():
    print('Reached the bottom')

top()

'''
Even though top is defined before bottom,
the code still works!
When you def a func, Python just saves it to the heap.
It only references them in the heap when you call the function.
We called it on line 7, meaning we called the function 
after both function had already been saved to the heap,
so we are good =)
What you can't do is call the function before defining it.
'''
'''
#The following will not work:
top()

def top():
    bottom()

def bottom():
    print('Reached the bottom')
'''  