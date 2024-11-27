import time

def factorial(x):
    if x <= 1:
        return x

    return x * factorial(x-1)

def factMem(x, memo: dict):
    if x in memo:
        return memo[x]

    if x <= 1:
        return 1

    memo[x] = x * factMem(x-1, memo)

    return memo[x]

def fib(x):
    if x <= 1:
        return x

    return fib(x-1) + fib(x-2)


def fibMem(n, memo: dict):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibMem(n-1, memo) + fibMem(n-2, memo)

    return memo[n]

def RUNM():
    N = 927

    print(f"N: {N}")
    # preA = time.time()
    # print(f"Normal fib: {fib(N)}")
    preB = time.time()
    # print(f"{1000*(preB-preA):.3f} ms")
    print(f"Memo fib: {fibMem(N, {})}")
    post = time.time()
    print(f"{1000 * (post - preB):.3f} ms")

    D = N
    print(f"\nN: {D}")
    preA = time.time()
    print(f"Normal fact: {factorial(D)}")
    preB = time.time()
    print(f"{1000*(preB-preA):.3f} ms")
    print(f"Memo fact: {factMem(D, {})}")
    post = time.time()
    print(f"{1000 * (post - preB):.3f} ms")


def is_prime_memoized(n, memo={}):
    if n in memo:
        return memo[n]

    if n < 2:
        memo[n] = False
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            memo[n] = False
            return False

    memo[n] = True
    return True


def find_primes_up_to(limit):
    primes = []
    memo = {}
    for num in range(2, limit + 1):
        if is_prime_memoized(num, memo):
            primes.append(num)
    return primes


def primeShit():
    preB = time.time()
    # Example usage
    limit = 163717100904197
    N = limit
    # primes = find_primes_up_to(limit)
    # print(f"Primes up to {limit}: {primes}")
    print(f"{N} is prime: {is_prime_memoized(N, {})}")
    post = time.time()
    print(f"{1000 * (post - preB):.3f} ms")

def claudePrimes():
    import random

    def miller_rabin(n, k=5):
        if n < 2: return False
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            if n % p == 0: return n == p
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d // 2
        for i in range(k):
            x = pow(random.randint(2, n - 1), d, n)
            if x == 1 or x == n - 1: continue
            for r in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1: break
            else:
                return False
        return True

    def is_prime_memoized(n, memo={}):
        if n in memo:
            return memo[n]
        result = miller_rabin(n)
        memo[n] = result
        return result

    def find_next_prime(n):
        while True:
            n += 1
            if is_prime_memoized(n):
                return n

    # Function to play your game
    def add_digit_for_prime(n):
        str_n = str(n)
        for i in range(len(str_n) + 1):
            for digit in '123456789':  # Skip 0 to avoid leading zeros
                new_num = int(str_n[:i] + digit + str_n[i:])
                if is_prime_memoized(new_num) and new_num > n:
                    return new_num
        return None  # If no prime found

    # Example usage
    # current_prime = 163717100904197
    # current_prime = 24221763717100904197
    # current_prime = 4572324221763717100904197
    # current_prime = 737845723324221763717100904197
    # current_prime = 79337884597923324221763717100904197
    # current_prime = 7634923378184597923324221763717100904197
    # current_prime = 5231762796349233378184597923324221763717100904197

    current_prime = 6342496456364781336357633635676986192634594635664769946284632619879161951236665952723653362156351786724796349283393678184597923324221763717100904197
    print(f"Starting prime: {current_prime}")

    for _ in range(99):  # Try 5 more rounds
        next_prime = add_digit_for_prime(current_prime)
        if next_prime:
            print(f"Next prime found: {next_prime}")
            current_prime = next_prime
        else:
            print("Couldn't find a larger prime by adding one digit.")
            break

claudePrimes()