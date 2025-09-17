import math
def task_3_sign(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"

def task_3_primes():
    primes = []
    num = 2 # first prime number
    while len(primes) < 10:
        for i in range(2, int(math.sqrt(num)) + 1): # num ** 0.5 is equivalent to sqrt(num)
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def task_3_sum_numbers():
    i = 0
    total = 0
    while i <= 100:
        total += i
        i += 1
    return total

