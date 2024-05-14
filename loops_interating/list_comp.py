squares = [ number * number for number in range(5) ]
print(squares)      # [0, 1, 4, 9, 16]





cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper()                      #transformation (also a selection because conditional present later on)
          for name in cats_colors           #iteration on a new line for readability
          if cats_colors[name] == 'orange'  #conditionals on new lines for readbility  
          if name[0] == 'L' ]               #2 conditionals same as nested conditionals
print(names)                                # ['LEO']