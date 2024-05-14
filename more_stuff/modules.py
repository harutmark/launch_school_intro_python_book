import math                 # Convention: import @ top of file

print(math.sqrt(math.pi))   # Note module.name format

#If you don't wanna write module.name all the time:
from math import pi, sqrt   # can lead to naming conlficts
print(sqrt(pi))             

#Or just use a shorter alias:
import math as m
print(m.sqrt(m.pi))
