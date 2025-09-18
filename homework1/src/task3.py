import math
def task_3_sign(x):
    """Return the sign of x."""
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"

def task_3_primes():
    """Return the first 10 prime numbers using a for loop."""
    primes = []
    num = 2 # first prime number
    while len(primes) < 10:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):  # num ** 0.5 is equivalent to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def task_3_sum_numbers():
    """Return the sum of all numbers 1 to 100."""
    i = 0
    total = 0
    while i <= 100:
        total += i
        i += 1
    return total

