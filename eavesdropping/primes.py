#!/usr/bin/env python3
import argparse

def findPrimes(ceiling):
    if ceiling < 2:
        print("No primes below {}".format(ceiling))
        exit(1)

    # List of all primes found
    prime_list = []
    # Squares of all primes found
    prime_squares = []

    for number in range(2, ceiling):
        isPrime = True
        for index, prime in enumerate(prime_list):
            # Break on finding a factor
            if number % prime == 0:
                isPrime = False
                break

            # Break if all possible factors have been checked
            if prime_squares[index] > number: break

        # Store prime
        if isPrime:
            prime_list.append(number)
            prime_squares.append(number**2)

    return prime_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("max", help="Find all primes below max", type=int, default=1000, nargs='?')
    args = parser.parse_args()
    print("Primes below {}: {}".format(args.max, findPrimes(args.max)))

if __name__ == '__main__':
    main()
