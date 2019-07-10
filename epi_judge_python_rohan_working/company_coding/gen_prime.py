import math
# Sieve of Eratosthenes for generation of prime numbers

def solution(i):
    # your code here
    limit_of_sieve = 22000
    str_of_prime = gen_prime(limit_of_sieve)

    return str_of_prime[i:i + 5]


def gen_prime(limit_of_sieve):
    logical_prime_array = [False, False]

    for i in range(2, limit_of_sieve):
        logical_prime_array.append(True)

    for i in range(2, int(math.sqrt(limit_of_sieve))):
        if logical_prime_array[i] is True:
            p = i ** 2
            while p < limit_of_sieve:
                logical_prime_array[p] = False
                p += i

    list_of_all_prime = [str(num) for num in range(limit_of_sieve) if logical_prime_array[num] is True ]

    return "".join(list_of_all_prime)

if __name__ == '__main__':
    for i in range(5):
        print(solution(i))
        print("------>" + str(i))
