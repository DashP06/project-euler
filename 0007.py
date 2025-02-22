# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see the 6th prime is 13.
# What is the 10,001st prime number?

# Takes a list of all primes up to the highest prime, then finds the next highest prime.
def find_next(nums: list[int]) -> int:
    x = max(nums)
    primeFound = False

    while(not primeFound):
        x = x + 1 # Check next num
        # Assume the number is prime and then check if it is not prime
        primeFound = True
        for n in nums:
            if x % n == 0:
                primeFound = False

    return x


def main():
    primes = [2]
    n = int(input("Nth prime you want: ")) # nth prime
    for i in range(n - 1):
        primes.append(find_next(primes))
    print(primes[-1])


if __name__ == "__main__":
    main()
