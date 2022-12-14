input = 5
held = input
held_remainder = input
multiplier = 3
factors = {}
divisor = 3
remainders = {7:3}

def round (multiplier, divisor, current_factor, current_remainder):
    temp1 = current_factor
    temp2 = current_remainder
    next_factor = current_factor * multiplier
    traditional = next_factor % divisor
    next_remainder = current_remainder * multiplier % divisor
    print(f"Full factor starts with {temp1} and leaves a remainder of {traditional}")
    print(f"Holding only remainders starts with {temp2} and leaves a remainder of {next_remainder}")
    return (next_factor, next_remainder)
    #for m in multipliers:
        #factors[m] = factors[m] * m
        #for d in divisors:
            #traditional = factors[m] % d
            #modulo = remainders[d] * m % d
            #print(f"Full factor leaves a remainder of {traditional}")
            #print(f"Holding only remainders leaves a remainder of {modulo}")

for i in range(1,30):
    held, held_remainder = round(i, i//divisor + 1, held, held_remainder)
