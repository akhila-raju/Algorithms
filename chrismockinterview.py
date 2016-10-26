# getprimes(4) -> [1, 2, 3, 5]
# getprimes(6) -> [1, 2, 3, 5, 7, 11]
# prime: only factors are itself and 1

# GO DADDY internship interview
def getprimes(n):
    # return the first n primes
    primes = [1, 2, 3]
    index = 4
    while len(primes) < n:
        if isPrime(index):
            primes.append(index)
        index += 1
    return primes
    
# x / i % z -> x = i * z (what we want)
# we don't need to loop all from 2->x every time
# a number that isn't divisible by any lower primes, is prime
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# more efficient solution 
def getPrimes_2(n):
    primes = [1, 2, 3]
    index = 4
    while len(primes) < n:
        if isPrime_2(index, primes):
            primes.append(index)
        index += 1
    return primes

def isPrime_2(n, primes):
    for i in primes:
        if n % i == 0 and i != 1:
            return False
    return True
#test
print(getPrimes_2(5))

# magic_numbers([-10, -1, 2, 5]) -> True
# magic_numbers([-10, -1, 0, 1]) -> False
# def magic_numbers(arr):
    # return whether any index == arr[index]
    # for i in range(0, len(arr)):
    #     if i == arr[i]:
    #         return True
    # return False


# magic_numbers([-10, -1, 0, 1, 5]) -> False
# UBER INTERVIEW
def magic_numbers(arr):
    index = len(array) / 2
    mid = arr[index]  # 0 
    if mid == index:
        return True
    elif mid < index: # since it's sorted, we know that the numbers to the left will also be smaller
        # check second half
        index = index / 2
        mid = arr[index]
        
    else: # mid > index
        # index = index / 2
        # mid = arr[index]

# FEEDBACK:
# binary search - log(n) runtime
# really good problem solving methodology !!! - proactively use examples, taking
#     time and explain what i'm doing
# just ask if you're going in the right direction and you're not sure "how
#     does that look to you," "do you want me to go over anything"
# remember mod --> remainder and binary search --> cutting things in half
# technically - work on more of these problems. know key words
# easier side in terms of algorithms - more accurate of what to expect
# try to make sure it's right before running it