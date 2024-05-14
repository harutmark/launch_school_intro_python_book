# Paste this code into the Python REPL
# Don't run it as a program

s = 'Hello, world!'
t = 'Hello, world!'
print(id(s) == id(t))         # False

s = 'supercalifragilisticexpialidocious'
t = 'supercalifragilisticexpialidocious'
print(id(s) == id(t))         # True

x = 5
y = 5
print(id(x) == id(y))         # True

x = 5
y = 6
print(id(x) == id(y))         # False
