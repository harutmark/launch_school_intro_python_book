principal = input('What is your initial investment?\n$')
principal = float(principal)

rate = input('What is the compounded interest rate in decimal format? (5% = 0.05)\nInterest Rate: ')
rate = float(rate)

time = input('For how many years will you collect interest?\nYears: ')
time = int(time)

balance = principal * ((1 + rate) ** time)

print(f'After {time} years you will have a balance of {balance}.')
