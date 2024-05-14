num = 4936

#find ones place
ones = num % 10
print("Ones place is " + str(ones))

#find tens place
tens = num // 10
tens = tens % 10
print("Tens place is " + str(tens))

#find hundreds place
hundreds = num // 100
hundreds = hundreds % 10
print("Hundreds place is " + str(hundreds))

#find thousands place
thousands = num // 1000
thousands = thousands % 10
print("Thousands place is " + str(thousands))