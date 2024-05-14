'''
greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')                   #Howdy Angie
print(greeting)                       #Salutations

#Python's default is to create & delete local var
#whenever a new var is created inside a func
#b/c of scope, it won't mess with global variables w/ same name
'''

#this behavior can be overridden w/ global and nonlocal statements:
greeting = 'Salutations'

def well_howdy(who):
    global greeting
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)


'''
def outer():
    def inner1():
        def inner2():
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")

        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()
inner2 -> 3 with id 4339312328
inner1 -> 2 with id 4339312296
outer -> 1 with id 4339312264
'''
 
#now using nonlocal statements:
def outer():
    def inner1():
        def inner2():
            nonlocal foo
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")

        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()
#inner2 -> 3 with id 4339312328
#inner1 -> 3 with id 4339312328       # Same as inner2
#outer -> 1 with id 4339312264
