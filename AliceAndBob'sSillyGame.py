import os
import sys

#
# Complete the sillyGame function below.
#
primes = [2]
def isPrime(x):
        for i in range(2, int(x ** .5) + 1):
            if not x % i: return False
        return True

def sillyGame(n):
    biggest_prime = primes[-1]
    if n > biggest_prime:
        for i in range(biggest_prime + 1, n + 1):
            if isPrime(i): primes.append(i)
    return 'Alice' if sum(i <= n for i in primes) % 2 else 'Bob'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        result = sillyGame(n)

        fptr.write(result + '\n')

    fptr.close()
