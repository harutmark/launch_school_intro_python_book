'''
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper()
# "MONTY PYTHON'S FLYING CIRCUS"

tv_show = tv_show.split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']
'''

#Instead of the above you can just do:
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper().split()              # ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']



#things can quickly messy quickly so try formatting for readability:
letters = 'abcdefghijklmnoqrstuvwxyz'
consonants = (letters.replace('a', '').
                      replace('e', '').
                      replace('i', '').
                      replace('o', '').
                      replace('u', ''))
print(consonants)    # bcdfghjklmnqrstvwxyz