'''
Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a 
prime and twice a square?
'''

'''
The approach I use for this problem will be:

Find next odd composite number n
For every prime p less than n
Check if (n - p) / 2 is square
If for all p < n there is no square found return n
'''
import math

class Goldbach:
    n: int = 9 # The current odd composite number
    primes: list[int] = [2, 3, 5, 7] # All primes < n

    def next_odd_composite(self):

        is_composite = True
        while(is_composite):

            self.n = self.n + 2 # Check next odd number. All even primes have been found (2)
            is_composite = False # Assume prime, then check if not prime. See 0007

            for p in self.primes:
                if self.n % p == 0:
                    # n is composite. Want to stop search and keep n
                    is_composite = True
                    return
            
            # n must be prime
            if not is_composite:
                self.primes.append(self.n)

            is_composite = True

    def check_sum(self) -> bool:
        for p in self.primes:
            x = (self.n - p) / 2 # Solve for the square number
            if math.sqrt(x) % 1 == 0: # Check whether the difference is square
                return True # There exists an appropriate sum
        return False # No appropriate sum found

def main():
    g = Goldbach()

    # Find the first odd composite that cannot be written as conjectered
    while(g.check_sum()):
        g.next_odd_composite()

    print(g.n)
    

if __name__ == "__main__":
    main()